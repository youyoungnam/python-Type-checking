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



from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
#fastapiApp 안에 templates를 지정 즉 하나하나 바꿔주는게 아니라 path를 지정하고 싶음

# path(__file__) 현재 파일 경로임 parent하는 순간 main.pu의 부모를 가리킴
# 절대경로 지정해서 사용
BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()

# middle ware css, image ㅊㅓ리, png file, 등등이 static file임
# app.mount("/static", StaticFiles(directory="static"), name="static")

# html file 위치를 지정
templates = Jinja2Templates(directory="fastapiApp/templates")

# 라우터는 웹 클라이언트, 클라이언트에게 요청을 받고 해당하는 로직에 따라 처리
# response_class는 response타입을 html response로 결정하고 싶은것 즉 html로 서빙하고 싶을 때
@app.get("/item/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    # 첫 번째인자는 html파일
    # 두 번째인자는 item.html를 데이터를 보낼 수 잇음
    return templates.TemplateResponse("item.html", {"request": request, "id": id, "data": "hello fastApi"})

