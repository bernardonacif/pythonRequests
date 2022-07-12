import requests
from requests.exceptions import RequestException
 
# 1XX - Informação
# 2XX - Sucesso
# 3XX - Redirecionar
# 4XX - Erro de cliente (você cometeu um erro)
# 5XX - Erro de servidor (eles cometeram um erro)

url1 = "http://www.not_exist.com/"
url2 = "https://httpbin.org/status/500"
url3 = "https://httpbin.org/delay/15"
url4 = 'https://www.google.com/' # ok

geral = [url1, url2, url3, url4]

def urlTest(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f'{response.status_code} - {url}') # All ok 200
    except RequestException as error: #essa está identificando os erros menos o 500
    # except requests.HTTPError as error: #nao está pegando nenhum erro 
        # pass
        print(error)
    except:
        print('erro desconhecido, cria')
    finally:
        print('========================')

contador = 1

for i in geral:
    print(f'teste n{contador}')
    urlTest(i)
    contador = contador + 1
    
