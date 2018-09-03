# -*- coding: utf-8 -*-
'''
Created on 2012-7-3

@author: lihao
'''
import top.api
import json

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了

'''
top.setDefaultAppInfo("12061046", "8b0aeb0da683f8ca8a9c602ecd35d0d4")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)

使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")

使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()

'''
req = top.api.TbkItemGetRequest()
req.fields = "title,nick,price"
req.q = "女装"

try:
	resp= req.getResponse()
	print(json.dumps(resp, indent=4))
except Exception as e:
	raise e
