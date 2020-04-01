import get
import code
import data

def add(isbn):
    c = get.get(isbn)
    data.add(code.decode(c))

def query_all():
    data.query_all()

def query_isbn(isbn):
    print(data.query_detail(isbn = isbn))
    print(data.query_rating(isbn = isbn))

act = input()
if act == 'add':
    while True:
        isbn = input()
        if isbn == 'x':
            break
        add(isbn)
if act == 'qa':
    res = data.query_all()
    for i in res :
        print(i.isbn,i.name)
        print('------')
if act == 'qs':
    while True:
        isbn = input()
        if isbn == 'x':
            break
        query_isbn(isbn)