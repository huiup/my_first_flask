# coding:utf-8
from utils import get_conn, close_conn
# 将数据库中的各学段书目数据保存txt文件


def get_books_data():
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


if __name__ == '__main__':
    f1 = open('./data2/12年级书目.txt', 'w', encoding='utf-8')
    f2 = open('./data2/34年级书目.txt', 'w', encoding='utf-8')
    f3 = open('./data2/56年级书目.txt', 'w', encoding='utf-8')
    f4 = open('./data2/全年级书目.txt', 'w', encoding='utf-8')
    data_list = get_books_data()
    for data in data_list:
        low = data['low'].strip('[]')
        mid = data['mid'].strip('[]')
        high = data['high'].strip('[]')
        f1.write(low + '\n\n')
        f2.write(mid + '\n\n')
        f3.write(high + '\n\n')
        # print(data['url'])
        f4.write(low + '\n' + mid + '\n' + high + '\n\n')
        # break
    f1.close()
    f2.close()
    f3.close()
    f4.close()
