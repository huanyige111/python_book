from urllib import parse
from django.utils.http import urlquote,unquote
from pyquery import PyQuery as pq
from books.bookwebs import utils
import requests

class BiQuGe(object):
    
    site = 'biquge'
    url = 'http://www.qu.la/'
    search_url = 'http://zhannei.baidu.com/cse/search?s=920895234054625192&entry=1&%s'
    catalog_url = url+'book/%s/'
    chapter_url = url+'book/%s/%s.html'

    def chapter(self,chapter_id,book_id):
        chapter_url_r = self.chapter_url % (book_id,chapter_id)
        response = requests.get(chapter_url_r)
        response.encoding = 'UTF-8'
        html = response.text
        response.close()
        try:
            pq(html)
        except Exception as e:
            return []
        context = pq(html)
        content = context.find('#content').html()
        title = context.find('.bookname').find('h1').text()
        pre_url = str(context.find('a#A1').attr('href'))
        next_url = str(context.find('a#A3').attr('href'))
        if len(pre_url) > 5:
            pre_url = pre_url[0:-5]
        else:
            pre_url = ''
        if len(next_url) > 5:
            next_url = next_url[0:-5]
        else:
            next_url = ''
        chapter_info = {'content':content, 'title':title, 'repo_name':self.site, 'book_id':book_id, 'pre_id':pre_url, 'next_id':next_url}
        return chapter_info
        

    '''  目录  '''
    def catalog(self,q,site,order='asc'):
        catalog_url_r = self.catalog_url % (q)
        response = requests.get(catalog_url_r)
        response.encoding = 'UTF-8'
        html = response.text
        response.close()
        try:
            pq(html)
        except Exception as e:
            return []
        chapters_a_tags = pq(html).find('#list').find('a') 
        chapter_list = []
        for chapter_a_tag in chapters_a_tags:
            chapter_name = pq(chapter_a_tag).text()
            chapter_url = pq(chapter_a_tag).attr('href')
            args = utils.pick_from_str(chapter_url,'/book/(\d+)/(\d+).html',[1,2])
            book_id = args[0]
            chapter_id = args[1]
            chapter_list.append({'chapter_name':chapter_name,'chapter_url':chapter_url,'book_id':book_id,'chapter_id':chapter_id})
        if(order == 'desc'):
            chapter_list.reverse()
        book_name = pq(html).find('#info').find('h1').text()
        chapter_info = {'book_name':book_name,'chapterlist':chapter_list,'site':self.site}
        return chapter_info


    def search(self,keyword):
        keyword = parse.urlencode({'q':keyword})
        search_url_r = self.search_url % (keyword)
        response = requests.get(search_url_r)
        response.encoding = 'UTF-8'
        html = response.text
        response.close()
        booktags = pq(html).find('#results').find('[class="result-game-item-detail"]')
        list_book_info = []
        for tag in booktags:
            title_a_tag = pq(tag).find('a[cpos=title]')
            book_url = title_a_tag.attr('href')
            book_name = str(title_a_tag.text()).replace(' ','')
            book_id = book_url.split('/')[-2]
            newchapter_a_tag = pq(tag).find('a[cpos=newchapter]')
            chapter_url = newchapter_a_tag.attr('href')
            chapter_name = str(newchapter_a_tag.text()).replace(' ','')
            #print(str(book_url)+'  '+ str(book_name)+'  '+ str(chapter_url)+'  '+ str(chapter_name)+'  '+ str(book_id))
            list_book_info.append({'book_url':book_url,'book_name':book_name,'chapter_url':chapter_url,'chapter_name':chapter_name,'book_id':book_id})
        book_info = {'listbook':list_book_info,'site':self.site}
        return book_info
