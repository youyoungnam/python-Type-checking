# import time
# import asyncio
#
# async def delivery(name, mealtime):
#     print(f"{name}에게 배달완료!")
#     await asyncio.sleep(mealtime)
#     print(f"{name} 식사 완료, {mealtime}시간 소요...")
#     print(f"{name} 그릇 수거 완료!")
#
#     return mealtime
#
#
# async def main():
#     result = await asyncio.gather(
#     delivery("A", 1),
#     delivery("B", 1),
#     delivery("C", 1)
#     )
#     print(result)
#
# if __name__ =="__main__":
#     asyncio.run(main())
import asyncio
async def requests_users(name, id):
    print(f"user: {name}이 정보 요청을 하였습니다.")
    await asyncio.sleep(1)
    return f"{name}정보 전달"

async def main():
    result = await asyncio.gather(
        requests_users("a", 1),
        requests_users("b", 1),
        requests_users("c", 1)
    )
    print(result)
if __name__ =="__main__":
    print(asyncio.run(main()))
