# -*- coding:utf-8 -*-
import asyncio
import datetime
import random
import time

import aiohttp
import asyncpg
from lxml import etree


class Task:

    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.first_queue = asyncio.Queue(maxsize=10000)
        self.second_queue = asyncio.Queue(maxsize=10000)
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
        self.sema = asyncio.Semaphore(Seam)
        self._ip = ""
        self._expiretime = None

    @property
    def ip(self):
        return f"http://{self._ip}"

    async def get_ip(self, sleep=0, create_task=True):
        url = "http://ip.ipjldl.com/index.php/api/entry?method=proxyServer.hdtiqu_api_url&packid=0&fa=0&dt=0&fetch_key=&qty=1&time=100&port=1&format=json&ss=5&css=&ipport=1&et=1&pro=&city="
        if sleep:
            await asyncio.sleep(sleep)
        if self._expiretime and self._expiretime > datetime.datetime.now() and (
                self._expiretime - datetime.datetime.now()).seconds > 5:
            print("还没到过期时间，过期时间:", self._expiretime.strftime("%Y-%m-%d %H:%M:%S"))
        else:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60),
                                             connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with self.sema, session.get(url) as response:
                    if response.status == 503:
                        print(f"无法访问:{url}")
                        self.loop.call_soon_threadsafe(self.loop.stop)
                        return
                    result = await response.json(content_type=None)
            data = result['data']
            if not data:
                print(f"没获取到ip:{result['msg']}")
                self.loop.call_soon_threadsafe(self.loop.stop)
                return
            try:
                self._expiretime = datetime.datetime.strptime(data[0]['ExpireTime'], "%Y-%m-%d %H:%M:%S")
            except KeyError:
                print("没有过期时间:", result)
                self.loop.call_soon_threadsafe(self.loop.stop)
                return
            print(data)
            self._ip = [i['IP'] for i in data][0]

        sleep = (self._expiretime - datetime.datetime.now()).seconds - 5
        if create_task:
            asyncio.ensure_future(self.get_ip(sleep=sleep > 1000 and 0 or sleep))

    async def set_up(self, then):
        self.db = await asyncpg.create_pool(host="127.0.0.1",
                                            database='data_aliexpress',
                                            user='postgres',
                                            password="mmhjd123")
        await self.get_ip()
        asyncio.ensure_future(getattr(self, then)())

    async def get(self, url, params, retry=0, **kwargs):
        try:
            async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=60),
                                             connector=aiohttp.TCPConnector(ssl=False)) as session:
                async with self.sema, session.get(url, params=params, headers=self.headers, proxy=self.ip,
                                                  **kwargs) as response:
                    return await response.text()
        except Exception as e:
            await self.get_ip(create_task=False)
            if retry < 3:
                return await self.get(url, params, retry + 1, **kwargs)
            else:
                raise e

    async def first_step(self):
        # 加载conf数据 执行第一部每个start_url 一个进程 进程内跑协程
        asyncio.ensure_future(self.collect_first())
        asyncio.ensure_future(self.first_task_check_stop())
        async with self.db.acquire() as connection:
            async with connection.transaction():
                statement = '''SELECT start_url,min_price,max_price,freq FROM crawl_category_conf WHERE stat = 1;'''
                for row in await connection.fetch(statement):
                    start_url = row['start_url']
                    min_price = row['min_price'] or 0
                    max_price = row['max_price'] or 0
                    freq = row['freq'] or 1
                    if max_price < min_price:
                        max_price = min_price = 0
                    for i in range(freq):
                        asyncio.ensure_future(self.get_id_meta_first(start_url, min_price, max_price))

    async def get_id_meta_first(self, url, min_price, max_price):
        # 第一阶段
        for page in range(1, 101):
            params = {
                "page": str(page),
                'SortType': 'total_tranpro_desc',
            }
            if min_price:
                params.update(minPrice=str(min_price))
            if max_price:
                params.update(maxPrice=str(min_price))
            asyncio.ensure_future(self.get_id_meta_subtask(url, params=params))

    async def get_id_meta_subtask(self, url, params):
        response = None
        try:
            cur_time = datetime.datetime.now().date()
            response = await self.get(url=url, params=params)
            parsehtml = etree.HTML(response)
            order_48 = parsehtml.xpath('//li[{}]/div/div/div[@class="rate-history"]/span[3]/a/em/text()'.format(48))[0][
                       10:-1]
            order_1 = parsehtml.xpath('//li[{}]/div/div/div[@class="rate-history"]/span[3]/a/em/text()'.format(1))[0][
                      10:-1]
            if int(order_48) > 300 or int(order_1) < 100:
                return
            cat_name = url.split(r'/')[-1].split(r'.', 1)[0]
            for i in range(1, 101):
                price = parsehtml.xpath('//li[{}]/div/div/span/span[1]/text()'.format(i))[0]
                if '-' in price:
                    price = price[price.index('$'):price.index('-') - 1]
                else:
                    price = price[price.index('$') + 1:-1]
                # votes = parsehtml.xpath('//*[@id="list-items"]/ul/li[{}]/div/div/div[@class="rate-history"]/a/text()'.format(i))[0][1:-1]
                # orders = parsehtml.xpath('//li[{}]/div/div/div[@class="rate-history"]/span[3]/a/em/text()'.format(i))[0][10:-1]
                rating = parsehtml.xpath('//*[@id="list-items"]/ul/li[{}]/div/div/div/span[1]/@title'.format(i))[0][
                         13:16]
                link = 'https:' + parsehtml.xpath('//li[{}]/div/div/h3/a/@href'.format(i))[0].split('?')[0]
                pid = link.split('/')[-1].split('.')[0]
                if pid and price and rating and link and cat_name:
                    # if int(orders) >= 10 and int(orders) <= 300:
                    # print(3333333333333333333333333)
                    await self.first_queue.put(
                        [int(pid), float(price[1:] if price.startswith("$") else price), link, cat_name, cur_time])
        except Exception as e:
            pass
            # print(f"有报错{e}")
        finally:
            if response is None:
                pass
                # print(f"{url}获取信息失败")

    async def collect_first(self):
        res = []
        while True:
            data = await self.first_queue.get()
            if data is None:
                await self.bulk_first(res)
                self.loop.call_soon_threadsafe(self.loop.stop)
                return
            else:
                res.append(data)
            if len(res) % 300 == 0:
                await self.bulk_first(res)
                res = []

    async def first_task_check_stop(self):
        while True:
            await asyncio.sleep(1)
            if len(asyncio.Task.all_tasks()) == 3:
                await self.first_queue.put(None)
                return

    async def bulk_first(self, bulk):
        async with self.db.acquire() as connection:
            async with connection.transaction():
                statement = '''
                            INSERT INTO product_id_meta (  pid, price, link, cat_name, stat,date )
                            VALUES
                                (  $1, $2,$3,$4,1,$5 ) ON conflict ( pid ) DO NOTHING;
                '''
                await connection.executemany(statement, bulk)

    async def second_step(self):
        # 每1w个url放入一个进程，进程内部用协程爬取（asyncio并发量设为500--asyncio.Semaphore）
        asyncio.ensure_future(self.collect_second())
        asyncio.ensure_future(self.second_task_check_stop())
        async with self.db.acquire() as connection:
            async with connection.transaction():
                statement = '''SELECT link,cat_name FROM product_id_meta WHERE stat = 1;'''
                for row in await connection.fetch(statement):
                    asyncio.ensure_future(self.get_info_meta_subtask(row['link'], row['cat_name']))

    async def get_info_meta_subtask(self, url, cat_name):
        cur_time = datetime.datetime.now().date()
        try:
            response = await self.get(url=url, params=None)
            parsehtml = etree.HTML(response)

            price = parsehtml.xpath('//*[@id="j-sku-discount-price"]/text()')[0]
            if price == ' - ':
                price = parsehtml.xpath('//*[@id="j-sku-discount-price"]/span[1]/text()')[0]
            votes = parsehtml.xpath('//*[@id="j-customer-reviews-trigger"]/span[3]/text()')[0]
            pic_url = parsehtml.xpath('//*[@id="magnifier"]/div[1]/a/img/@src')[0]
            votes = votes[1:votes.index(' ')]
            rating = parsehtml.xpath('//*[@id="j-customer-reviews-trigger"]/span[2]/text()')[0]
            orders = parsehtml.xpath('//*[@id="j-order-num"]/text()')[0]
            orders = orders[0:orders.index(' ')]
            link = url
            pid = link[link.rindex('/') + 1:link.rindex('.')]
            if pid and price and votes and rating and link and cat_name and pic_url:
                await self.second_queue.put(
                    [int(pid), float(price), int(votes), int(orders), float(rating), pic_url, link, cat_name,
                     cur_time])

        except Exception as e:
            print(f"second:{e}")
            pass

    async def collect_second(self):
        res = []
        while True:
            data = await self.second_queue.get()
            if data is None:
                await self.bulk_second(res)
                self.loop.call_soon_threadsafe(self.loop.stop)
                return
            else:
                res.append(data)
            if len(res) % 500 == 0:
                await self.bulk_second(res)
                res = []

    async def second_task_check_stop(self):
        while True:
            await asyncio.sleep(1)
            if len(asyncio.Task.all_tasks()) <= 4:
                await self.second_queue.put(None)
                return

    async def bulk_second(self, bulk):
        async with self.db.acquire() as connection:
            async with connection.transaction():
                statement = '''
                                INSERT INTO product_info_meta (  pid, price, votes, orders, rating,pic_url,link,cat_name,date )
                                VALUES
                                    ( $1, $2, $3,$4,$5,$6 ,$7,$8,$9);
                    '''
                await connection.executemany(statement, bulk)


if __name__ == '__main__':
    start = time.time()
    Seam = 100

    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    task = Task()
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(task.set_up(then="first_step"))
    loop.run_forever()

    for t in asyncio.Task.all_tasks():
        t.cancel()
    task = Task()
    asyncio.ensure_future(task.set_up(then="second_step"))
    loop.run_forever()

    print(time.time() - start)
