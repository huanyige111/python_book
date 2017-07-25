"""python_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^save$', views.save_book, name='save'), 
    url(r'^search$', views.search_book, name='search'),
    url(r'^(?P<site>[a-z0-9]+)/(?P<q>[0-9]+)/(?P<order>[a-z]+)$', views.show_catalog, name='catalog'),  
    url(r'^(?P<site>[a-z0-9]+)/(?P<book_id>[0-9]+)/(?P<chapter_id>[0-9]+)$', views.show_chapter, name='chapter'), 
    url(r'^order/save/(?P<repo_name>[a-z0-9]+)/(?P<book_id>[0-9]+)$', views.save_order, name='order'), 
    url(r'^order/list$', views.order_info, name='order_show'), 
    url(r'^order/del/(?P<repo_name>[a-zA-Z0-9]+)/(?P<book_id>[0-9]+)$', views.del_order, name='order_del'), 
]