from flask import Flask, render_template
from utils import *

app = Flask(__name__)


@app.route('/low_grade')
def low_grade():
    book_list, num_list = get_low_data()
    country_list = []
    country_12 = get_12_country()
    country_12 = sorted(country_12, key=operator.itemgetter('value'))
    for x in country_12:
        country_list.append(x['name'])
    return render_template('low_grade.html', book_list=book_list, num_list=num_list, country_12=country_12,
                           country_list=country_list)


@app.route('/mid_grade')
def mid_grade():
    book_list, num_list = get_mid_data()
    country_list = []
    country_34 = get_34_country()
    country_34 = sorted(country_34, key=operator.itemgetter('value'))
    for x in country_34:
        country_list.append(x['name'])
    return render_template('mid_grade.html', book_list=book_list, num_list=num_list, country_34=country_34,
                           country_list=country_list)


@app.route('/high_grade')
def high_grade():
    book_list, num_list = get_high_data()
    country_list = []
    country_56 = get_56_country()
    country_56 = sorted(country_56, key=operator.itemgetter('value'))
    for x in country_56:
        country_list.append(x['name'])
    return render_template('high_grade.html', book_list=book_list, num_list=num_list, country_56=country_56,
                           country_list=country_list)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/')
def index():
    country_list = []
    # 世界地图
    top100 = get_top100_country()
    # 推荐频率次数、推荐频率（折线图）
    num1, num2 = get_freq_data()
    # 前20 书名、推荐频率（条形图）
    book, num3 = get_all_data()
    # 推荐书目国家统计（饼图）
    country_top100 = get_top100_country_2()
    country_top100 = sorted(country_top100, key=operator.itemgetter('value'))
    for x in country_top100:
        country_list.append(x['name'])
    num1.reverse()
    num2.reverse()
    return render_template('main.html', num1=num1, num2=num2, book=book, num3=num3, top100=top100,
                           country_list=country_list, country_top100=country_top100)


@app.route('/main')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
