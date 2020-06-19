# coding:utf-8
import pymysql


# 连接本地数据库
def get_conn():
    """
    :return: 连接，游标
    """
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="huihuiyo",
                           db="books",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    return conn, cursor


# 关闭本地数据库
def close_conn(conn, cursor):
    cursor.close()
    conn.close()


def get_books_data():
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select book,num from book_freq limit 60"
    count = cursor.execute(sql)
    res = cursor.fetchall()
    for out in res:
        data_dict[out[0]] = out[1]
    close_conn(conn, cursor)
    return data_dict
  

if __name__ == '__main__':
  testlist = get_books_data()
  print(testlist)