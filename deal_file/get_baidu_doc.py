import requests
import re
import json
from url_list import *
import os

# 获取百度文库的doc文件
def get_document(main_url, save_path='data/'):
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    if main_url in url_list:
        print('该网页已经爬取过！')
        return
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    sess = requests.Session()
    html = sess.get(url=main_url, headers=headers).content.decode("gbk")
    # 抓取到文档标题
    title = re.search('id="doc-tittle-0">(.*?)</span>', html).group(1)
    # 若文件名重复但url不同，则修改标题
    txt_title = save_path + title + '.txt'
    if os.path.exists(txt_title):
        txt_title = txt_title[:-4] + '_1' + '.txt'
    # 使用正则提取 文档内容的url
    res = re.search("WkInfo.htmlUrls = '(.*)'", html).group(1)
    # \\x22是linux中的引号，替换成Python中的引号
    res = res.replace("\\x22", "\"")
    data = json.loads(res)
    f = open(txt_title, 'w', encoding='utf-8')
    f.write(main_url + '\n')
    string = ""
    for i in data["json"]:
        url = i["pageLoadUrl"]  # 获取到url
        url = url.replace("\\", "")  # url中有转义符\去掉

        # 请求文档内容
        data = requests.get(url).content.decode("utf-8")
        # 提取文本数据
        res = re.search("wenku_\d*\((.*)\)", data, re.S).group(1)
        # 将json对象数据转成Python对象
        data = json.loads(res)
        # pprint(data)
        for i in data['body']:
            # 判断数据是什么类型,word表示文本内容
            if i["t"] == "word":
                # 获取到文本
                string += str(i["c"])
                # ps中不为空并且_enter==1的时候是换行也就是一段内容
                if i["ps"] and i["ps"].get("_enter") == 1:
                    f.write(string + '\n')
                    string = ""
    f.close()
    print(main_url, '爬取完毕！')


if __name__ == '__main__':
    url = 'https://wenku.baidu.com/view/4b40abf4aff8941ea76e58fafab069dc50224702.html?fr=search'
    get_document(url)
