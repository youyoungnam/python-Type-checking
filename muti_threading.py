# import asyncio
#
# import requests
# import time
# import os
# import threading
#
# # def fetcher(session, url):
# #     print(os.getpid(), "Process | ", threading.get_ident(), "url: ", url)
# #     with session.get(url) as response:
# #         return response.text
# #
# #
# #
# # def main():
# #     urls = ["https://google.com", "https://apple.com"] *50
# #
# #     with requests.Session() as session:
# #         result = [fetcher(session, url) for url in urls]
# #         print(result)
# #
# # if __name__ == "__main__":
# #     main()
# # import aiohttp
# # async def fetcher(session, url):
# #     print(f"{os.getpid()} process | {threading.get_ident()} url: {url}")
# #     async with aiohttp.ClientSession() as response:
# #         return await response.text()
# #
# # async def main():
# #     urls = ["https://google.com", "https://apple.com"] *50
# #     async with aiohttp.ClientSession() as session:
# #         result = await asyncio.gather(fetcher(session, url) for url in urls)
# #         print(result)
# # if __name__ == "__main__":
# #     aiohttp.run()
#
#
# # 멀티 스레딩 구현
# from concurrent.futures import ThreadPoolExecutor
# # def fetcher(session, url):
# #     print(os.getpid(), "Process | ", threading.get_ident(), "url: ", url)
# #     with session.get(url) as response:
# #         return response.text
#
#
# # 파이썬은 기본적으로 병렬적으로 수행이안됨 멀티스레딩이
# # 웬만하면 코루틴을 쓰는게 좋음
# # def fetcher(params):
# #     print(params)
# #     session = params[0]
# #     url = params[1]
# #     def fetcher(session, url):
# #         print(os.getpid(), "Process | ", threading.get_ident(), "url: ", url)
# #         with session.get(url) as response:
# #             return response.text
# #
# #
# #
# # def main():
# #     urls = ["https://google.com", "https://apple.com"] *50
# #     executor = ThreadPoolExecutor(max_workers=1)
# #     with requests.Session() as session:
# #         result = [fetcher(session, url) for url in urls]
# #         print(result)
# #         # 실행시키고 싶은 함수 첫 번째 인자 그다음 파라미터
# #         executor.map(fetcher, urls)
# #
# #         # 세샨, 실행시킬 함수, 파라메터
# #
# #         # params = [(session, url) for url in urls]
# #
# # if __name__ == "__main__":
# #     main()
#
#
# import requests
# import time
# import os
# import threading
# from concurrent.futures import ThreadPoolExecutor
#
#
# def fetcher(params):
#     session = params[0]
#     url = params[1]
#     print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
#     with session.get(url) as response:
#         return response.text
#
#
# def main():
#     urls = ["https://google.com", "https://apple.com"] * 50
#     # 쓰레드가 여러개 실행된것도 볼 수 있음 빨라진 이유가 동시성 프로그래밍 되서 그렇다
#     # 각각의 스레드가 동시적으로 fetcher를 처리해서 그런것
#     # 웬만하면 코루틴 쓰자 왜냐 이거 쓰레드를 하나하나 만드는 것도 거기에 우선순위를 부여하는 것도 연산과정임
#     # 웬만하면 ayncio로 싱글 스레드 기법으로 코루틴 동작보다 메모리를 더 잡아먹음
#     executor = ThreadPoolExecutor(max_workers=10)
#
#     with requests.Session() as session:
#         # result = [fetcher(session, url) for url in urls]
#         # print(result)
#         params = [(session, url) for url in urls] # 연산 추가
#         results = list(executor.map(fetcher, params)) # 연산 추가
#         print(results)
#
#
# if __name__ == "__main__":
#     start = time.time()
#     main()
#     end = time.time()
#     print(end - start)  # 6.8


# 모든상황에서 동시성 프로그래밍이 좋은건 아니다
# 만약 동시에 at the same time  여러개의 cpu core가 존재한다면, cpu core들에게 각각 연산을 맡게하면 된다

# 멀티 프로세싱 프로세스가 여로개로 복제되서 각각의 프로세스에서 계산을 수행 각각의 프로세스는 멀티스레딩을 사용할 수 있음 동시성도 사용할 수 있고
# 병렬성도 사용가능
# 멀티스레딩은 하나의 프로세스를 여러개로 만들어서 메모리를 공유함 계산하다가 망하면 다른 애들도 망할 수 있
# cpu 집약적인 연산을할 때는 멀티 프로세싱을 하는게 좋음 병렬성으로