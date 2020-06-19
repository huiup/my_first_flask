# coding:utf-8
from collections import Counter
from nltk import FreqDist
from save_txt import get_books_data
from utils import *
import json
# 统计词频

# 利用nltk进行词频统计
def nltk_freq(word_list=None):
    word_freq_list = {}
    fdist = FreqDist(word_list)
    for key in fdist:
        word_freq_list[key] = fdist[key]
    stat = sorted(word_freq_list.items(), key=lambda x: x[1], reverse=True)
    # print(stat)
    return stat


# 用Counter进行词频统计
def counter_freq(word_list=None):
    word_freq_list = {}
    Words = Counter(word_list)

    for word, freq in Words.items():
        word_freq_list[word] = freq
    word_freq_list = sorted(word_freq_list.items(),
                            key=lambda x: x[1], reverse=True)
    # print(doc_list)
    return word_freq_list


# 自定义统计词频函数
def count_book(word_list=None):
    word_freq_list = {}
    for x in word_list:
        word_freq_list[x] = word_freq_list.get(x, 0) + 1
    word_freq_list = sorted(word_freq_list.items(),
                            key=lambda x: x[1], reverse=True)
    return word_freq_list


def save_json(filename, stat=None):
    freq_dict = {}
    with open('./data2/' + filename, 'w', encoding='utf-8') as f:
        for item in stat:
            freq_dict[item[0]] = item[1]
        # ensure_ascii=False 解决乱码
        f.write(json.dumps(freq_dict, ensure_ascii=False))
    print('保存' + filename + '.json成功！')


def save_csv(filename, stat=None):
    # encoding='utf_8_sig' 解决用Excel打开出现乱码的问题
    f = open('./data2/' + filename, 'w', encoding='utf_8_sig')
    for item in stat:
        f.write(item[0] + ',' + str(item[1]) + '\n')
    f.close()
    print('保存' + filename + '.csv成功！')


def insert_to_sql_all(*args):
    try:
        conn, cursor = get_conn_cloud()
        sql = "insert into book_freq (`book`,`num`) values(%s,%s);"
        cursor.execute(sql, args)
        conn.commit()
        close_conn_cloud(conn, cursor)
        print('添加成功', args[0])
    except Exception as e:
        print(e)


# 将某阶段的书频添加数据库
def insert_to_sql(table_name, *args):
    try:
        conn, cursor = get_conn()
        sql = "insert into " + table_name + " (`book`,`num`) values(%s,%s);"
        cursor.execute(sql, args)
        conn.commit()
        close_conn(conn, cursor)
        print('添加成功！')
    except Exception as e:
        print(e)


# 获取各阶段总书目
def get_all_book(data_list=None):
    all_book = ''
    for x in data_list:
        all_book = all_book + \
            x['low'].strip('[]') + x['mid'].strip('[]') + x['high'].strip('[]')
    # 进行简单处理，转为列表
    all_book_list = all_book.replace(' ', '').replace("'", '').split(',')
    return all_book_list


# 获取各阶段书目
def get_book(data_list=None):
    low_book = ''
    mid_book = ''
    high_book = ''
    for x in data_list:
        low_book = low_book + x['low'].strip('[]')
        mid_book = mid_book + x['mid'].strip('[]')
        high_book = high_book + x['high'].strip('[]')
    # 进行简单处理，转为列表
    low_book_list = low_book.replace(' ', '').replace("'", '').split(',')
    mid_book_list = mid_book.replace(' ', '').replace("'", '').split(',')
    high_book_list = high_book.replace(' ', '').replace("'", '').split(',')
    return low_book_list, mid_book_list, high_book_list


if __name__ == '__main__':
    # 获取库中的所数据
    data_list = get_books_data()
    # print(data_list)
    # 提取出总的书目
    all_book_list = get_all_book(data_list)
    # print(len(all_book_list))
    # 提取出各阶段的书目
    low_book_list, mid_book_list, high_book_list = get_book(data_list)

    # 获取书目频率
    # res = count_book(all_book_list)
    # res = nltk_freq(all_book_list)
    # res = counter_freq(all_book_list)
    res_low = counter_freq(low_book_list)
    res_mid = counter_freq(mid_book_list)
    res_high = counter_freq(high_book_list)

    # 计算平均推荐书目个数
    print(len(low_book_list))
    print(len(mid_book_list))
    print(len(high_book_list))

    print(len(low_book_list)/38)
    print(len(mid_book_list)/38)
    print(len(high_book_list)/38)

    # 数据保存为文件
    # save_csv('全部书目频率.csv',res)
    # save_json('全部书目频率.json',res)
    # save_csv('12年级书目频率.csv',res_low)
    # save_json('12年级书目频率.json',res_low)
    # save_csv('34年级书目频率.csv',res_mid)
    # save_json('34年级书目频率.json',res_mid)
    # save_csv('56年级书目频率.csv',res_high)
    # save_json('56年级书目频率.json',res_high)
    

    # 数据存入数据库
    # for x in res:
    #     # print(x)
    #     insert_to_sql_all(x[0], x[1])
    #
    # for x in res_low:
    #     insert_to_sql('12_book_freq',x[0],x[1])
    # for x in res_mid:
    #     insert_to_sql('34_book_freq',x[0],x[1])
    # for x in res_high:
    #     insert_to_sql('56_book_freq',x[0],x[1])
