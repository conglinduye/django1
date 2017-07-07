#coding=utf-8
from django.shortcuts import redirect

def user_islogin(func):
    def func1(request,*args,**kwargs):
        #判断是否登陆
        if request.session.has_key('uid'):
            #如果登陆，则执行func函数
            return func(request,*args,**kwargs)
        else:
            #如果没有登陆，即转到login视图，进入登陆页面
            return redirect('/login/')
    return func1