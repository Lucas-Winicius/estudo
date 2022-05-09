import urllib
import urllib.request
site = ''
try:
    site == urllib.request.urlopen('http://www.youtube.com/')
except urllib.error.URLError:
    print('O SITE NAO ESTA ACESSIVEL')
else:
    print('SITE ATIVO')