import books.bookwebs.constant 
import re

'''  用正则从字符串中抽取参数   indexs为参数下标的集合  '''
def pick_from_str(str,regx,indexs):
    m = re.match(regx,str)
    result = []
    if(m):
        for index in indexs:
            result.append(m.group(index))
        return result
    else:
        print('不匹配   str:'+str+'  regx:'+regx)
        return []

def ismatch(str,regx):
    m = re.match(regx,str)
    if(m):
        return True
    else:
        return False

def get_host(url):
    res = pick_from_str(url, 'http[s]{0,1}://([a-z0-9A-Z\.]+)[:0-9]*/.*', [1])
    if len(res)>0 :
        return res[0]
    else:
        return ''

def trans_to_local(url):
    if ismatch(url, constant.repo_mapper['biquge']['site_regx']):
        if ismatch(url, constant.repo_mapper['biquge']['book_regx']):
            res = pick_from_str(url, constant.repo_mapper['biquge']['book_regx'], [1])
            return {'name':'biquge', 'book_id':res[0]}
        elif ismatch(url, constant.repo_mapper['biquge']['chapter_regx']):
            res = pick_from_str(url, constant.repo_mapper['biquge']['chapter_regx'], [1])
            return {'name':'biquge', 'book_id':res[0], 'chapter_id':res[1]}
    elif 1 == 1:
        pass
    return ''

def trans_to_repo(data): 
    repo_url = ''
    if data['name'] == 'biquge':
        if 'chapter_id' in data.keys():
            repo_url = constant.repo_mapper['biquge']['chapter_url_format'] % (data['book_id'], data['chapter_id'])
        else:
            repo_url = constant.repo_mapper['biquge']['book_url_format'] % (data['book_id'])
    return repo_url
