# coding:utf-8
from utils import *
import re
import pandas as pd

# 提取txt文件中的数据，存入本地数据库，
def get_txt(txt_path):
    with open(txt_path,'r',encoding='utf-8') as f:
        url = f.readline()
        txt = f.read()
    return url, txt
def clean_txt(txt):
    txt = txt.replace('?','·').replace('．','·').replace(' ','').replace('•','·')
    text = re.findall(r'《(.*?)》',txt)
    text_list = []
    for x in text:
        if x not in text_list:
            text_list.append(x)
    list12 = text_list[:35]
    list34 = text_list[35:76]
    list56 = text_list[76:]
    # # print(text_list)
    pd.set_option('display.max_rows',None)
    print(pd.Series(text_list))
    # print(pd.Series(list12))
    # print(pd.Series(list34))
    # print(pd.Series(list56))
    low = str(list12)
    mid = str(list34)
    high = str(list56)

    return low,mid,high
def insert(*args):
    try:
        conn, cursor = get_conn()
        sql = "insert into book_data (`url`,`low`,`mid`,`high`) values(%s,%s,%s,%s);"
        cursor.execute(sql, args)
        conn.commit()
        close_conn(conn, cursor)
        print('添加成功')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    path = r'./data/部编版小学1-6年级课外阅读书单推荐，值得收藏！_孩子.txt'
    txt_url, txt = get_txt(path)
    # print(txt_url)
    a, b, c = clean_txt(txt)
    # insert(txt_url,a,b,c)
