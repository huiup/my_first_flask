# coding:utf-8
import operator

import pymysql
import pprint


def get_conn():
    # 创建连接
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="huihuiyo",
                           db="books",
                           charset="utf8")
    # 创建游标
    cursor = conn.cursor()
    return conn, cursor


def close_conn(conn, cursor):
    cursor.close()
    conn.close()


# 总的书目推荐次数
def get_all_data():
    book_list = []
    num_list = []
    conn, cursor = get_conn()
    sql = "select book,num from book_freq limit 50"
    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        book_list.append(line[0])
        num_list.append(line[1])
    close_conn(conn, cursor)
    return book_list, num_list


# 推荐书目数量分布
def get_freq_data():
    list1 = []
    list2 = []
    conn, cursor = get_conn()
    sql = "select num,count(num) from book_freq group by num"
    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        list1.append(line[0])
        list2.append(line[1])
    close_conn(conn, cursor)
    return list1, list2


# 低年级书目推荐次数
def get_low_data():
    book_list = []
    num_list = []
    conn, cursor = get_conn()
    sql = "select book,num from 12_book_freq limit 35"
    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        book_list.append(line[0])
        num_list.append(line[1])
    close_conn(conn, cursor)
    return book_list, num_list


# 中年级书目推荐次数
def get_mid_data():
    book_list = []
    num_list = []
    conn, cursor = get_conn()
    sql = "select book,num from 34_book_freq limit 35"
    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        book_list.append(line[0])
        num_list.append(line[1])
    close_conn(conn, cursor)
    return book_list, num_list


# 高年级书目推荐次数
def get_high_data():
    book_list = []
    num_list = []
    conn, cursor = get_conn()
    sql = "select book,num from 56_book_freq limit 35"
    cursor.execute(sql)
    res = cursor.fetchall()
    for line in res:
        book_list.append(line[0])
        num_list.append(line[1])
    close_conn(conn, cursor)
    return book_list, num_list


# 获取推荐书目top100的国家
def get_top100_country():
    data_list = []
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select country,count(country) from top100_country group by country"
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        name = x[0]
        if name == '苏格兰':
            name = 'United Kingdom'
        elif name == '英国':
            name = 'United Kingdom'
        elif name == '法国':
            name = 'France'
        elif name == '意大利':
            name = 'Italy'
        elif name == '中国':
            name = 'China'
        elif name == '丹麦':
            name = 'Denmark'
        elif name == '美国':
            name = 'United States'
        elif name == '日本':
            name = 'Japan'
        elif name == '瑞典':
            name = 'Sweden'
        elif name == '比利时':
            name = 'Belgium'
        elif name == '德国':
            name = 'Germany'
        elif name == '加拿大':
            name = 'Canada'
        elif name == '芬兰':
            name = 'Finland'
        elif name == '苏联':
            name = 'Russia'
        elif name == '希腊':
            name = 'Greece'
        elif name == '阿拉伯':
            name = 'Saudi Arabia'
        elif name == '挪威':
            name = 'Norway'
        data_dict["name"] = name
        data_dict["value"] = x[1]
        data_list.append(data_dict)
        data_dict = {}
    close_conn(conn, cursor)
    return data_list


def get_top100_country_2():
    data_list = []
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select country,count(country) from top100_country group by country"
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        data_dict["name"] = x[0]
        data_dict["value"] = x[1]
        data_list.append(data_dict)
        data_dict = {}
    close_conn(conn, cursor)
    return data_list


# 获取12年级推荐书目频率前35的国家
def get_12_country():
    data_list = []
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select country,count(country) from 12_country group by country"
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        data_dict["name"] = x[0]
        data_dict["value"] = x[1]
        data_list.append(data_dict)
        data_dict = {}
    close_conn(conn, cursor)
    return data_list


# 获取34年级推荐书目频率前35的国家
def get_34_country():
    data_list = []
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select country,count(country) from 34_country group by country"
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        data_dict["name"] = x[0]
        data_dict["value"] = x[1]
        data_list.append(data_dict)
        data_dict = {}
    close_conn(conn, cursor)
    return data_list


# 获取56年级推荐书目频率前35的国家
def get_56_country():
    data_list = []
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select country,count(country) from 56_country group by country"
    cursor.execute(sql)
    res = cursor.fetchall()
    for x in res:
        data_dict["name"] = x[0]
        data_dict["value"] = x[1]
        data_list.append(data_dict)
        data_dict = {}
    close_conn(conn, cursor)
    return data_list


if __name__ == '__main__':
    country_list = []
    country_12 = get_top100_country_2()
    country_12 = sorted(country_12, key=operator.itemgetter('value'))
    for x in country_12:
        country_list.append(x['name'])
    print(country_list)
    print(country_12)

