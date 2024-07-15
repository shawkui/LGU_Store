# LGU Store

This is a simple online shopping platform designed for the final project of CSC 3170.

In this project, some basic online shopping functions are implemented and a MySQL database is employed to maintain the transactions.

* Set up

  First of all, you need to install the MySQL database in your computer and run the `taobao1.sql` to create the schema.

  Then, to run the project, you will need to have python >=3.6. Install the required packages: 

  ```python
  pip install -r requirements.txt
  ```

  Change the following configuration in the main.py.

  ```python
  define("port", default=8888, help="run on the given port", type=int)
  define("dbaddress", default="localhost", help="connect to database in given address", type=str)
  define("database", default="taobao1", help="connect to given database", type=str)
  define("username", default="root", help="log in database with given user name", type=str)
  define("password", default="password", help="log in database with given password", type=str)
  ```

  Then, run the project:

  ```python
  python main.py
  ```

  After all the above procedures, you can open [localhost:8888](localhost:8888) in your browser to open the website (the "8888" should be changed to the port you selected in main.py)

  

* Platform Guide

  * Customer:

    * As a customer, the following identities are created by default. You can find their information in the following table. Besides, you can create your own identity on the login page.

      |  ID  |   Name   | Password |
      | :--: | :------: | :------: |
      |  1   | 大猪蹄子 |  123456  |
      |  2   | 小猪佩奇 |  123789  |
      |  3   |  乔奶奶  |  987321  |
      |  4   |  德云社  |  654321  |
      |  5   |  卢本伟  |  192837  |
      |  6   |  五五开  |  918273  |
      |  7   |   G胖    |  110119  |
      |  8   |   PDD    |  119120  |
      |  9   |  凡先生  |  911211  |

    *  The following functions are implemented for customers:

      * Search specific product by name.

      * Browse Products by Category, Store or Sales.

      * Find the detailed information of products.

      * Find account balance for purchase.

      * Add products to Shopping Cart.

      * Check out and place order.

      * Create and edit receiver information.

      * Find order histories.

      * Raise warning and Roll Back when illegal operations are performed.

        

  * Seller: 

    * As a seller, the following identities are created by default. You can find their information in the following table. Besides, you can create your own identity on the login page.

      |  ID  |      Name      | Password |
      | :--: | :------------: | :------: |
      |  1   |  螺霸王旗舰店  |  12345   |
      |  2   |   耐克旗舰店   |  12345   |
      |  3   |   宝洁旗舰店   |  12345   |
      |  4   |   苹果旗舰店   |  12345   |
      |  5   |   文轩旗舰店   |  12345   |
      |  6   |   百事旗舰店   |  12345   |
      |  7   |   雪碧旗舰店   |  12345   |
      |  8   | 可口可乐旗舰店 |  12345   |
      |  9   |   魅可旗舰店   |  12345   |
      |  10  | 海蓝之谜旗舰店 |  12345   |
      |  11  |  徐老师零食铺  |  12345   |
      |  12  |   美的旗舰店   |  12345   |

    * The following functions are implemented for sellers:

      * Find all products in the seller's store.

      * Edit the detailed information of products.

      * Create or delete products.

      * Find all orders and detailed order information for the seller's store.

      * Edit the name, address and password of the store. 

        ( Note that due to the md5 encryption function in our platform, a seller should encrypt his new password first and paste the encrypted password to the password editing box. )

      * Find the balance of the seller and the top 10 best selling products.

      * Raise warning and Roll Back when illegal operations are performed.


 

