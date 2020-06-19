# coding:utf-8
import wordcloud
from wordcloud import ImageColorGenerator
import imageio
from utils import get_conn, close_conn


def get_all_data():
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select book,num from book_freq limit 100"
    count = cursor.execute(sql)
    res = cursor.fetchall()
    for out in res:
        data_dict[out[0]] = out[1]
    close_conn(conn, cursor)
    return data_dict


def get_low_data():
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select book,num from 12_book_freq limit 60"
    count = cursor.execute(sql)
    res = cursor.fetchall()
    for out in res:
        data_dict[out[0]] = out[1]
    close_conn(conn, cursor)
    return data_dict


def get_mid_data():
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select book,num from 34_book_freq limit 60"
    count = cursor.execute(sql)
    res = cursor.fetchall()
    for out in res:
        data_dict[out[0]] = out[1]
    close_conn(conn, cursor)
    return data_dict


def get_high_data():
    data_dict = {}
    conn, cursor = get_conn()
    sql = "select book,num from 56_book_freq limit 60"
    count = cursor.execute(sql)
    res = cursor.fetchall()
    for out in res:
        data_dict[out[0]] = out[1]
    close_conn(conn, cursor)
    return data_dict


def make_wc(data=None,img_path=None,save_name=None):
    mk = imageio.imread(img_path)
    image_colors = ImageColorGenerator(mk)
    word_cloud = wordcloud.WordCloud(width=500, height=400,
                                     background_color='white', font_path='simsun.ttc',
                                     mask=mk,max_font_size=30)
    # word_cloud.generate_from_frequencies(data_list)
    word_cloud.fit_words(data)
    # word_cloud.recolor(color_func=image_colors)
    word_cloud.to_file(save_name)


if __name__ == '__main__':
    img_path = 'image'
    # 全部阶段书目的词云
    all_data = get_all_data()
    make_wc(all_data,img_path+r'\chinamap.png','all.png')
    # 低阶段书目的词云
    low_data = get_low_data()
    make_wc(low_data,img_path+r'\gezi.jpeg','low.png')
    # 中阶段书目的词云
    mid_data = get_mid_data()
    make_wc(mid_data,img_path+r'\tree.jpg','mid.png')
    # 高阶段书目的词云
    high_data = get_high_data()
    make_wc(high_data,img_path+r'\manshape2.png','high.png')