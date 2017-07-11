#coding=utf-8
from django.db import models
from tinymce.models import HTMLField #导入副文本

# Create your models here.
#商品分类表
class TypeInfo(models.Model):
    ttitle =models.CharField(max_length=20)  #分类标题
    isdelete = models.BooleanField(default=False) #删除标志

    class Meta:
        db_table = 'typeinfo'#定义表名
    #商品分类默认选择ttitle
    def __str__(self):
        return self.ttitle.encode('utf-8')

#商品信息表
class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20) #商品名称
    gpic = models.ImageField(upload_to='goods/') #商品图片
    gprice = models.DecimalField(max_digits=5,decimal_places=2) #商品价格，保留两位小数
    gclick = models.IntegerField()# 商品点击量
    gunit = models.CharField(max_length=10) #单位
    isdelete = models.BooleanField(default=False)#是否删除
    gsubtitle = models.CharField(max_length=200)# 商品简介
    gkucun = models.ImageField(default=100)#商品库存
    gcontent = HTMLField() #副文本:商品详细信息
    gtype = models.ForeignKey('TypeInfo')#与商品分类表的连接

    class Meta:
        db_table = 'goodsinfo' #定义表名