import urllib
import urllib.request
try:
   site = urllib.request.urlopen('https://www.tudogostoso.com.br')
except:
    print('ERRO')
else:
    print('Tudo ok!')