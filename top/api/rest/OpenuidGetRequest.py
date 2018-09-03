'''
Created by auto_sdk on 2018.01.03
'''
from ..base import RestApi


class OpenuidGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'taobao.openuid.get'
