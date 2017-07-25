from django.utils.http import urlquote
from django.utils.http import unquote
from django.core.urlresolvers import resolve


#print(unquote('http%3A//127.0.0.1%3A8000/plist/%3Fp1%3Dchina%26p2%3D2012'))
func, args, kwargs = resolve('/some/path/')
print(str(func)+'  '+str(args)+'  '+str(kwargs))