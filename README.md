# python-Type-checking
- Python SDK를 개발하면서, python function, class에 type을 넣는 방법을 기록


## function type 지정

- function_type.py에 function에 type을 사용하는 방법 
- type alias 사용법 
- requests 요청
- response json 타입 지정 방법

## Class type 지정
- Class 내부에서 클래스 자신을 호출하는 타입 지정 방법
- Generic Type Class에 적용방법
- __slot__를 통해 클래스 메모리 효율을 관리 하는 방법
- isinstance 함수를 사용하여 Type체크하는 방법

## aiohttp using asyncio 사용 
- aiohttp 와 asyncio를 사용해서 동시성 프로그래밍 작성하기(Feat. 예제)
  - 해당 예제를 잘 활용하면, 이미지를 동시에 s3에 저장하는 기능 구현에 사용할 수 있을 것
- 

## multi_threading
- 파이썬에서 muti threading보다 코루틴 사용하는게 좋은 이유(Feat 예제)
- 멀티스레딩은 하나의 프로세스를 여러개로 만들어서 메모리를 공유하기 때문에 특정 연산을 하다가 망하면 다른 애들도 망할 수 있음
- cpu 집약적인 연산을할 때는 멀티 프로세싱을 하는게 좋다.

## FastApi
- fastapi 사용하기 위해서는 uvicorn과 ASGI에 대해 알아야한다. 
  - 간단한 정리 파이썬에서 웹 서버를 실행하기 위해서 WSGI가 필요하다. 
    - WSGI가 무엇인가? 
      - 웹서버가 파이썬 웹 애플리케이션과 통신하기 위한 인터페이스다.
      - 즉, WSGI로 개발한 웹 서버는 WSGI를 구현 파이썬 애플리케이션을 실행할 수 있다.
    - ASGI는 WSGI의 업그레이드 된 버전이다. 
      - 즉, ASGI는 파이썬에서 비동기로 구현을 했을 때 비동기 코드를 처리할 수 있다.
      - WSGI의 단점인 비동기 코드를 처리하지 못하는 것을 보안한게 ASGI다.
    - ASGI는 비동기 호출이 가능하도록 설계가 되어있다. 따라서 웹 클라이언트에서 한번에 많은 요청이 온다면,
    백그라운드 에서 코루틴으로 처리할 수 있다.
  - Uvicorn는 ASGI를 구현한 서버이다. 