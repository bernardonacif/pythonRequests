import requests

# url = ['http://www.google.com/', 'http://www.google.com/', 'http://globo.com']

def url_ok(url): 
    try: 
        response = requests.head(url) 
        if response.status_code == 200: 
            return True 
        else: 
            return False 
    except requests.ConnectionError as e: 
        return e 
url = "http://www.google.com/alpha"

contador = 1

while contador < 15 :
    print(url_ok(url))
    contador = contador + 1
    


# def chamaApi():
#     print('startAplication')
#     try:
#         for i in zip(url):
#             r = requests.get(i)
#             r.raise_for_status()
#             print(r)
#             print(r.elapsed.total_seconds())
#     except requests.exceptions.HTTPError as err:
#         raise SystemExit(err)
#         # assert SystemExit(err)
# chamaApi()

# def chamaApi():
#     print('startAplication')
#     for i in zip(url):
#        r = requests.get(i)
#        r.raise_for_status()
#        print(r)
#        print(r.elapsed.total_seconds())
       
#         # assert SystemExit(err)
# chamaApi()
