import requests


def get(isbn):
    isbn = str(isbn)
    url = 'http://book.feelyou.top/isbn/'
    url = url+isbn
    print('Getting information from', url, '……')
    result = requests.get(url)
    return result.json()
