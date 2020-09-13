#  版本一：url+字典拼合法查找

# 用到了很古老的一个东西————PhantomJS 因为页面加载时电费是JS动态加载，这个办法是动态加载页面后获取了相关的数据
# selenium版本3.8   
# 增加了一项功能————模糊音处理问题，解决了因打错字而导致的查询失败


from selenium import webdriver
import os
from xpinyin import Pinyin

area_py = Pinyin() 
url = 'http://www.houqinbao.com/hydropower/index.php?rebind=1&m=PayWeChat&c=Index&a=bingding&token=&openid=oUiRowXbORPJT9eWljFST1-UzoWg&schoolcode=13579&payopenid='
area_dic = {
            "杏一":"13579_173_288_948", "杏二":"13579_173_288_949", "杏三":"13579_173_288_950", 
            "竹一":"13579_173_289_951", "竹二":"13579_173_289_952", "竹三":"13579_173_289_953", "竹四":"13579_173_289_954", 
            "松一":"13579_173_290_955", "松二":"13579_173_290_956", "松三":"13579_173_290_957", "松四":"13579_173_290_958", 
            "桃一":"13579_173_291_959", "桃二":"13579_173_291_960", "桃三":"13579_173_291_961", "桃四":"13579_173_291_962", "桃五":"13579_173_291_963",
            "研一":"13579_173_293_967", "研二":"13579_173_293_968", "研三":"13579_173_293_969"
            }
fuzzy_pro = {
# 杏苑
    "xyi":"杏一","xingyuanyihaolou":"杏一","xingyilou":"杏一","xingyuanyilou":"杏一","xing1lou":"杏一","xing1":"杏一",
    "xer":"杏二","xingyuanerhaolou":"杏二","xingerlou":"杏二","xingyuanerlou":"杏二","xing2lou":"杏二","xing2":"杏二",
    "xsan":"杏三","xingyuansanhaolou":"杏三","xingsanlou":"杏三","xingyuansanlou":"杏三","xing3lou":"杏三","xing3":"杏三",
# 竹苑
    "zyi":"竹一","zhuyuanyihaolou":"竹一","zhuyilou":"竹一","zhuyuanyilou":"竹一","zhu1lou":"竹一","zhu1":"竹一",
    "zer":"竹二","zhuyuanerhaolou":"竹二","zhuerlou":"竹二","zhuyuanerlou":"竹二","zhu2lou":"竹二","zhu2":"竹二",
    "zsan":"竹三","zhuyuansanhaolou":"竹三","zhusanlou":"竹三","zhuyuansanlou":"竹三","zhu3lou":"竹三","zhu3":"竹三",
    "zsi":"竹四","zhuyuansihaolou":"竹四","zhusilou":"竹四","zhuyuansilou":"竹四","zhu4lou":"竹四","zhu4":"竹四",
# 松苑
    "syi":"松一","songyuanyihaolou":"松一","songyilou":"松一","songyuanyilou":"松一","song1lou":"松一","song1":"松一",
    "ser":"松二","songyuanerhaolou":"松二","songerlou":"松二","songyuanerlou":"松二","song2lou":"松二","song2":"松二",
    "ssan":"松三","songyuansanhaolou":"松三","songsanlou":"松三","songyuansanlou":"松三","song3lou":"松三","song3":"松三",
    "ssi":"松四","songyuansihaolou":"松四","songsilou":"松四","songyuansilou":"松四","song4lou":"松四","song4":"松四",
# 桃苑
    "tyi":"桃一","taoyuanyihaolou":"桃一","taoyilou":"桃一","taoyuanyilou":"桃一","tao1lou":"桃一","tao1":"桃一",
    "ter":"桃二","taoyuanerhaolou":"桃二","taoerlou":"桃二","taoyuanerlou":"桃二","tao2lou":"桃二","tao2":"桃二",
    "tsan":"桃三","taoyuansanhaolou":"桃三","taosanlou":"桃三","taoyuansanlou":"桃三","tao3lou":"桃三","tao3":"桃三",
    "tsi":"桃四","taoyuansihaolou":"桃四","taosilou":"桃四","taoyuansilou":"桃四","tao4lou":"桃四","tao4":"桃四",
    "twu":"桃五","taoyuanwuhaolou":"桃五","taowulou":"桃五","taoyuanwulou":"桃五","tao5lou":"桃五","tao5":"桃五",
# 研究生苑
    "yyi":"研一","yanjiushengyihaolou":"研一","yanyilou":"研一","yanjiushengyilou":"研一","yan1lou":"研一","yan1":"研一",
    "yer":"研二","yanjiushengerhaolou":"研二","yanerlou":"研二","yanjiushengerlou":"研二","yan2lou":"研二","yan2":"研二",
    "ysan":"研三","yanjiushengsanhaolou":"研三","yansanlou":"研三","yanjiushengsanlou":"研三","yan3lou":"研三","yan3":"研三",
}
def fuzzy_pro():
    return 0

def url_add( areaid , roomid ):
    try:
        if areaid not in area_dic:
            areaid = fuzzy_pro[area_py.get_pinyin(areaid, '')]
        id_list = area_dic[areaid].split('_')
    except:
        print("输入房间不存在，请求错误!")
        return False
    return "http://www.houqinbao.com/hydropower/index.php?m=PayWeChat&c=Index&a=before&payopenid=&openid=oUiRowXbORPJT9eWljFST1-UzoWg&schoolcode={}&campusid={}&areaid={}&flatid={}&roomname={}".format(id_list[0] , id_list[0]+"_"+id_list[1] , id_list[0]+"_"+id_list[1]+"_"+id_list[2] , id_list[0]+"_"+id_list[1]+"_"+id_list[2]+"_"+id_list[3] , roomid)  
# print(url_add("桃四楼","B3102"))

def ele_ask(nameid , roomid):  # 查询
    try:
        try:
            driver = webdriver.PhantomJS(executable_path=r'phantomjs.exe')
        except:
            print("缺少关键文件PhantomJS")
        driver.get(url_add(nameid , roomid.upper()))
        ele_pay = driver.find_element_by_class_name("dushu").text
        print(ele_pay)
        driver.quit()
    except:
        print("发生异常,不是你网断了就是垃圾端口又崩了...")

def input_id(text):  #获取信息
    return input(text)

def try_move():   #删除已有的日志
    try:
        os.remove("ghostdriver.log")
    except:
        pass

if __name__ == "__main__":
    try_move()
    name = input_id("寝室楼:")
    room = input_id("房间号:")
    ele_ask(name , room) #....测试数据....
    input("按回车结束...")
    try_move()

# 其他的版本想起来就搞一搞，搞完弄到"Gay Hub"上去