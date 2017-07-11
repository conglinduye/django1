#coding=utf-8
from django.shortcuts import render,redirect
from .models import UserInfo
from hashlib import sha1
from django.http import JsonResponse,HttpResponse
import datetime
from . import user_decorators  #导入装饰器函数
from bookgoods.models import *

# Create your views here.

#天天生鲜-注册
def register(request):
    return render(request,'booktest/register.html',{'title':'天天生鲜-注册'})

#将数据保存到数据库
def register_handle(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    ucpwd = request.POST.get('cpwd')
    uemail = request.POST.get('email')
    upwd1 = upwd.encode('utf-8')
    #密码加密
    s1 = sha1()
    s1.update(upwd1)
    upwd_sha1 = s1.hexdigest()
    #保存数据
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = uemail
    user.save()
    #重定向到本页
    #return redirect('/register/')
    #重定向到登陆页
    return redirect(('/login/'))

#判断注册名是否重复
def register_check(request):
    uname = request.GET.get('uname')
    num = UserInfo.objects.filter(uname=uname).count()
    contest = {'data':num}
    return JsonResponse(contest)

#天天生鲜-登陆
def login(request):
    uname = request.COOKIES.get('uname','')
    return render(request,'booktest/login.html',{'title':'天天生鲜-登陆','uname':uname})
#登陆界面
def login_handle(request):
    uname = request.POST.get('username')
    upwd = request.POST.get('pwd')
    ujz = request.POST.get('ujz')
    upwd1 = upwd.encode('utf-8')

    # 密码加密
    s1 = sha1()
    s1.update(upwd1)
    upwd_sha1 = s1.hexdigest()

    context={'title':'天天生鲜-登陆','uname':uname,'upwd':upwd}

    result=UserInfo.objects.filter(uname=uname)
    if len(result)==0:
        context['error_name'] = '输入用户名错误！'
        return render(request,'booktest/login.html',context)
    else:
        if result[0].upwd !=upwd_sha1:
            context['error_pwd']='输入密码错误！'
            return render(request,'booktest/login.html',context)
        else:
            response = redirect(request.session.get('url_path1','/goods/index/'))
            request.session['uid']=result[0].id#获取session中的id值
            request.session['uname']=result[0].uname#获取session中的uname值

            if ujz==1:
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days = 14))
            else:
                response.set_cookie('uname','',max_age=-1)
            return response

#用户中心-个人信息页面_info
@user_decorators.user_islogin
def user_center_info(request):
    #查询当前用户对象
    user = UserInfo.objects.filter(pk=request.session['uid'])
    users = user[0]
    print(user)
    #查询最近浏览
    ids = request.COOKIES.get('goods_ids','').split(',')[:-1]
    glist=[]
    for id in ids:
        glist.append(GoodsInfo.objects.get(id=id))
    print(glist)
    return render(request,'booktest/user_center_info.html',{'user':users,'title':'用户中心-个人信息','glist':glist})
#用户中心-全部订单页面_order
@user_decorators.user_islogin
def user_center_order(request):

    return render(request,'booktest/user_center_order.html',{'title':'用户中心-全部订单'})
#用户中心-收货地址页面_site
@user_decorators.user_islogin
def user_center_site(request):
    user = UserInfo.objects.filter(pk=request.session['uid'])
    users=user[0]
    a=request.method
    print(a)
    #get收货人信息
    if request.method == 'POST':
        userver = request.POST.get('userver')
        uaddress = request.POST.get('uaddress')
        uphon = request.POST.get('uphon')
        upcode = request.POST.get('upcode')

        #往数据库中存储重写收货人信息
        users.userver = userver
        users.uaddress = uaddress
        users.uphon = uphon
        users.upcode = upcode
        users.save()

        #context = {'title':'用户中心-收货地址','userver':userver,'uaddress':uaddress,'uphon':uphon,'upcode':upcode}
    return render(request,'booktest/user_center_site.html',{'user':users})
#退出登陆
def logout(request):
    request.session.flush()
    return redirect('/login/')
