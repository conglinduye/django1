from django.db import models

# Create your models here.


class UserInfo(models.Model):

    uname = models.CharField(max_length=20)#用户名
    upwd = models.CharField(max_length=40)#密码加密后的位数是40位
    uemail = models.CharField(max_length=30)#邮箱
    userver = models.CharField(max_length=20,default='')#收件人姓名
    uphon = models.CharField(max_length=11,default='')#联系人手机号
    uaddress = models.CharField(max_length=40,default='')#联系地址
    upcode = models.CharField(max_length=10,default='')#邮编一般为六位
    class Meta:
        db_table = 'userinfo'#指定表的名称