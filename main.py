from urllib import request

resposta = request.urlopen("http://g1.com.br")
html = resposta.read()
print(html)