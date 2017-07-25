from books.bookwebs.biquge import BiQuGe

repo_mapper = {
    'biquge':{
        'name':'笔趣阁',
        'obj':BiQuGe(),
        'site':'http://www.qu.la/',
        'book_url_format':'http://www.qu.la/book/%s.html',
        'chapter_url_format':'http://www.qu.la/book/%s/%s.html',
        'site_regx':'http://www.qu.la/.*',
        'book_regx':'http://www.qu.la/book/([^/]*?)\.html',
        'chapter_regx':'http://www.qu.la/book/([^/]*?)/([^/]*?)\.html'
    }
}