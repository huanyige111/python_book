from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse  
from django.shortcuts import redirect  
from . import models
from books.bookwebs.adapter import BookRepositryAdapter
import books.bookwebs.utils as utils

# Create your views here.
def index(request):
    return redirect(reverse('order_show',args=[]))

def save_book(request):
    b = models.Book(title="哈哈哈1",source_web="http://www.baidu1.com")
    b.save() 
    return HttpResponse("<html>saved!</html>")  

def show_chapter(request,book_id,chapter_id,site):
    b = BookRepositryAdapter()
    chapter_info = b.chapter(site, chapter_id, book_id)
    template = loader.get_template('books/chapter.html')
    return HttpResponse(template.render({'chapter':chapter_info}, request))  

def search_book(request):
    keyword = request.POST.get('keyword')
    b = BookRepositryAdapter()
    book_info = b.search(keyword)
    print(book_info)
    template = loader.get_template('books/search.html')
    context = {'bookinfo':book_info}
    return HttpResponse(template.render(context,request))  

def show_catalog(request, q, site, order):
    b = BookRepositryAdapter()
    chapter_info = b.catalog(q, site, order)
    template = loader.get_template('books/catalog.html')
    context = {'chapter_info':chapter_info}
    return HttpResponse(template.render(context,request))  

def save_order(request, repo_name, book_id):
    user_id = request.session.get('user_id')
    template = loader.get_template('books/order.html')
    result = models.Order.objects.filter(user_id=user_id, book_id=book_id, repo_name=repo_name)
    if len(result)>0:
        return HttpResponse('已订阅该书籍')  
    source_web = utils.trans_to_repo({'name':repo_name, 'book_id':book_id})
    book_name = (BookRepositryAdapter().catalog(book_id, source_web))['book_name']
    order = models.Order(title=book_name, user_id=user_id, book_id=book_id, repo_name=repo_name, source_web=source_web)
    order.save()
    result = models.Order.objects.filter(user_id=user_id)
    return HttpResponse(template.render({'order_info':result},request))  

def order_info(request):
    user_id = 1
    request.session['user_id'] = user_id
    template = loader.get_template('books/order.html')
    result = models.Order.objects.filter(user_id=user_id)
    return HttpResponse(template.render({'order_info':result},request))  

def del_order(request, repo_name, book_id):
    user_id = request.session.get('user_id')
    models.Order.objects.filter(user_id=user_id, book_id=book_id, repo_name=repo_name).delete()
    template = loader.get_template('books/order.html')
    result = models.Order.objects.filter(user_id=user_id)
    return HttpResponse(template.render({'order_info':result},request)) 
