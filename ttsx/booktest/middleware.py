#coding=utf-8
from django.http import HttpResponse,HttpRequest

class UrlPathMiddleware:
    def process_view(self,request,view_func,view_args,view_kwargs):
        path = request.get_full_path()
        path1 = request.path
        if request.path not in ['/login/',
                         '/register/',
                         '/register_handle/',
                         '/register_check/',
                         '/login_handle/',
                         '/logout/']:
            request.session['url_path']=request.get_full_path()

#下一步，去setting中注册中间件
'''
http://www.itcalt.cn/python?a=100
get_full_path():/python?a=100
path:/python
'''