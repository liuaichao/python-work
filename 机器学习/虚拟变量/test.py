# -*- coding:utf-8 -*-
import pandas as pd
demo_df = pd.DataFrame({'int':[0,1,2,1],'str':['s', 'f', 's', 'b']})
demo_df = pd.get_dummies(demo_df, columns=['int', 'str'])
print(demo_df)


a = {
    'a':1
}