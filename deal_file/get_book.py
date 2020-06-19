from lxml import etree
import requests

# 获取搜狐的推荐书目网页内容
url = 'https://www.sohu.com/a/330675336_369891'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
text = requests.get(url = url,headers=headers).text
# print(text)
tree = etree.HTML(text)
title = tree.xpath('//title/text()')[0]
book_text = tree.xpath('//*[@id="mp-editor"]/p[position() > 11 and position() < 143]//text()')
print(url)
print(title)
print(book_text)
save_path = './data/' + title + '.txt'
# with open(save_path, 'w', encoding='utf-8') as f:
#     f.write(url+'\n')
#     for line in book_text:
#         f.write(line+'\n')