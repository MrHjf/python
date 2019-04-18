#!/usr/bin/env python
#coding:utf-8

####################
#公司访问外网认证脚本
###################

from urllib import request, parse
import getpass

#name = raw_input('请输入用户名：')
name = 'root' # 在本行输入您的名字
url = 'http://172.29.2.124:4430/api/frontEnd/yyfaxapm/user.action?fn=login'

def auth():
	page = 0
	parameters = {'password':'e10adc3949ba59abbe56e057f20f883e','secret':'true','username':name} 
	#提交的数据参数
	data = parse.urlencode(parameters)  #对参数进行编码
	req = request.Request(url) #形成url请求
	try:
		#response = request.urlopen(req) #发送请求
		response = request.urlopen(req, data=data.encode('utf-8')) #发送请求
		page = response.read() #读取返回的页面
		print(page);
	except Exception as e:
		print(e);
		print('登录失败，请重新登录!') #修复HTTPError错误
	if page:
		if "认证成功" in page or "该IP已登录" in page:
			print('恭喜您，登录成功，您现在可以访问外网了！')
		else:
			print('账号或密码错误，请重新登录！')

if __name__ == '__main__':
	print("####################################")
	print("#访问外网认证脚本              #")
	print("####################################")
	print('用户名：%s' %name)
	#passwd = int(getpass.getpass('请输入密码：'))
	auth()