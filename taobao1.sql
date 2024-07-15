create schema taobao1;
use taobao1;
-- drop schema taobao1;
CREATE TABLE seller (
    PRIMARY KEY (seller_id, seller_name),
    seller_id INT NOT NULL AUTO_INCREMENT,
    seller_password VARCHAR(32) NOT NULL,
    seller_name VARCHAR(100) NOT NULL,
    balance decimal(9,2) DEFAULT 0,
    num_of_fan INT DEFAULT 0,
    place_of_dispatch TEXT NOT NULL,
    mark DECIMAL(2,1) DEFAULT NULL
);

insert into seller values 
(1,md5('12345'),'螺霸王旗舰店',0,5723124,'柳州',4.7),
(2,md5('12345'),'耐克旗舰店',0,123142,'天津',4.5),
(3,md5('12345'),'宝洁旗舰店',0,12354,'上海',4.9),
(4,md5('12345'),'苹果旗舰店',0,12543,'北京',5.0),
(5,md5('12345'),'文轩旗舰店',0,5324,'成都',4.6),
(6,md5('12345'),'百事旗舰店',0,54968,'大连',5.0),
(7,md5('12345'),'雪碧旗舰店',0,5932,'杭州',4.9),
(8,md5('12345'),'可口可乐旗舰店',0,123123,'太原',4.6),
(9,md5('12345'),'魅可旗舰店',0,34657,'北京',4.9),
(10,md5('12345'),'海蓝之谜旗舰店',0,96424,'太原',4.6),
(11,md5('12345'),'徐老师零食铺',0,15321,'太原',3.9),
(12,md5('12345'),'美的旗舰店',0,21942,'深圳',4.1);

create table product(
primary key(product_id),
product_id int not null auto_increment,
seller_id int not null,
product_name varchar(100) default null,
product_image_url varchar(255) default null,
product_describe text default null, 
category_id int default null,
product_price decimal(9,2) default null,
sales int default null,
inventory int default null,
mark decimal(2,1) default null
);

