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


# 连接云服务器数据库
def get_conn_cloud():
  """
  :return: 连接，游标
  """
  # 创建连接
  conn = pymysql.connect(host="112.126.79.62",
                         user="root",
                         password="huihuiyo",
                         db="books",
                         charset="utf8")
  # 创建游标
  cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
  return conn, cursor


# 关闭云服务器数据库
def close_conn_cloud(conn, cursor):
  cursor.close()
  conn.close()
