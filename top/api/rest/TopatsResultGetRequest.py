'''
Created by auto_sdk on 2016.10.12
'''
from ..base import RestApi


class TopatsResultGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.task_id = None

	def getapiname(self):
		return 'taobao.topats.result.get'
