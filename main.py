from urllib import request, parse

#criando um dicionario para fazer bypass do WAF
cabecalho = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Cookie": "cf_clearance=eiBP.XVHTCd.QZVWX9iQT7FPwx_3wB5dfcZtUUn.yqU-1673286953-0-150"}

dados = {"user":"admin", "password":"senhafoda"}
dados = parse.urlencode(dados).encode()

req = request.Request("http://www.bancocn.com/admin/index.php", headers=cabecalho, data=dados)
resposta = request.urlopen(req)
html = resposta.read()
print(html)



