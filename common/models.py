"""
myadmin的数据模型
"""
from django.db import models
from datetime import datetime

# Create your models here.
class Member(models.Model):
    """
    会员信息表
    """
    # 会员的真实姓名
    user_name = models.CharField(max_length=32)

    # 会员的昵称
    nick_name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    # 收货地址
    address = models.CharField(max_length=255)
    # 邮编
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    add_time = models.DateTimeField(default=datetime.now)

    def toDict(self):
        """
        将对象都转换成字典
        """
        return {
            'id': self.id, 'username': self.user_name,
            'name': self.nick_name, 'password': self.password,
            'address': self.address, 'phone': self.phone,
            'email': self.email, 'state': self.state, 'sex': self.sex
        }

    def __str__(self):
        return self.user_name

    class Meta(object):
        db_table = 'member'


class Category(models.Model):
    """
    商品类别
    """
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "type"  # 更改表名


class Goods(models.Model):
    """
    商品信息
    """
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    content = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    state = models.IntegerField(default=1)
    addtime = models.DateTimeField(default=datetime.now)

    def toDict(self):
        return {'id': self.id, 'typeid': self.typeid,
                'goods': self.goods, 'company': self.company,
                'price': self.price, 'picname': self.picname,
                'store': self.store, 'num': self.num,
                'clicknum': self.clicknum, 'state': self.state
        }

    class Meta:
        db_table = "goods"  # 更改表名

# 订单模型
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    addtime = models.DateTimeField(default=datetime.now)
    total = models.FloatField()
    state = models.IntegerField()

    class Meta:
        db_table = "orders"  # 更改表名

#订单详情模型
class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()

    class Meta:
        db_table = "detail"  # 更改表名

class RobotKiller(models.Model):
    """
    过滤爬虫，请求次数过多则封IP
    """
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=16)    #IP地址
    visits = models.IntegerField()          #请求次数
    time = models.DateTimeField()           #第一次发起请求的时间
    class Meta:
        db_table = 'robotkiller'