insert into product values
(1,1,'经典柳州螺狮粉','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588078061153&di=64e68143020bb5af2c359d78647fc684&imgtype=0&src=http%3A%2F%2Fimg1.lukou.com%2Fstatic%2Fp%2Fcommodity%2Fmedium%2F0009%2F99%2F58%2F13%2F9995813.jpg','经典的味道',3,19.90,981,23123,5.0),
(2,1,'小龙虾螺狮粉','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3756655875,3706946792&fm=15&gp=0.jpg','新口味',3,21.90,571,2134,4.9),
(3,1,'卤蛋螺狮粉','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3049427856,1910348900&fm=26&gp=0.jpg','全新口味',3,21.90,124,1234,4.9),
(4,2,'新款卫衣','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=422500072,2580080894&fm=11&gp=0.jpg','全新卫衣',2,299.90,312,5012,4.8),
(5,2,'潮流运动裤','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588247076139&di=d76ab8296d36ccee6e712304f01d3023&imgtype=0&src=http%3A%2F%2Fm.360buyimg.com%2Fn12%2Fjfs%2Ft2710%2F54%2F1291873801%2F139579%2Fa702e786%2F57398d83Na4ba6697.jpg%2521q70.jpg','新款裤子',2,299.90,123,141,4.7),
(6,3,'蓝月亮洗衣液','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3916931007,3763245017&fm=26&gp=0.jpg','强力清洗',5,59.90,435,40123,4.5),
(7,8,'樱桃味可乐','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588247862270&di=d9dea9122f252ed54037b13dd0049392&imgtype=0&src=http%3A%2F%2Fimg.mp.itc.cn%2Fupload%2F20170621%2Fdc42189f94df47bebc3b08166fa22125_th.jpg','感受樱桃汽水的魔力',3,3.90,1234,141,4.7),
(8,2,'短袖T恤','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588253689607&di=47be38d86dc50fe1819bd9afe1838622&imgtype=0&src=http%3A%2F%2Fimg07.huishangbao.com%2Ffile%2Fupload%2F201605%2F31%2F11%2F11-21-18-75-362324.jpg','潮流新品',2,159.90,546,1984,4.9),
(9,2,'宽松内搭长袖','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=280029638,1113278754&fm=26&gp=0.jpg','爆款新品',2,189.90,658,15467,4.5),
(10,2,'春季七分袖','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=408678526,2013571209&fm=15&gp=0.jpg','春季新款',2,159.90,15467,1213,4.7),
(11,2,'韩版中袖','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3681308520,2016748563&fm=26&gp=0.jpg','韩款新品',2,129.90,352123,1345,4.7),
(12,2,'条纹长袖','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=1445262912,2024822272&fm=11&gp=0.jpg','程序员战衣',2,129.90,523,135235,4.8),
(13,2,'纯棉假两件','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1384170871,3975216812&fm=15&gp=0.jpg','潮流假两件',2,159.90,32523,3255,4.7),
(14,2,'潮流夏季冰丝','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1576700466,648975881&fm=15&gp=0.jpg','潮流清爽',2,89.90,4121,401153223,4.6),
(15,2,'亚麻潮流半袖','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3092477156,863249532&fm=26&gp=0.jpg','亚麻潮流半袖',2,99.90,4135,48323,4.2),
(16,2,'港风工装痞帅衬衫','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2986431072,993306588&fm=11&gp=0.jpg','痞帅衬衫',2,159.90,43125,465123,3.9),
(17,2,'纯棉五分袖','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3448076962,2916494579&fm=26&gp=0.jpg','纯棉五分袖新款',2,59.90,4315,8523,3.5),
(18,6,'百事可乐联名凡士林润唇膏限量款','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2681269071,3980512504&fm=15&gp=0.jpg','凡士林联名可乐',3,89.90,64,123,3.2),
(19,6,'百事可乐无糖树莓口味','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2487583810,2126547363&fm=26&gp=0.jpg','无糖树莓口味',3,25.90,201,1233,2.9),
(20,6,'百事可乐老佛爷无糖碳酸饮料','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588257236927&di=c1b56e31426b5c36923d260442afb42d&imgtype=0&src=http%3A%2F%2F8080bl.com%2FPublic%2Fupload%2Fgoods%2F2019%2F11-02%2F5dbd407da752a.jpg','老佛爷无糖可乐',3,39.90,675,12123,4.9),
(21,6,'百事可乐鼠年限量金罐','https://img14.360buyimg.com/n0/jfs/t1/96841/39/6216/515208/5df33146E65ae0fa6/824cbc6c0373d6bf.jpg','百事可乐鼠年限量款',3,39.90,13,4323,2.5),
(22,7,'雪碧零卡碳酸饮料','https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1323555190,4175414808&fm=26&gp=0.jpg','零卡快乐水',3,59.80,814,52873,3.2),
(23,8,'可口可乐定制生日礼物世界杯','https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4246852502,945937162&fm=26&gp=0.jpg','定制生日礼物世界杯',3,19.90,244,4958,4.1),
(24,8,'可口可乐日本进口2020限量','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588258060213&di=68ac489876449c5f9b49c04100a0dbc7&imgtype=0&src=http%3A%2F%2Fimg1.tbcdn.cn%2Ftfscom%2Fi3%2F38801599%2FTB2cqPoyNxmpuFjSZFNXXXrRXXa_%2521%252138801599.jpg','可口可乐日本进口2020限量',3,39.90,318,95812,4.9),
(25,8,'可口可乐纤维+零卡无糖可乐','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=355646162,2761437271&fm=26&gp=0.jpg','纤维+零卡无糖可乐',3,60.00,251,391,3.7),
(26,8,'可口可乐联名菲诗小铺化妆品','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3505516886,3654504091&fm=26&gp=0.jpg','菲诗小铺化妆品联名可口可乐',3,89.90,64,123,3.2),
(27,8,'可口可乐Body Armor水果宾治味运动饮料','http://www.cpmin.cn/scripts/editor/attached/image/20180816/20180816133605_0376.jpg','可口可乐Body Armor水果宾治味运动饮料，新款',3,92.90,59,123,2.9),
(28,5,'冰与火之歌','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588403488272&di=90e7cbe1a379422eab84b29a87ec3d4d&imgtype=0&src=http%3A%2F%2Fimg1.cnforex.com%2Fnews%2F2018%2F09%2F05%2Fe65efe3d-55d3-42d1-9bb4-dd8c50b7eb43.jpg','权利的游戏原著',4,599.90,46,154,5.0),
(29,5,'边城','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588307661716&di=708fa7c3345f789af163730b335ceb29&imgtype=0&src=http%3A%2F%2Fi2.w.yun.hjfile.cn%2Fdoc%2F201303%2F8069f80a-5702-4231-960b-bb3453fc6266_02.jpg','沈从文作品',4,15.00,482,5313,3.1),
(30,5,'百年孤独','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588307713007&di=750b20ed2d0d355cfd6933b4a4b692cb&imgtype=0&src=http%3A%2F%2Fxs.cnnb.com.cn%2Fpic%2F0%2F10%2F06%2F36%2F10063656_816424.jpg','优秀作品',4,38.90,142,3216,3.8),
(31,5,'海底两万里','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1061618774,1541407919&fm=26&gp=0.jpg','奇幻的冒险',4,29.10,6911,10323,4.1),
(32,5,'龙族','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588308713490&di=a487e4c8c28c9826654ec4755c98f4b0&imgtype=0&src=http%3A%2F%2Fwww.sybooks.com.cn%2FUploadCover%2F2013%2F03%2F01%2F110436151.jpg','江南作品',4,55.00,48,27000,2.9),
(33,5,'天之炽','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=49505438,1782440827&fm=26&gp=0.jpg','江南作品',4,74.00,5,123,1.2),
(34,5,'淘气包马小跳','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1576960061,160748940&fm=26&gp=0.jpg','杨红樱作品',4,45.00,51,2423,3.5),
(35,5,'笑猫日记','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588308934912&di=25361520d892ce554d2f55a19deacb04&imgtype=0&src=http%3A%2F%2Fecx.images-amazon.com%2Fimages%2FI%2F51ej9yN0ikL._AA500_.jpg','杨红樱作品',4,50.00,200,2190,4.1),
(36,5,'蓝色翠鸟倒计时','https://img3.doubanio.com/view/subject/l/public/s26537763.jpg','青春文学',4,18.03,2,26,1.9),
(37,5,'百科全书','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588309147388&di=05c4c9a8d563690fc48d25417a235fbc&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D2393965199%2C96521790%26fm%3D214%26gp%3D0.jpg','百科全书',4,69.90,642,3941,3.9),
(38,5,'名人传','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588309286921&di=9e82b174fc97b676b33871c5377957cd&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20170905%2F7b7b269e0857427294884a9b506b6ef9.jpeg','名人传',4,11.90,572,2043,3.8),
(39,12,'美的电烤箱','https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1200310148,2744864593&fm=26&gp=0.jpg','38L大容量',5,299.00,21437,54123,4.5),
(40,12,'美的家用空调挂机','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588312643854&di=ab4b8b96c5e407fff3d9f32a0d34be22&imgtype=0&src=http%3A%2F%2Fimg1.imgtn.bdimg.com%2Fit%2Fu%3D3974739946%2C2916768975%26fm%3D214%26gp%3D0.jpg','一级能效',5,2599,12548,3985,4.2),
(41,12,'美的客厅立式柜机','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1430343754,1429329565&fm=26&gp=0.jpg','快速冷暖,强力制冷',5,2999,908,4912,3.4),
(42,12,'美的家用蒸汽电熨斗','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1195856225,3497250142&fm=26&gp=0.jpg','干湿两用，手柄控温',5,1099,145,1234,3.8),
(43,12,'美的空调扇制冷器','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588313259600&di=1395528e64d84d21f92aeb9374e80fbf&imgtype=0&src=http%3A%2F%2Fimage2.suning.cn%2Fuimg%2Fb2c%2Fnewcatentries%2F0070115165-000000000611676391_3_800x800.jpg','宽幅凉风，净化加湿',5,649,1970,2043,2.5),
(44,12,'美的小型电熨斗蒸汽手持式','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=3813047734,2639075125&fm=26&gp=0.jpg','轻小便携，一熨即平',5,199,460,3041,2.8),
(45,12,'美的洗碗机','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1775610810,1511029495&fm=26&gp=0.jpg','台式免安装',5,1049,316,8521,3.2),
(46,12,'美的洗衣机','https://gss0.baidu.com/7LsWdDW5_xN3otqbppnN2DJv/space/pic/item/c8ea15ce36d3d53954f353993587e950342ab09a.jpg','10kg大容量',5,2499,6570,84721,2.4),
(47,12,'美的大吸力扫地机器人','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588313674325&di=3875fa94f1acaed2ada94cc765590876&imgtype=0&src=http%3A%2F%2Fimgs.tom.com%2Fwhyz%2F201807%2FCONTENTB6D603EF38BF4EAD.jpg','智能扫地规划',5,899,527,2943,3.9),
(48,12,'美的吸尘器','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588313744750&di=84d2c5dcbaba1fbad07afe7bf8f0962f&imgtype=0&src=http%3A%2F%2Fopc-img.ehsy.com%2Fuploadfile%2Fopc%2Feditor%2Fimage%2F201711%2F20%2F1511169154191391.jpg','吸床/吸地两用',5,139,20182,8853,3.8),
(49,12,'美的小冰箱','https://gss0.baidu.com/7LsWdDW5_xN3otqbppnN2DJv/space/pic/item/6159252dd42a2834ef686a5154b5c9ea14cebf9a.jpg','三门三温',5,1289,4621,9481,2.5),
(50,12,'美的电热水壶','https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2542870134,541880116&fm=26&gp=0.jpg','智能温控',5,69,15234,29521,3.5),
(51,4,'iPhone SE','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1561407810,2435039251&fm=11&gp=0.jpg','包含一个耳机，usb连接线',6,3299,837,3812,4.9),
(52,4,'APPLE耳机 用于iPhone 6/7/8P','https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2499594610,3258602197&fm=26&gp=0.jpg','3.5mm接口',6,99,281,9481,2.5),
(53,4,'iPad 2018款','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588315736366&di=1191c4d148208f36860bdb4e9824a2fc&imgtype=0&src=http%3A%2F%2Fimg3.imgtn.bdimg.com%2Fit%2Fu%3D3669463098%2C1502486731%26fm%3D214%26gp%3D0.jpg','现货速发',6,2499,16,981,2.7),
(54,4,'苹果数据线1m','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316449777&di=ad82e7d8880180da467ab7b81fdc50a5&imgtype=0&src=http%3A%2F%2Fimg2.99114.com%2Fgroup1%2FM00%2F34%2F40%2FwKgGMFX7fuOAXb85AAGIi5qc2xg486.jpg','苹果原装数据线（1m）',6,65,43,941,2.2),
(55,4,'iPhone 11','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316574527&di=20234e178fe4243c78e960efbbc4cf70&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Ftranslate%2F439%2Fw712h527%2F20191026%2Fc12b-ihmipqw8011748.jpg','全网通4g',6,4299,139,281,2.7),
(56,4,'iPhone X','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316676356&di=b992490c9b3b6bbb18d29fca83ab5876&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D2271387814%2C124958664%26fm%3D214%26gp%3D0.jpg','7天无理由退换',6,1699,141,3721,2.5),
(57,4,'iPad Air3','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316778394&di=e7e7474b8ac6df3d46e51173790c81b2&imgtype=0&src=http%3A%2F%2Fcdimg.good.cc%2Fimages%2FUploadImage%2F0%2F399%2F399143.jpg','10.5英寸',6,4798,0,12,2.1),
(58,4,'MacBook Pro','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316844662&di=d68d284065e9f8044686ca359c9bfdd2&imgtype=0&src=http%3A%2F%2Fcdn.178hui.com%2Fupload%2F2018%2F0830%2F08283376748.jpg','顺丰包邮',6,4499,0,81,2.3),
(59,4,'苹果 11Pro','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588316995481&di=d4bdf50c3cfdf628441fdfc3256d1df5&imgtype=0&src=http%3A%2F%2F2f.zol-img.com.cn%2Fproduct%2F201_800x600%2F329%2FceDqNlxQIeAbY.jpg','3期免息',6,6199,11,41,1.2),
(60,4,'iPhone SE2','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588317076317&di=2c1817152cd544450b3cf3be46e26f7c&imgtype=0&src=http%3A%2F%2Fsy0.img.pcpop.com%2Fcopy%2F1553411974%2F1553411974951%2F1553411974951015.jpg%2521thumbnail','1200万像素',6,3299,653,981,2.1),
(61,4,'iPhone 8 Plus','https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3606788521,2597799848&fm=26&gp=0.jpg','原装未激活',6,1699,231,312,2.1),
(62,9,'MAC王者荣耀联名限定生姜高光修容盘','https://m.maccosmetics.com.cn/media/export/cms/products/640x600/mac_sku_SK1T19_640x600_0.jpg','生姜高光闪耀c位王者',7,240,2246,2913,4.9),
(63,9,'MAC尤雾弹唇膏','https://www.maccosmetics.com.cn/media/export/cms/products/280x320/mac_sku_S4K038_280x320_0.jpg','人间水蜜桃923',7,170,102031,20193,3.9),
(64,9,'MAC王者荣耀联名限定四色眼影盘','https://img.yzcdn.cn/upload_files/2020/04/21/FtmaLsnkmqbT82J4Z7Yhiynq8E1_.jpg?imageView2/2/w/580/h/580/q/75/format/jpg','4色晴彩MATCH王者人设',7,280,1693,2931,4.8),
(65,9,'MAC可定制无暇粉底液','https://www.maccosmetics.com.cn/media/export/cms/products/280x320/mac_sku_MYH201_280x320_0.jpg','明星同款GET无暇奶油肌',7,320,20193,1981,3.9),
(66,9,'MAC王者荣耀联名限定口红大牌正品','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588403044480&di=043a4e5db56eb6f8be87c3d23e219006&imgtype=0&src=http%3A%2F%2Fspider.ws.126.net%2F0923040c124caab71810837ede8bf5c7.jpeg','渐变外壳玩转王者唇色',7,170,20947,2013,4.9),
(67,9,'MAC持久防水眼线笔','https://www.maccosmetics.com.cn/media/export/cms/products/280x320/mac_sku_M3RY09_280x320_0.jpg','下单即享精美礼盒',7,165,105,3812,4.1),
(68,10,'LA MER海蓝之谜修护精萃液','https://www.lamer.com.cn/media/export/cms/products/680x680/LM_SKU_51KA01_47744_680x680_0.png','澎湃能量如水似精华',7,1100,8529,2391,5.0),
(69,10,'LA MER海蓝之谜精华面霜','https://www.lamer.com.cn/media/export/cms/products/680x680/LM_SKU_332002_26766_680x680_0.png','修护经典深澈滋润',7,2550,5029,2984,4.9),
(70,10,'LA MER海蓝之谜鎏光焕变气垫粉底液','https://www.lamer.com.cn/media/export/cms/products/680x680/LM_SKU_5NM701_85754_680x680_0.png','奢润无瑕鎏光此刻',7,1000,730,381,4.8),
(71,10,'LA MER海蓝之谜璀璨防晒隔离乳液','https://m.lamer.com.cn/media/export/cms/products/680x680/LM_SKU_5W7601_95484_680x680_0.png','轻盈清透璀璨夏日光芒',7,900,281,847,4.6),
(72,10,'LA MER海蓝之谜浓缩密集修护眼霜','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1588322111962&di=7abfdb3f9d659d409a6af65ecf62b015&imgtype=0&src=http%3A%2F%2Fwx4.sinaimg.cn%2Flarge%2F67f7411fly1gd50jn3dv8j20ly0cckbj.jpg','密集焕活眼见年轻',7,1700,4446,2938,4.8),
(73,10,'LA MER海蓝之谜鎏金焕颜精华液','https://www.lamer.com.cn/media/export/cms/products/680x680/LM_SKU_5LNT01_84260_680x680_0.png','赋活焕采',7,2200,266,2931,4.9);

