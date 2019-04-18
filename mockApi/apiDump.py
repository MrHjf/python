#linux \033[显示方式;字体色;背景色m......[\033[0m]
#-------------------------------------------
#-------------------------------------------
#字体色     |       背景色     |      颜色描述
#-------------------------------------------
#30        |        40       |       黑色
#31        |        41       |       红色
#32        |        42       |       绿色
#33        |        43       |       黃色
#34        |        44       |       蓝色
#35        |        45       |       紫红色
#36        |        46       |       青蓝色
#37        |        47       |       白色
#-------------------------------------------
#-------------------------------
#显示方式     |      效果
#-------------------------------
#0           |     终端默认设置
#1           |     高亮显示
#4           |     使用下划线
#5           |     闪烁
#7           |     反白显示
#8           |     不可见
#-------------------------------
# windows import color.py
import json, datetime, sys
from urllib import request, parse
sys.path.append("..")
from color import printYellow, printRed, printGreen, printPink


def loadFont():
	f = open("api.json", encoding='utf-8')  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
	apis = json.loads(f)
	for api in apis:
		requestApi(api)

def requestApi(api):
	data = parse.urlencode(api['data'])
	req = request.Request(api['url'])
	try:
		begin = datetime.datetime.now()
		printYellow(u'%s 【start】\n' % (api['url']))
		printYellow(u'%s [params]\n' % (api['data']))
		response = request.urlopen(req, data=data.encode('utf-8'))
		result = response.read()
		end = datetime.datetime.now()
		logger(result, api['url'], end - begin)
	except Exception as e:
		printRed(u'【error】: %s \n' % (e))

def logger(data, url, time):
	json_data = eval(data)
	if json_data['status'] == 'success':
		printGreen(u'%s 【success end】【耗时: %s】: \n %s \n' % (url, time, json.loads(data)))
	else:
		printPink(u'%s 【failed end】: \n %s \n' % (url, json.loads(data)))

loadFont()