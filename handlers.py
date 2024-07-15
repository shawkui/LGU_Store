import os.path
import re
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.locks
import tornado.options
import tornado.web
import time
import random

'''
所有handler的母类
实现了获取当前用户名的功能
'''


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


# 登录模块, url={/,/login}
# 处理login和logout, 当url为/或者/login时调用login,当页面为/logout时调用logout
# login.html会提交一个表格到/seller/login 或者 /customer/login 来调用对应的post，进行登录
# DONE: 错误信息返回; 调用数据库进行密码验证；
# TODO: 新建账户功能，管理员功能
class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html', customer_warning='', seller_warning='')

    def post(self):
        pass

class newcustomerHandler(BaseHandler):
    def get(self):
        self.render('new_user.html', user='customer',customer_warning='')
        pass
    def post(self):
        n_name=self.get_argument('n_name')
        n_pass=self.get_argument('n_pass')
        n_sex=self.get_argument('n_sex')
        n_age=self.get_argument('n_age')
        print(n_age,n_name,n_sex,n_pass)
        # 防止重复user name
        query='select * from buyer where buyer_name="%s"'%(n_name)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result=cursor.fetchall()
        if result:
            self.write(r"<script> alert('Cannot Create Account! User Name Exists!');  window.location.href = '/customer/newaccount';</script> ")
            return
        
        # buyer_id 不是自增的
        query = "insert into buyer(buyer_name, buyer_password, buyer_age, buyer_sex, balance)\
        values ('%s',md5('%s'),'%s','%s',0);"%(n_name, n_pass,n_age,n_sex)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            try:
                # 执行SQL语句
                cursor.execute(query)
                # 提交到数据库执行
                db.commit()
                print('Save')
                self.redirect('/')
            except:
                # 发生错误时回滚
                db.rollback()
                print('Roll back')
                self.write(r"<script> alert('Cannot Create Account!');  window.location.href = '/customer/newaccount';</script> ")
                return
        

class newsellerHandler(BaseHandler):
    def get(self):
        self.render('new_user.html', user='seller',customer_warning='')
        pass
    def post(self):
        n_name=self.get_argument('n_name')
        n_pass=self.get_argument('n_pass')
        n_add=self.get_argument('n_add')
        print(n_add,n_name,n_pass)
        # 防止重复user name
        query='select * from seller where seller_name="%s"'%(n_name)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result=cursor.fetchall()
        if result:
            self.write(r"<script> alert('Cannot Create Account! User Name Exists!');  window.location.href = '/seller/newaccount';</script> ")
            return
        query = "insert into seller(seller_name, seller_password, balance, num_of_fan, place_of_dispatch, mark)\
        values ('%s',md5('%s'),'0','0','%s','0');"%(n_name, n_pass,n_add)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            try:
                # 执行SQL语句
                cursor.execute(query)
                # 提交到数据库执行
                db.commit()
                print('Save')
                self.redirect('/')
            except:
                # 发生错误时回滚
                db.rollback()
                print('Roll back')
                self.write(r"<script> alert('Cannot Create Account!');  window.location.href = '/seller/newaccount';</script> ")
                return
class LogoutHandler(BaseHandler):
    def get(self):
        print('logout')
        if (1):
            self.clear_cookie("username")
            self.redirect(r"/")


class SellerLoginHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        input_name = self.get_argument("username")
        input_passw = self.get_argument('password')
        print('Set Customer')
        print(input_name, input_passw)
        if input_name == '':
            self.render(
                'login.html', customer_warning='', seller_warning='User Name Needed!')
            return
        elif input_passw == '':
            self.render(
                'login.html', customer_warning='', seller_warning='Password Needed!')
        else:
            # 查询input_name 的password的SQL命令
            # Fecthall=双层tuple, 第一层是不同行，第二层是不同列
            # 如果是无效输入，返回None
            query = 'select * from seller where seller_name ="%s" and seller_password=md5("%s");' % (
                input_name, input_passw)
            db = self.application.db
            # 查询密码
            with db.cursor() as cursor:
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            if result:
                self.set_secure_cookie(
                    "username", self.get_argument("username"))
                self.redirect(r"/seller/center/item")
            else:
                self.render(
                    'login.html', customer_warning='', seller_warning='Worng name or password! Please try again!')


class CusLoginHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        input_name = self.get_argument("username")
        input_passw = self.get_argument('password')
        print('Set Customer')
        print(input_name, input_passw)
        if input_name == '':
            self.render(
                'login.html', customer_warning='User Name Needed!', seller_warning='')
            return
        elif input_passw == '':
            self.render(
                'login.html', customer_warning='Password Needed!', seller_warning='')
        else:
            # 查询input_name 的password的SQL命令
            # Fecthall=双层tuple, 第一层是不同行，第二层是不同列
            # 如果是无效输入，返回()
            query = 'select buyer_password from buyer where buyer_name ="%s" and buyer_password=md5("%s");' % (
                input_name, input_passw)
            db = self.application.db
            # 查询密码
            with db.cursor() as cursor:
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
            if result:
                self.set_secure_cookie(
                    "username", self.get_argument("username"))
                self.redirect(r"/customer/home")
            else:
                self.render(
                    'login.html', customer_warning='Worng name or password! Please try again!', seller_warning='')


'''
Seller的handlers
'''

# 根据/seller/center/(w+)中的匹配到的内容进行页面渲染
# item->店铺商品信息 TODO: 添加和修改商品
# orderhistory->订单记录 TODO: 订单详细信息
# store_info->店铺信息 TODO: 不知道应该显示什么


