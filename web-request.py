import requests


resposta = requests.get("http://bancocn.com")
html = resposta.text
print(html)