select * from product;
alter table product add constraint FK_product_seller foreign key (seller_id)
references seller(seller_id) on delete cascade on update cascade;

create table category(
primary key(category_id),
category_id int not null auto_increment,
category_name varchar(100) default null,
parent_id int default null,
create_date datetime not null default current_timestamp,
constraint FK_category_parent foreign key (parent_id)
references category(category_id) on delete set null
);

insert into category(category_id,category_name,parent_id) values 
(1,'root',null),
(2,'Clothing',1),
(3,'Food&Drinks',1),
(4,'Books',1),
(5,'Home appliance',1),
(6,'Electronics',1),
(7,'Beauty&Health',1);

alter table product add constraint FK_product_category foreign key (category_id)
references category(category_id) on delete cascade on update cascade;

create table buyer(
primary key(buyer_id,buyer_name),
buyer_id int not null auto_increment,
buyer_password varchar(32) not null,
buyer_name varchar(100) not null,
buyer_sex enum('man','woman') default 'man',
buyer_age int default null,
balance decimal(9,2) default 0
);

insert into buyer values
(1,md5('123456'),'大猪蹄子','man',21,10000),
(2,md5('123789'),'小猪佩奇','woman',10,10000),
(3,md5('987321'),'乔奶奶','woman',65,10000),
(4,md5('654321'),'德云社','man',32,10000),
(5,md5('192837'),'卢本伟','man',35,10000),
(6,md5('918273'),'五五开','man',42,10000),
(7,md5('110119'),'G胖','man',45,10000),
(8,md5('119120'),'PDD','man',38,10000),
(9,md5('911211'),'凡先生','man',46,10000);

