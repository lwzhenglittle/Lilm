# 初步确定四个数据表
# books：概览表
# detail:细节表
# rating:评分表
# comment:评论表
# 均以isbn为关键字
from sqlalchemy import Column, String, create_engine, Text, Float, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Books(Base):

    __tablename__ = 'books'

    isbn = Column(String(13), primary_key=True)
    name = Column(String(128))
    cover_url = Column(String(96))


class Details(Base):

    __tablename__ = 'details'

    isbn = Column(String(13), primary_key=True)
    abstract = Column(Text)
    name = Column(String(128))
    book_intro = Column(Text)
    author_intro = Column(Text)
    catalog = Column(Text)
    labels = Column(Text)
    url = Column(String(96))


class Rating(Base):

    __tablename__ = 'rating'

    isbn = Column(String(13), primary_key=True)
    count = Column(Integer)
    info = Column(String(24))
    star_count = Column(Float)
    value = Column(Float)


#engine = create_engine(
#    'mysql+mysqlconnector://root:yuyu20040423@localhost:3306/lilm')
engine = create_engine(
    'sqlite:///test.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


def add(source):
    session = DBSession()
    session.add(Books(isbn=source.isbn, name=source.title,
                      cover_url=source.cover_url))
    session.add(Details(isbn=source.isbn, abstract=source.abstract, name = source.title, book_intro=source.book_intro,
                        author_intro=source.book_intro, catalog=source.catalog, labels=','.join(source.labels), url=source.url))
    session.add(Rating(isbn=source.isbn, count=source.rating['count'], info=source.rating['rating_info'],
                       star_count=source.rating['star_count'], value=source.rating['value']))
    session.add
    session.commit()
    session.close()

def query_all():
    session = DBSession()
    res = session.query(Books).all()
    session.close()
    return res

def query_detail(isbn):
    session = DBSession()
    res = session.query(Details).filter(Details.isbn==isbn).one()
    session.close()
    return res

def query_rating(isbn):
    session = DBSession()
    res = session.query(Rating).filter(Rating.isbn==isbn).one()
    session.close()
    return res;