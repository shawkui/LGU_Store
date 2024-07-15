-- 模糊搜索...结果按评分降序排列
SELECT 
    *
FROM
    product
WHERE
    product_name LIKE '%螺狮粉%'
order by mark desc;
-- 查找某个特定种类的商品，并按评分降序排列
select * from product;
SELECT 
    *
FROM
    product,
    category
WHERE
    product.category_id = category.category_id
        AND category.category_id = 2
ORDER BY mark desc;
select * from product where product_id = 1;
-- 添加购物车
insert into shopping_cart(buyer_id, product_id,product_number) values (1,7,3);
update shopping_cart set product_number = 5 where buyer_id = 1  and product_id= 2;
-- 生成订单
insert into order_information(seller_id, receiver_information_id) values (1,3);
insert into order_information_detail values(4,1,5);
insert into order_information_detail values(4,3,2);
-- 返回用户详细信息
select buyer_name,buyer_sex,buyer_age,balance from buyer where buyer_id = 1;
-- 修改用户信息
update buyer set buyer_name = '卢姥爷' where buyer_id = 1;
update buyer set buyer_sex = 'man' where buyer_id = 1;
update buyer set buyer_age = 72 where buyer_id = 1;
update buyer set buyer_password = md5('卢姥爷') where buyer_id = 1;
-- 按创建时间排序购物车内容：
SELECT 
    s.seller_name, p.product_name, sc.product_number
FROM
    shopping_cart sc,
    product p,
    seller s
WHERE
    sc.product_id = p.product_id
        AND p.seller_id = s.seller_id
        AND sc.buyer_id = 1
ORDER BY sc.create_date DESC;
-- 按创建时间排序订单内容：
SELECT 
    seller.seller_name,
    product.product_name,
    order_information_detail.product_number,
    order_information.create_date
FROM
    seller,
    product,
    order_information,
    order_information_detail
WHERE
    seller.seller_id = order_information.seller_id
        AND order_information.order_number = order_information_detail.order_number
        AND order_information_detail.product_id = product.product_id
        AND order_information.receiver_information_id IN (SELECT 
            receiver_information_id
        FROM
            receiver_information
        WHERE
            buyer_id = 1)
ORDER BY order_information.create_date DESC;
-- 返回地址信息：
SELECT 
    receiver_name, receiver_phone, receiver_address
FROM
    receiver_information
WHERE
    buyer_id = 1;
-- 添加地址信息：
insert into receiver_information(buyer_id, receiver_name,receiver_phone,receiver_address) values
(1,'大猪蹄子的弟弟','13983727635','滕王阁');
-- 修改地址信息：
UPDATE receiver_information 
SET 
    receiver_phone = '18629166281'
WHERE
    receiver_information_id = 2;
-- 删除地址信息:
DELETE FROM receiver_information 
WHERE
    receiver_information_id = 1;
-- 按照分类返回商家发布的商品：
SELECT 
    product.product_name, category.category_name
FROM
    product,
    category
WHERE
    category.category_id = product.category_id
        AND product.seller_id = 1;
-- 创建新的商品：
insert into product(seller_id,product_name,product_image_url,product_describe,category_id,product_price,inventory)
values (11,'牛肉面','https://gss0.baidu.com/7LsWdDW5_xN3otqbppnN2DJv.jpg','麻辣鲜香',3,19.90,291);
-- 修改商品信息：
update product set product_price = 29.9 where product_id = 2;
-- 删除商品：
delete from product where product_id = 1;
-- 统计销售额：
SELECT 
    SUM(product.product_price * order_information_detail.product_number)
FROM
    product,
    order_information_detail
WHERE
    product.product_id = order_information_detail.product_id
        AND order_information_detail.order_number IN (SELECT 
            order_number
        FROM
            order_information
        WHERE
            seller_id = 1);
-- 统计粉丝数：
select count(*) from add_favorite where seller_id = 1;

-- 输出产品id, name, price, 和对应的seller_id, seller_name
SELECT 
    product.product_id,
    product.product_name,
    product.product_price,
    seller.seller_id,
    seller.seller_name
FROM
    product,
    seller
WHERE
    seller.seller_id = product.seller_id;
    
-- 根据订单号返回订单里商品的购买数量
Select product_id, product_number from order_information_detail
where order_number = 2;