create table add_favorite(
primary key(seller_id,buyer_id),
seller_id int not null,
buyer_id int not null
);
alter table add_favorite add constraint FK_add_favorite_buyer foreign key (buyer_id)
references buyer(buyer_id) on delete cascade on update cascade;
alter table add_favorite add constraint FK_add_favorite_seller foreign key (seller_id) 
references seller(seller_id) on delete cascade on update cascade;

insert into add_favorite values (1,1),(1,2),(2,1),(2,3),(3,5),(3,9),(4,8),(4,1);
create table receiver_information(
primary key(receiver_information_id),
receiver_information_id int not null auto_increment,
buyer_id int not null,
receiver_name varchar(100) default null,
receiver_phone varchar(11) not null,
receiver_address text not null,
active_or_inactive enum('active','inactive') default 'active'
);

insert into receiver_information values
(1,1,'大猪蹄子','13203030394','LGU','active'),
(2,1,'大猪蹄子的爸爸','13980200304','LGU','active'),
(3,2,'小猪佩奇','12939293495','LGU','active'),
(4,3,'乔奶奶','12344672341','LGU','active');

alter table receiver_information add constraint FK_receiver_buyer foreign key (buyer_id)
references buyer(buyer_id) on delete cascade on update cascade;

create table order_information(
primary key(order_number),
order_number int not null auto_increment,
seller_id int not null,
receiver_information_id int not null,
create_date datetime default current_timestamp
);
alter table order_information add column total_price decimal(9,2) default 0;
insert into order_information(seller_id,receiver_information_id) values
(1,1);
insert into order_information(seller_id,receiver_information_id) values
(2,2),(3,2);
alter table order_information add constraint FK_order_seller foreign key (seller_id)
references seller(seller_id) on delete cascade on update cascade;
alter table order_information add constraint FK_order_receiver foreign key (receiver_information_id)
references receiver_information(receiver_information_id) on delete cascade on update cascade;

create table order_information_detail(
primary key(order_number,product_id),
order_number int not null,
product_id int not null,
product_number int default null
);
alter table order_information_detail add constraint FK_order_product foreign key (product_id)
references product(product_id) on delete cascade on update cascade;
alter table order_information_detail add constraint FK_order_detail foreign key (order_number)
references order_information(order_number) on delete cascade on update cascade;
insert into order_information_detail values 
(1,2,3),(1,3,2),(2,4,1),(3,6,1);

create table shopping_cart(
primary key(buyer_id,product_id),
buyer_id int not null,
product_id int not null,
product_number int default null,
create_date datetime default current_timestamp
);
alter table shopping_cart add constraint FK_cart_product foreign key (product_id)
references product(product_id) on delete cascade on update cascade;
alter table shopping_cart add constraint FK_cart_buyer foreign key (buyer_id)
references buyer(buyer_id) on delete cascade on update cascade;
insert into shopping_cart(buyer_id,product_id,product_number) values 
(2,6,3),
(1,4,2),
(1,2,5);



