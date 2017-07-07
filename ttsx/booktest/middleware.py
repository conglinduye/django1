#coding=utf-8
from django.http import HttpResponse,HttpRequest

class UrlPathMiddleware:
    def process_request(self,request):
        path = request.get_full_path()
        path1 = request.path
        if path1 not in ['/login/',
                         '/register/',
                         '/register_handle/',
                         '/register_check/',
                         '/login_handle/',
                         '/logout/']:
            request.session['url_path']=path1

#下一步，去setting中注册中间件
'''
http://www.itcalt.cn/python?a=100
get_full_path():/python?a=100
path:/python
'''