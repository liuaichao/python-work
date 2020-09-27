# -*- coding:utf-8 -*-
class ServerContent():
    def return_data(self):
        ip = '127.0.0.1'
        port = '9998'
        head_protocal = 'HTTP/1.1'
        head_code_200 = '200'
        head_status_OK = 'OK'
        head_content_length = 'Content-Length:'
        head_content_type = 'Content-Type:'
        content_type_html = 'text/html'
        blank_line = ''
        return {'ip':ip, 'port':port, 'head_protocal':head_protocal, 'head_code_200':head_code_200,
                'head_status_OK':head_status_OK, 'head_content_length':head_content_length,
                'head_content_type':head_content_type, 'content_type_html':content_type_html,
                'blank_line':blank_line}