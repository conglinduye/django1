from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
# Create your views here.

#首页显示
def index(request):
    type_list = TypeInfo.objects.all()
    list1 = []
    for type1 in type_list:
        new_list = type1.goodsinfo_set.order_by('-id')[0:4]
        click_list = type1.goodsinfo_set.order_by('gprice')[0:4]
        list1.append({'new_list':new_list,'click_list':click_list,'t1':type1})
    context = {'list1':list1,'top':'0','title':'首页','cart_num':'1'}
    return render(request,'bookgoods/index.html',context)  #top标志父模板需要继承的内容

#商品详情页
def detail(request,id):
    try:
        goods = GoodsInfo.objects.get(pk = id)
        #找到当前分类对象，在找到此分类对象最新的两个
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title': '天天生鲜-商品详情', 'top': '0', 'cart_num': '1','new_list':new_list,'goods':goods }
        return render(request, 'bookgoods/detail.html', context)
    except: return render(request,'404.html')



#商品列表页
def goods_list(request,tid,pindex):
    t1 = TypeInfo.objects.get(pk=tid)
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by('-id')
    paginator = Paginator(glist,15)
    page = paginator.page(pindex)
    context = {'title':'天天生鲜-商品列表','top':'0','cart_num':'1','new_list':new_list,'page':page,'t1':t1}
    return render(request,'bookgoods/list.html',context)