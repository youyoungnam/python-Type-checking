# from typing import Optional
# from fastapi import FastAPI
#
# #uvicorn는 ASGI 구현체 파이썬으로 만들어진 이 코드를 ASGI에서 실행할 수 있게 함
# # app이라는 자체가 핵심적인 인스턴스 이게 싱글톤 패턴
# # @ decorator 함수에다가 함수를 뿌려주는 것
# app = FastAPI()
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
# # 웹이 클라이언트 브라우저 이 프로그램이 서버
# # 클라이언트인 웹이 get과 url를 통해서 get url를통해서 get이라는 http 프로토콜를 보냄 이 응답이 return인것
# # @app.get("/hello")
# def read_root():
#     print("hello FastAPi")
#
# # http://127.0.0.1:8000/item/3/xczxca?q=dasda
# # ?q는 쿼리 쿼리안에 변수가 들어감 optoinal str이라서 와도되고 안와도 되는 것 있어도되고 없어도됨
# @app.get("/item/{item_id}/{xyz}")
# def read_item(item_id: int, xyz:str, q: Optional[str] = None):
#     return {"item_id": item_id, "q":q}



# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
# from fastapi.templating import Jinja2Templates
# #fastapiApp 안에 templates를 지정 즉 하나하나 바꿔주는게 아니라 path를 지정하고 싶음
#
# # path(__file__) 현재 파일 경로임 parent하는 순간 main.pu의 부모를 가리킴
# # 절대경로 지정해서 사용
# BASE_DIR = Path(__file__).resolve().parent
#
# app = FastAPI()
#
# # middle ware css, image ㅊㅓ리, png file, 등등이 static file임
# # app.mount("/static", StaticFiles(directory="static"), name="static")
#
# # html file 위치를 지정
# templates = Jinja2Templates(directory="fastapiApp/templates")
#
# # 라우터는 웹 클라이언트, 클라이언트에게 요청을 받고 해당하는 로직에 따라 처리
# # response_class는 response타입을 html response로 결정하고 싶은것 즉 html로 서빙하고 싶을 때
# @app.get("/item/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     # 첫 번째인자는 html파일
#     # 두 번째인자는 item.html를 데이터를 보낼 수 잇음
#     return templates.TemplateResponse("index.html", {"request": request, "id": id, "data": "hello fastApi"})



# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from pathlib import Path
# from fastapi.templating import Jinja2Templates
# #fastapiApp 안에 templates를 지정 즉 하나하나 바꿔주는게 아니라 path를 지정하고 싶음
#
# # path(__file__) 현재 파일 경로임 parent하는 순간 main.pu의 부모를 가리킴
# # 절대경로 지정해서 사용
# BASE_DIR = Path(__file__).resolve().parent
#
# app = FastAPI()
#
# # middle ware css, image ㅊㅓ리, png file, 등등이 static file임
# # app.mount("/static", StaticFiles(directory="static"), name="static")
#
# # html file 위치를 지정
# templates = Jinja2Templates(directory="fastapiApp/templates")
#
# # app.get이라는 데코레이터가 이것을 어떤식으로 인식하냐면 옆에있는 타입힌트로 인식을 한다 만약에 해주지 않는다면 오류가 발생한다.
# @app.get("/item/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     print("requests속성값 알기: ",dir(request))
#     return templates.TemplateResponse("index.html", {"request": request, "id": id, "data": "hello fastApi"})

# 만약 request 파라미터르 지운다면 어떻게 될까?
# 에러가 난다 해당 에러는 contents는 반드시 requests key가 반드시 포함해야 한다.
# 왜냐면 TemplateResponse안에서 contents로 html에 변수로 보낼 때 requests key가 반드시 필요하다.
# @app.get("/item/{id}", response_class=HTMLResponse)
# async def read_item( id: str):
#     print("requests속성값 알기: ",dir(request))
#     return templates.TemplateResponse("index.html", {"request": request, "id": id, "data": "hello fastApi"})


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from odmantic import AIOEngine
from config import MONGO_DB_NAME, MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient
from fastapiApp.models.init import mongodb
from fastapiApp.models.book import BookModel

#fastapiApp 안에 templates를 지정 즉 하나하나 바꿔주는게 아니라 path를 지정하고 싶음

# path(__file__) 현재 파일 경로임 parent하는 순간 main.pu의 부모를 가리킴
# 절대경로 지정해서 사용
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# middle ware css, image ㅊㅓ리, png file, 등등이 static file임
# app.mount("/static", StaticFiles(directory="static"), name="static")

# html file 위치를 지정
templates = Jinja2Templates(directory="fastapiApp/templates")

# app.get이라는 데코레이터가 이것을 어떤식으로 인식하냐면 옆에있는 타입힌트로 인식을 한다 만약에 해주지 않는다면 오류가 발생한다.
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    book = BookModel(keyword="it", publisher="판판", price=2000, image="me.png")
    # await가 붙은 이유 save함수가 async 함수 코루틴 함수 즉 비동기 함수라서 붙임  # db save
    print(await mongodb.engine.save(book))
    # mongodb.engine.save_all 각각의 인스턴스 리스트에 대해서 각각의 인스턴스를 저장함 asyncaio gather를 통해 저장
    print(book, "@")
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "title": "콜렉터 북북이"
                                       })

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    return templates.TemplateResponse("index.html",{"request": request,
                                                    "keyword": q})


# fastapi 이벤트 실행 방법
# fastapi 실행되기전에 db연결하고 서버가 종료되면 db연결 끊게 하기
@app.on_event("startup")
def on_app_start():
    """
    before start fastapi server
    """
    mongodb.connect()



@app.on_event("shutdown")
async def on_app_shutdown():
    """
    after shutdown fastapi server
    """
    mongodb.close()