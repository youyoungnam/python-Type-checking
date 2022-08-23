from odmantic import Model

class BookScraper(Model):
    keyword: str
    publisher: str
    price: int
    image: str


    class Config:
        collection = "bookScraper"

