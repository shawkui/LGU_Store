
import os.path
import re
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web
import pymysql
from handlers import *
import platform
# windows 系统下, python 3.8版本时， tornado 需要使用 SelectorEventLoop
'''
if platform.system() == "Windows":
    import asyncio

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
'''

from tornado.options import define, options

# Change this part according to your settings
define("port", default=8888, help="run on the given port", type=int)
define("dbaddress", default="localhost",
       help="connect to database in given address", type=str)
define("database", default="taobao1",
       help="connect to given database", type=str)
define("username", default="root",
       help="log in database with given user name", type=str)
define("password", default="shaokui239",
       help="log in database with given password", type=str)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            blog_title=u"LGU Store",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            login_url=r"/auth/login",
            debug=True,
        )
        handlers = [
            (r"/", LoginHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler),

            (r"/seller/login", SellerLoginHandler),
            (r'/seller/center/(\w+)', SellCenHandler),
            (r'/seller/center/orderdetail/(\w+)', sellerOrderDetailHandler),
            (r'/seller/item/(\w+)', sellerItemHandler),
            (r'/seller/new', sellerNewHandler),

            (r"/customer/login", CusLoginHandler),
            (r'/customer/home', CusHomeHandler),
            (r"/customer/placeorder", placeorderHandler),
            (r'/customer/checkout', checkoutHandler),
            (r'/customer/home/(\w+)', ClassifyHandler),
            (r'/customer/center/(\w+)', CusCenHandler),
            (r'/customer/center/orderdetail/(\w+)', orderDetailHandler),

            (r"/item/(\w+)", itemHandler),

            (r"/store/(\w+)", storeHandler),

            (r'/search', searchHandler),

            (r'/order/(\w+)', orderDetailHandler),  # 备用订单网页

            (r"/customer/newaccount", newcustomerHandler),
            (r"/seller/newaccount", newsellerHandler),
        ]
        conn = pymysql.connect(options.dbaddress, options.username,
                               options.password, options.database, autocommit=1)
        self.db = conn
        print(conn)
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()

    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
