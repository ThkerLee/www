import tornado.ioloop
import tornado.web
import os.path
from tornado.options import define,options
from tornado.concurrent import Future
define("port",default=8888,help="run on the given port",type=int)
define("debug",default=True,help="run in debug mode")
class mainhandler(tornado.web.RequestHandler):
	def get(self):
		self.render("index.html")


def main():
	app=tornado.web.Application(
		[
		(r"/",mainhandler),

		],
		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__),"static"),
		debug=options.debug,

		)
	app.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
if __name__ =="__main__":
	main()