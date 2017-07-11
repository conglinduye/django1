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
        goods = GoodsInfo.objects.get(pk = int(id))
        goods.gclick+=1
        goods.save()
        #找到当前分类对象，在找到此分类对象最新的两个
        new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        context = {'title': '天天生鲜-商品详情', 'top': '0', 'cart_num': '1','new_list':new_list,'goods':goods }
        response=render(request, 'bookgoods/detail.html', context)
        #最近浏览[]1'2'3'4'5
        ids=request.COOKIES.get('goods_ids','').split(',')
        if id in ids:
            ids.remove(id)
        ids.insert(0,id)
        if len(ids)>5:
            ids.pop()
        response.set_cookie('goods_ids',','.join(ids),max_age=60*60*24*7)
        return response
    except: return render(request,'404.html')



#商品列表页
def goods_list(request,tid,pindex,orderby): #tid:商品分类id ;pindex：页码编号;orderby:商品排序编号
    t1 = TypeInfo.objects.get(pk=tid)
    #orderby:1为默认排序  2为按价格排序  3为按人气排序
    orderby_str = '-id' #默认排序，根据id降序
    desc = '1'#按价格排序，默认为降序
    if int(orderby) == 2:
        desc = request.GET.get('desc')
        if desc =='1':
            orderby_str = '-gprice'
        else:
            orderby_str = 'gprice'
    if int(orderby) == 3:#按人气降序
        orderby_str = '-gclick'
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by(orderby_str)
    print(orderby_str)
    paginator = Paginator(glist,10)
    pindex1=int(pindex)
    if pindex1<=1:
        pindex1=1
    if pindex1>=paginator.num_pages:
        pindex1=paginator.num_pages
    page = paginator.page(pindex1)

    context = {'title':'天天生鲜-商品列表','top':'0','cart_num':'1','new_list':new_list,'page':page,'t1':t1,'orderby':orderby,'desc':desc}
    return render(request,'bookgoods/list.html',context)