class SellCenHandler(BaseHandler):
    def get_id(self):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        query = 'select seller_id from seller where seller_name="%s"' % (user)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        return result[0][0]

    def get(self, input):
        print(input)
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        print(type(user))
        if input == 'item':
            query = "select product_id, product_name, product_price, inventory \
                from product \
                    where seller_id=%s;" % (self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            item_list = result

            self.render("seller_center.html", user=user, item_list=item_list)
        elif input == 'orderhistory':
            # 订单的查询是个问题，因为一个订单包含多个商品，考虑加入商品详情页面
            query = "select order_number, receiver_name, receiver_phone, receiver_address, total_price, create_date\
                    from order_information join receiver_information \
                    where order_information.seller_id=%s and \
                    order_information.receiver_information_id=receiver_information.receiver_information_id;"%(self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            order_list = result
            self.render("seller_order.html", user=user,order_list=order_list, order_detail_list=())
        elif input == 'storeinfo':
            query="select seller_name, place_of_dispatch , seller_password from seller where seller_id='%s';"%(self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            item = result[0]
            self.render("seller_store.html", user=user,item=item)
        elif input=='statistic':
            # 获取总收入
            query="select sum(total_price) from order_information where seller_id='%s';"%(self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            total_income=result[0][0]
            
            # 获取当前balance
            query="select balance from seller where seller_id='%s';"%(self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            balance=result[0][0]

            # 获取总销量
            query="select sum(sales) from  product \
            where seller_id=%s;"%(self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            toatl_sales=result[0][0]
            # 获取销量前十名

            query = "select product_id, product_name, product_price, sales, inventory \
                from product \
                    where seller_id=%s order by sales desc;" % (self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchmany(10)
            print(result)
            item_list = result

            self.render('seller_sta.html',user=user,balance=balance, total_income=total_income,item_list=item_list, toatl_sales=toatl_sales)
            pass
        else:
            self.write('Wrong URL!')
        pass

    def post(self, input):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        all_para = str(input).split('_')
        print(all_para)

        # 修改地址 TODO: 返回错误信息
        if all_para[0] == 'item':
            if all_para[1]=='save':
                new_amt=self.get_argument('amt')

                query = 'update product set inventory="%s"\
                    where product_id="%s";' % (new_amt, all_para[2])
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        self.write('Bad new Amount! Please check it.')
                        print('Roll back')
                        return
                self.redirect('/seller/center/item')
            elif all_para[1]=='new':
                new_name=self.get_argument('p_name')
                new_rul=self.get_argument('p_image')
                new_price=self.get_argument('p_price')
                new_invent=self.get_argument('p_invent')
                new_des=self.get_argument('p_des')
                new_cat=self.get_argument('p_cat')
                print(new_cat)


                query = "insert into product(seller_id,product_name,product_image_url,product_describe,category_id,product_price,inventory,sales,mark)\
                values ('%s','%s','%s','%s','%s',%s, '%s', '%s', '%s');"%(self.get_id(), new_name, new_rul,new_des,new_cat,new_price, new_invent, '0', '5')
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        print('Roll back')
                        self.write('Cannot Save it! Please check it.')
                        return
                self.redirect('/seller/center/item')

            elif all_para[1]=='update':
                new_name=self.get_argument('p_name')
                new_rul=self.get_argument('p_image')
                new_price=self.get_argument('p_price')
                new_invent=self.get_argument('p_invent')
                new_des=self.get_argument('p_des')
                new_cat=self.get_argument('p_cat')
                print(new_cat)

                # 删除当前货物的情况， 货物id为all_para[2]
                query = "update product  set seller_id='%s' ,product_name='%s', product_image_url='%s', product_describe='%s',\
                    category_id='%s', product_price=%s, inventory='%s' \
                        where product_id='%s';"%(self.get_id(), new_name, new_rul,new_des,new_cat,new_price, new_invent, all_para[2])
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        print('Roll back')
                        self.write('Cannot Save it! Please check it.')
                        return
                self.redirect('/seller/center/item')


            elif all_para[1]=='del':
                query = "delete from product where product_id='%s'"%(all_para[2])
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        self.write('Bad new Amount! Please check it.')
                        print('Roll back')
                        return
                self.redirect('/seller/center/item')
            else:
                self.write('Wrong URL')
        elif all_para[0] == 'storeinfo':
            if all_para[1]=='save':
                new_name=self.get_argument('s_name')
                new_add=self.get_argument('s_address')
                new_pass=self.get_argument('s_pass')

                query = 'update seller set seller_name="%s", place_of_dispatch="%s", seller_password="%s"\
                    where seller_id="%s";' % (new_name, new_add, new_pass, self.get_id())
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        self.write('Bad new info! Please check it.')
                        print('Roll back')
                        return
                    self.redirect('/')

class sellerItemHandler(BaseHandler):
    def get(self, input):
        # 在渲染页面的时候直接把item的id编码进url里，类似于/item/id这种格式，方便进入详情页面
        # 数据库里获取商品详细信息， 输出到页面里
        #
        item_id = input
        query = "SELECT *\
                FROM product join seller\
                WHERE seller.seller_id = product.seller_id and product_id='%s';" % (item_id)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        if len(result) == 0:
            self.write('Wrong URL')
        else:
            item = result[0]
            self.render('edit_item_detail.html', item=item,
                        user=self.get_current_user(),oper='update')

    def post(self):
        pass
class sellerNewHandler(SellCenHandler):
    def get(self):
        item = ('','','','','','','','','','','','','','','','','','','','')
        self.render('edit_item_detail.html', item=item,
                    user=self.get_current_user(),oper='new')

        pass
    def post(self):
        pass

class sellerOrderDetailHandler(SellCenHandler):

    def get(self, input):
        user = self.get_current_user()
        print(input)
        query = "select order_number, receiver_name, receiver_phone, receiver_address, total_price, create_date\
                from order_information join receiver_information \
                where order_number='%s' and \
                order_information.receiver_information_id=receiver_information.receiver_information_id;"%(input)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        order_list = result

        # Item: item_id, name, price, store_id, store_name
        query = "select product.product_id, product_name, product_price, product_number \
                from order_information_detail join product\
                 where order_number='%s' and product.product_id=order_information_detail.product_id;" % (input)
        db = self.application.db
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        order_detail_list = result
        self.render("seller_order.html", user=user, order_list=order_list, order_detail_list=order_detail_list)
        pass

'''
customer的handlers
'''

# Homepage渲染，提供了商品的搜索，展示和分类


class CusHomeHandler(BaseHandler):
    def get(self):
        user = self.get_current_user()
        print(type(user))
        # Item: item_id, name, price, store_id, store_name
        query = "SELECT product_id, product_name, product_price, seller.seller_id, seller_name, product_image_url \
                FROM product join seller\
                WHERE seller.seller_id = product.seller_id\
                ORDER by product.sales desc;"
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)

        item_list = result
        self.render("customer_home.html", user=user,
                    Showbox_title="Today's Hot", item_list=item_list)
        pass

# 商品分类展示


class ClassifyHandler(BaseHandler):
    def get(self, input):
        user = self.get_current_user()
        print(type(user))
        print(input)
        if input == 'clothing':
            ca_id = 2
            title = 'Clothing'
        elif input == 'fooddrinks':
            ca_id = 3
            title = 'Food & Drinks'
        elif input == 'books':
            ca_id = 4
            title = 'Books'
        elif input == 'homeappliance':
            ca_id = 5
            title = 'Home Appliance'
        elif input == 'electronics':
            ca_id = 6
            title = 'Electronics'
        elif input == 'beautyhealth':
            ca_id = 7
            title = 'Beauty & Health'
        else:
            self.write('Wrong URL')
            return
        query = 'SELECT product_id, product_name, product_price, seller.seller_id, seller_name, product_image_url\
             FROM product join category join seller\
            WHERE product.category_id = category.category_id AND seller.seller_id=product.seller_id AND category.category_id="%s" \
                ORDER BY product.mark desc;' % (ca_id)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)

        item_list = result
        self.render("customer_home.html", user=user,
                    Showbox_title='Category ' + title, item_list=item_list)


# address->地址簿 DONE: 修改，删除和新建
# customer_order->历史订单 DONE: 订单详情和商品详情
# shopping_chart->购物车 TODO: 购物车的修改和删除，以及下单功能，库存检查功能，余额检查功能还有，订单添加功能
# 检查非法输入，所有非法get和post都会转向Wrong Url
class CusCenHandler(BaseHandler):
    def get_balance(self):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        query = 'select balance from buyer where buyer_name="%s"' % (user)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        return float(result[0][0])

    def get_id(self):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        query = 'select buyer_id from buyer where buyer_name="%s"' % (user)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        return result[0][0]

    def get(self, input):
        user = self.get_current_user()
        print(type(user))
        user = str(user, encoding="utf-8")
        if input == 'address':
            # 展示地址
            query = 'select receiver_information_id, receiver_name, receiver_phone, receiver_address \
                     from receiver_information join buyer \
                     where buyer.buyer_id=receiver_information.buyer_id and buyer.buyer_name="%s";' % (user)
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            add_list = result
            self.render('customer_address.html', user=user,
                        balance=self.get_balance(), add_list=add_list)

        elif input == 'orderhistory':
            # 订单的查询是个问题，因为一个订单包含多个商品，考虑加入商品详情页面
            query = "select order_number, receiver_name, receiver_phone, receiver_address, total_price, create_date  \
                    from order_information join receiver_information join buyer \
                    where order_information.receiver_information_id=receiver_information.receiver_information_id and \
                    buyer.buyer_id=receiver_information.buyer_id and buyer.buyer_name='%s'\
                        order by order_information.create_date desc;" % (user)
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            order_list = result
            self.render("customer_order.html", user=user, balance=self.get_balance(
            ), order_list=order_list, order_detail_list=())

        elif input == 'shoppingcart':
            # 获取购物车详情
            # Item: item_id, name, price, order_name
            print(self.get_id())
            query = "select product.product_id, product_name, product_price, product_number \
                from shopping_cart join product \
                    where product.product_id=shopping_cart.product_id and buyer_id='%s' \
                        order by shopping_cart.create_date desc;" % (self.get_id())
            print(query)
            db = self.application.db
            with db.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            print(result)
            item_list = result

            self.render("customer_shopcart.html", user=user,
                        balance=self.get_balance(), item_list=item_list)
        else:
            self.write('Wrong URL!')
        pass

    def post(self, input):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        all_para = str(input).split('_')
        print(all_para)

        # 修改地址 TODO: 返回错误信息
        if all_para[0] == 'address':
            # 展示地址
            new_add = self.get_argument('r_add')
            new_phone = self.get_argument('r_phone')
            new_name = self.get_argument('r_name')
            if all_para[1] == 'save':
                query = 'update receiver_information set receiver_name="%s", receiver_phone="%s", receiver_address="%s"\
                    where receiver_information_id="%s";' % (new_name, new_phone, new_add, all_para[2])
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        self.write('Bad new address! Please check it.')
                        print('Roll back')
                        return
                    self.redirect('/customer/center/address')

            elif all_para[1] == 'del':
                query = 'delete from receiver_information where receiver_information_id="%s";' % (
                    all_para[2])
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        print('Roll back')
                        self.write('Cannot Delete it! Please check it.')
                        return
                    self.redirect('/customer/center/address')
            elif all_para[1] == 'new':
                query = "insert into receiver_information(buyer_id, receiver_name,receiver_phone,receiver_address) \
                    values ('%s','%s','%s','%s');" % (self.get_id(), new_name, new_phone, new_add)
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        print('Roll back')
                        self.write('Bad new address! Please check it.')
                        return
                    self.redirect('/customer/center/address')
            else:
                self.write('Wrong URL')

        # 修改购物车
        elif all_para[0] == 'shoppingcart':
            new_amt = self.get_argument('amt')
            if all_para[1] == 'save':
                query = 'update shopping_cart set product_number="%s"\
                    where product_id="%s" and buyer_id="%s";' % (new_amt, all_para[2], self.get_id())
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        self.write('Bad new Amount! Please check it.')
                        print('Roll back')
                        return
                    self.redirect('/customer/center/shoppingcart')
            elif all_para[1] == 'del':
                # 删除当前货物的情况， 货物id为all_para[2]
                query = 'delete from shopping_cart where product_id="%s" and buyer_id="%s";' % (
                    all_para[2], self.get_id())
                print(query)
                db = self.application.db
                with db.cursor() as cursor:
                    try:
                        # 执行SQL语句
                        cursor.execute(query)
                        # 提交到数据库执行
                        db.commit()
                        print('Save')
                    except:
                        # 发生错误时回滚
                        db.rollback()
                        print('Roll back')
                        self.write('Cannot Delete it! Please check it.')
                        return
                    self.redirect('/customer/center/shoppingcart')
            else:
                self.write('Wrong URL')
        else:
            self.write('Wrong URL!')
        pass
# 订单详情页面

class orderDetailHandler(BaseHandler):
    def get_balance(self):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        query = 'select balance from buyer where buyer_name="%s"' % (user)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        return result[0][0]

    def get(self, input):
        user = self.get_current_user()
        print(type(user))
        print(input)
        query = "select order_number, receiver_name, receiver_phone, receiver_address, total_price, create_date  \
                from order_information join receiver_information join buyer \
                where order_information.receiver_information_id=receiver_information.receiver_information_id and \
                buyer.buyer_id=receiver_information.buyer_id and order_number='%s';" % (input)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        order_list = result

        # Item: item_id, name, price, store_id, store_name
        query = "select product.product_id, product_name, product_price, product_number \
                from order_information_detail join product\
                 where order_number='%s' and product.product_id=order_information_detail.product_id;" % (input)
        db = self.application.db
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        order_detail_list = result
        self.render("customer_order.html", user=user, balance=self.get_balance(
        ), order_list=order_list, order_detail_list=order_detail_list)
        pass

# 搜索功能


class searchHandler(BaseHandler):
    def get(self):
        pass

    def post(self):
        # TODO: 检查空白输入，加上图片
        item_name = self.get_argument("item_name")
        print('begin search')
        # 数据库查询
        # 输出查询结果
        # Item: item_id, name, price, store_id, store_name
        # -- 模糊搜索...结果按评分降序排列
        if item_name == '':
            self.render('customer_home.html', user=self.get_current_user(),
                        Showbox_title='Seach Keyword is Needed', item_list=[])
        query = "SELECT product_id, product_name, product_price, seller.seller_id, seller_name, product_image_url \
                FROM product join seller\
                WHERE seller.seller_id = product.seller_id and product_name LIKE '%%%s%%' \
                ORDER by product.mark desc;" % (item_name)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)

        item_list = result

        # 将查询结果输出到页面上，跟主页面类似，但传入参数不同，可以分为title和商品两类
        # 空结果result=[], 会显示为没有图片
        self.render('customer_home.html', user=self.get_current_user(),
                    Showbox_title='Search Result of '+item_name, item_list=item_list)

# 商品详情


class itemHandler(CusCenHandler):
    def get(self, input):
        # 在渲染页面的时候直接把item的id编码进url里，类似于/item/id这种格式，方便进入详情页面
        # 数据库里获取商品详细信息， 输出到页面里
        #
        item_id = input
        query = "SELECT *\
                FROM product join seller\
                WHERE seller.seller_id = product.seller_id and product_id=%s;" % (item_id)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        if len(result) == 0:
            self.write('Wrong URL')
        else:
            item = result[0]
            self.render('item_detail.html', item=item,
                        user=self.get_current_user())

    def post(self,input):
        item_id=self.get_argument('i_id')
        query = "insert into shopping_cart (buyer_id, product_id,product_number) \
            values ('%s','%s','%s');" % (self.get_id(), item_id, '1')
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            try:
                # 执行SQL语句
                cursor.execute(query)
                # 提交到数据库执行
                db.commit()
                print('Save')
            except:
                # 发生错误时回滚
                db.rollback()
                print('Roll back')
                self.write(r"<script> alert('Item is in cart!');  window.location.href = '/customer/center/shoppingcart';</script> ")
                return
            self.redirect('/customer/center/shoppingcart')


# 店铺商品展示


class storeHandler(BaseHandler):
    # 在URL里编码店铺id，搜索数据库来显示
    def get(self, input):
        user = self.get_current_user()
        print(type(user))
        # Item: item_id, name, price, store_id, store_name
        query = "SELECT product_id, product_name, product_price, seller.seller_id, seller_name, product_image_url \
                FROM product join seller\
                WHERE seller.seller_id = product.seller_id and product.seller_id=%s\
                ORDER by product.mark desc;" % (input)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        if result:

            item_list = result
            self.render("customer_home.html", user=user,
                        Showbox_title=result[0][4], item_list=item_list)
        else:
            self.write('Wrong URL')
            return

    def post(self):
        pass

# 下单功能
class checkoutHandler(CusCenHandler):
    def get(self):
        user = self.get_current_user()
        user = str(user, encoding="utf-8")
        print(self.get_id())
        # 获取购物车中所有商品信息
        query = "select product.product_id, product_name, product_price, product_number ,product_price* product_number, inventory, inventory-product_number\
            from shopping_cart join product \
                where product.product_id=shopping_cart.product_id and buyer_id=%s;" % (self.get_id())
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        item_list = result

        # 获取总花费和剩余金额
        query = "select sum(product_price* product_number)\
            from shopping_cart join product \
                where product.product_id=shopping_cart.product_id and buyer_id=%s;" % (self.get_id())
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        total_cost=result[0][0]
        balance=float(self.get_balance())
        res_balance=round(balance-float(total_cost),2)

        # 获取地址
        query = 'select receiver_information_id, receiver_name, receiver_phone, receiver_address \
            from receiver_information join buyer \
            where buyer.buyer_id=receiver_information.buyer_id and buyer.buyer_name="%s";' % (user)
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        add_list = result
        if add_list:

            self.render("checkout.html", user=user,
                        balance=self.get_balance(), item_list=item_list, total_cost=total_cost, res_balance=res_balance, add_list=add_list)
        else:
            self.write(r"<script> alert('Address is needed!');  window.location.href = '/customer/center/shoppingcart';</script> ")
            return
        pass

    def post(self):
        pass

class placeorderHandler(CusCenHandler):
    def get(self):
        pass

    def post(self):
        # 获取购物车详情
        # Item: item_id, name, price, order_name
        # 检查库存
        query=" select product_name\
                from shopping_cart join product \
                where product.product_id=shopping_cart.product_id and buyer_id='%s' and product_number >=inventory;" %(self.get_id())
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        if result:
            self.write("<script> alert('Inventory not enough!');  window.location.href = '/customer/center/shoppingcart';</script> ")
            return
        
        # 检查余额
        query = "select sum(product_price* product_number)\
            from shopping_cart join product \
                where product.product_id=shopping_cart.product_id and buyer_id=%s;" % (self.get_id())
        print(query)
        db = self.application.db
        with db.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
        print(result)
        total_cost=result[0][0]
        balance=float(self.get_balance())
        res_balance=round(balance-float(total_cost),2)
        print(res_balance<0)
        if res_balance<0:
            self.write(r"<script> alert('Balance not enough!');  window.location.href = '/customer/center/shoppingcart';</script> ")
            return
        
        # 获取地址
        r_add=self.get_argument('o_add')


        # 提交订单
        print('-------------------------------------------------------------------------------------------')
        with db.cursor() as cursor:
            try:
                #获取订单seller_id
                query="select  seller_id from shopping_cart join product \
                        where shopping_cart.product_id=product.product_id and buyer_id='%s'\
                        group by seller_id;"%(self.get_id())
                cursor.execute(query)
                print(query)
                seller_list = cursor.fetchall()
                print(seller_list)
                # 获取订单号
                query="select order_number from order_information order by order_number desc;"
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
                print(result)
                if result:
                    o_id=int(result[0][0])
                else: 
                    o_id=0
                # 拆分订单
                for seller in seller_list:
                    o_id+=1
                    print(o_id)
                    # 获取订单总金额
                    query=" select  sum(product.product_price*product_number) from shopping_cart join product \
                            where shopping_cart.product_id=product.product_id and buyer_id='%s' and seller_id='%s';"%(self.get_id(), seller[0])
                    cursor.execute(query)
                    result = cursor.fetchall()
                    print(result,'------------------------')
                    total_cost=float(result[0][0])
                    print(total_cost)

                    # 获取商家balance
                    query="select balance from seller where seller_id='%s'"%(seller[0])
                    print(query)
                    cursor.execute(query)
                    result=cursor.fetchall()
                    print(result)
                    s_balance=float(result[0][0])
                    new_s_balance=s_balance+total_cost

                    # 更新商家balance
                    query="update seller set balance=%s where seller_id='%s';"%(str(new_s_balance), seller[0])
                    print(query)
                    cursor.execute(query)

                    
                    # 插入订单信息
                    query=" insert into order_information( seller_id, receiver_information_id, total_price) \
                        values ('%s','%s',%s);"%(seller[0],r_add, str(total_cost))
                    print(query)
                    cursor.execute(query)

                    # 插入订单详情
                    # 筛选商品
                    query=" select  product.product_id, product_number from shopping_cart join product \
                            where shopping_cart.product_id= product.product_id and buyer_id='%s' and seller_id='%s';"%(self.get_id(), seller[0])
                    print(query)
                    cursor.execute(query)
                    result = cursor.fetchall()
                    print(result)
                    item_list=result
                    for item in item_list:
                        # 更新商品销量
                        query=" select sales, inventory from product where product_id='%s'"%(item[0])
                        print(query)
                        cursor.execute(query)
                        result=cursor.fetchall()
                        # 获取当前销量 库存
                        i_sale=int(result[0][0])
                        i_invent=int(result[0][1])
                        # 获取新销量库存
                        new_sale=i_sale+int(item[1])
                        new_invent=i_invent-int(item[1])
                        # 更新
                        query="update product set sales=%s, inventory=%s where product_id='%s';"%(str(new_sale),str(new_invent), item[0])
                        cursor.execute(query)

                        
                        # 插入当前商品的信息
                        query=" insert into order_information_detail(order_number, product_id, product_number) \
                            values ('%s','%s','%s');"%(o_id, item[0], item[1])
                        print(query)
                        cursor.execute(query)
                        # 从购物车中删除当前商品
                        query = 'delete from shopping_cart where product_id="%s" and buyer_id=%s;' % (
                            item[0], self.get_id())
                        print(query)
                        cursor.execute(query)
                        print(result)
                # 金额修改
                query="update buyer set balance=%s where buyer_id='%s';"%(str(res_balance), self.get_id())
                cursor.execute(query)
                db.commit()
                self.redirect('/customer/center/orderhistory')
            except:
                db.rollback()
                self.write(r"<script> alert('Cannot Place order!');  window.location.href = '/customer/center/shoppingcart';</script> ")
                return
        

        pass
