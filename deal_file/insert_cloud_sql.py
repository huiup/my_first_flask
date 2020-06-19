# coding:utf-8
import pymysql.cursors
from utils import *


# 将本地数据插入到云服务器数据库中
def get_local_books_data():
    try:
        conn, cursor = get_conn()
        sql = "select url,low,mid,high from book_data"
        count = cursor.execute(sql)
        # res = cursor.fetchone()
        res = cursor.fetchall()
        data_list = []
        for out in res:
            data_list.append(
                {"url": out[0], "low": out[1], "mid": out[2], "high": out[3]})
        close_conn(conn, cursor)
        return data_list
    except Exception as e:
        print(e)


def insert_data(*args):
    try:
        conn, cursor = get_conn_cloud()
        sql = "insert into book_data (`url`,`low`,`mid`,`high`) values(%s,%s,%s,%s);"
        cursor.execute(sql, args)
        conn.commit()
        close_conn_cloud(conn, cursor)
        print('添加成功', args[0])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    book_list = get_local_books_data()
    for line in book_list:
        url = line['url']
        low_data = line["low"].replace(' ', '').replace('*', '·').replace('•','·')
        mid_data = line["mid"].replace(' ', '').replace('*', '·').replace('•','·')
        high_data = line["high"].replace(' ', '').replace('*', '·').replace('•','·')
        insert_data(url, low_data, mid_data, high_data)
