# 모델은 하나의 데이터 즉, 하나의 도큐먼트 파이썬에서 불리는 용어가 모델

from odmantic import  Model

# 책을 수집을 하니 클래스이름은 북모델
# 즉 어떤 데이터를 수집할지 정하는 것
class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"


# db 내부에 collection 내부에는 document
# fastapi-pj collection books
# document {
# keyword: "파이썬",
# publisher: "~~",
# price: 20000,
# image: "sssd/jpg
# }