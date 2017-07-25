import books.bookwebs.constant as constant

class BookRepositryAdapter(object):
    
    _repo_mapper = {}

    def __init__(self):
        self._repo_mapper = constant.repo_mapper

    def search(self,keyword):
        search_result = []
        for repo_name in self._repo_mapper:
            book_info = self._repo_mapper[repo_name]['obj'].search(keyword)
            book_info['repo_name'] = self._repo_mapper[repo_name]['name']
            search_result.append(book_info)
        return search_result

    def chapter(self, repo_name, chapter_id, book_id):
        if repo_name not in self._repo_mapper.keys():
            return {}
        chapter_info = self._repo_mapper[repo_name]['obj'].chapter(chapter_id, book_id)
        return chapter_info

    def catalog(self, book_id, repo_name, order='asc'):
        if repo_name not in self._repo_mapper.keys():
            return {}
        catalog_info = self._repo_mapper[repo_name]['obj'].catalog(book_id, repo_name, order)
        if len(catalog_info) < 1:
            return catalog_info
        chapter_list = catalog_info['chapterlist']
        newest_list = []
        if len(chapter_list) > 20:
            newest_list = chapter_list[-20:-1]
        else:
            newest_list = chapter_list[0:-1]
        newest_list.reverse()
        catalog_info['newestlist'] = newest_list
        return catalog_info
