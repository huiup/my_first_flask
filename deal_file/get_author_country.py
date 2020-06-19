# coding:utf-8
from utils import *
# 获取书目国家信息，存入数据库

grade_12 = "[['小猪唏哩呼噜', '中国'],['安徒生童话', '丹麦'],['猜猜我有多爱你', '中国'],['爷爷一定有办法', '加拿大'],['了不起的狐狸爸爸', '英国'],['大个子老鼠小个子猫', '中国'],['三毛流浪记', '中国'],['格林童话', '德国'],['没头脑和不高兴', '中国'],['丁丁历险记', '比利时'],['逃家小兔', '美国'],['洋葱头历险记', '意大利'],['我和小姐姐克拉拉', '德国'],['爱心树', '美国'],['小布头奇遇记', '中国'],['木偶奇遇记', '意大利'],['不一样的卡梅拉', '法国'],['一年级大个子二年级小个子', '日本'],['小老虎历险记', '中国'],['神奇校车', '美国'],['弟子规', '中国'],['三字经', '中国'],['亲爱的笨笨猪', '中国'],['舒克和贝塔历险记', '中国'],['伊索寓言', '希腊'],['豆蔻镇的居民和强盗', '挪威'],['一粒种子的旅行', '德国'],['犟龟', '德国'],['调皮的日子', '中国'],['兔子坡', '美国'],['红鞋子', '中国'],['泡泡儿去旅行', '中国'],['中华歌谣100首', '中国'],['我爸爸', '英国'],['我妈妈', '英国']]"
grade_34 = "[['时代广场的蟋蟀', '美国'],['长袜子皮皮', '瑞典'],['爱的教育', '意大利'],['夏洛的网', '美国'],['木偶奇遇记', '意大利'],['皮皮鲁传', '中国'],['亲爱的汉修先生', '美国'],['魔法师的帽子', '芬兰'],['乌丢丢的奇遇', '中国'],['海底两万里', '法国'],['窗边的小豆豆', '日本'],['大林和小林', '中国'],['昆虫记', '法国'],['宝葫芦的秘密', '中国'],['天方夜谭', '阿拉伯'],['蓝鲸的眼睛', '中国'],['西游记', '中国'],['高士其科普童话', '中国'],['吹牛大王历险记', '德国'],['草房子', '中国'],['列那狐的故事', '法国'],['当世界年纪还小的时候', '德国'],['格列佛游记', '法国'],['草原上的小木屋', '美国'],['小兵张嘎', '中国'],['绿野仙踪', '美国'],['苹果树上的外婆', '奥地利'],['装在口袋里的爸爸', '中国'],['鲁西西传', '中国'],['水孩子', '英国'],['成语故事', '中国'],['讲给孩子的中国地理', '中国'],['寄小读者', '中国'],['淘气包埃米尔', '瑞典'],['十万个为什么', '中国']]"
grade_56 = "[['小王子', '法国'],['假如给我三天光明', '美国'],['城南旧事', '中国'],['草房子', '中国'],['青铜葵花', '中国'],['昆虫记', '法国'],['三国演义', '中国'],['女儿的故事', '中国'],['汤姆·索亚历险记', '美国'],['童年', '苏联'],['水浒传', '中国'],['上下五千年', '中国'],['男生贾里', '中国'],['永远讲不完的故事', '德国'],['西游记', '中国'],['呼兰河传', '中国'],['我的妈妈是精灵', '中国'],['王子与贫儿', '美国'],['骑鹅旅行记', '瑞典'],['寄小读者', '中国'],['狼王梦', '中国'],['鲁滨逊漂流记', '英国'],['女生贾梅', '中国'],['我要做好孩子', '中国'],['第三军团', '中国'],['格列佛游记', '英国'],['老人与海', '美国'],['绿山墙的安妮', '加拿大'],['乌丢丢的奇遇', '中国'],['窗边的小豆豆', '日本'],['蓝色的海豚岛', '美国'],['爱的教育', '意大利'],['金银岛', '英国'],['女生日记', '中国'],['好兵帅克', '捷克']]"


def insert_12_country(*args):
    conn, cursor = get_conn()
    sql = "insert into 12_country (`book`,`country`) values(%s,%s);"
    cursor.execute(sql, args)
    conn.commit()
    close_conn(conn, cursor)
    # print('12插入数据成功')

def insert_34_country(*args):
    conn, cursor = get_conn()
    sql = "insert into 34_country (`book`,`country`) values(%s,%s);"
    cursor.execute(sql, args)
    conn.commit()
    close_conn(conn, cursor)
    # print('34插入数据成功')

def insert_56_country(*args):
    conn, cursor = get_conn()
    sql = "insert into 56_country (`book`,`country`) values(%s,%s);"
    cursor.execute(sql, args)
    conn.commit()
    close_conn(conn, cursor)
    # print('56插入数据成功')


if __name__ == '__main__':
    # a = eval(grade_12)
    # b = eval(grade_34)
    # c = eval(grade_56)
    # for x in a:
    #     insert_12_country(x[0], x[1])
    # for x in b:
    #     print(x[0], x[1])
    #     insert_34_country(x[0], x[1])
    # for x in c:
    #     insert_56_country(x[0], x[1])