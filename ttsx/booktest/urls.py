#coding=utf-8
from django.conf.urls import include, url
from . import views
urlpatterns = [
    url(r'^login/$',views.login),#首页登陆login
    url(r'^register/$',views.register),#注册页
    url(r'^register_handle/$',views.register_handle),#往数据库保存数据
    url(r'^register_check/$',views.register_check),#判断注册名是否重复
    url(r'^login_handle/$',views.login_handle),#登陆页面
    #用户中心的三个页面
    url(r'^user_center_info/$',views.user_center_info),#用户中心-个人信息
    url(r'^user_center_order/$',views.user_center_order),#用户中心-全部订单
    url(r'^user_center_site/$',views.user_center_site),#用户中心-地址信息
    url(r'^logout/$',views.logout),#退出
]