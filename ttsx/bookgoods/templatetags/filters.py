#coding=utf-8
from django.template import Library  #导入
#创建组策对象
register = Library()
#有参数
@register.filter()
def multi(desc):
    return int(desc*(-1))
