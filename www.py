
#coding=utf-8

import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define,options

define("port",default=8888,help="run on the given port",type=int)
define("debug",default=True,help="run in debug mode")
class mainhandler(tornado.web.RequestHandler):

	def get(self):
		 self.render("index.html")
		# self.render("index-model.html")
class top_nav(tornado.web.RequestHandler):

	def get(self):
		self.render("top-nav.html")

class left_nav(tornado.web.RequestHandler):

	def get(self):
		leftmenu={u'我的工作台':(u'待审核单据',u'我的单据',u'已审核单据'),u'的工作台':(u'待审核单据',u'我的单据',u'已审核单据'),}
		self.render('left-nav.html',menus=leftmenu)
class right_nav(tornado.web.RequestHandler):

	def get(self):
		self.render("right-nav.html")
class right_mini_nav(tornado.web.RequestHandler):

	def get(self):
		self.render("right-mini-nav.html")

class right_content(tornado.web.RequestHandler):

	def get(self):
		self.render("right-conent.html")



def main():
	app=tornado.web.Application(
		[
		(r"/",mainhandler),
		(r"/templates/left-nav.html",left_nav),
		(r"/templates/right-nav.html",right_nav),
		(r"/templates/top-nav.html",top_nav),
		(r"/templates/right-content.html",right_content),
		(r"/templates/right-mini-nav.html",right_mini_nav),
		],

		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		debug=options.debug,

		)
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__ =="__main__":
	main()
