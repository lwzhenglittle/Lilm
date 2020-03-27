from dataclasses import dataclass
import jsonpickle
import typing
@dataclass
class Rating:
    count: int
    rating_info: str
    star_count: float
    value: float


@dataclass
class Comment:
    user_name: str
    user_page: str
    user_pic: str
    vote: str
    rate: str
    time: str
    content: str


@dataclass
class BookData:
    create_time: str
    isbn: str
    title: str
    abstract: str
    book_intro: str
    author_intro: str
    catalog: str
    original_texts: list
    labels: list
    cover_url: str
    url: str
    rating: Rating
    comments: typing.List[Comment]
    source: str


def decode(source):  # source should be a dict
    data = BookData(**source)
    return data


def encode(source):  # source should be a bookdata
    return jsonpickle.encode(source)
