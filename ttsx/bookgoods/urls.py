#coding=utf-8
from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^index/$',views.index),#首页
    url(r'^(\d+)/$',views.detail),#商品详细页
    url(r'^detail/$',views.detail),#商品详细页
    url(r'^list(\d+)_(\d+)/$',views.goods_list),#商品列表页
]