# page/1 page/2 page/3 .... 각각의 페이지를 동시에 html를 가져오는 것을 동시성 프로그래밍으로 시도

from bs4 import BeautifulSoup
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        cont_thumb = soup.find_all('div', "cont_thumb")
        for cont in cont_thumb:
            title = cont.find('p', 'txt_thumb')
            if title is not None:
                print(title.text)

async def main():
    BASE_URL = "https://bjpublic.tistory.com/category/%EC%A0%84%EC%B2%B4%20%EC%B6%9C%EA%B0%84%20%EB%8F%84%EC%84%9C"
    urls = [f"{BASE_URL}?/page={i}" for i in range(1, 10)]
    # session을 연결
    # page 1개에 대한 데이터를 가져오고
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url) for url in urls])


# 이미지 다운로더 만들기
# 수많은 이미지 데이터를 동시성을 이용하여 빠른 속도로 구현
# 만약 동시성이아니라 그냥 동기방식이였다면 느렸을것

import os
import aiofiles
async  def img_downloader(session, img):
    img_name = img.split("/")[-1]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    async with session.get(img) as response:
        if response.status == 200:
            # byte를 쓰기때문에 wb
            async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
            # 이미지를 aiohttp 세션을 통해 열으면 데이터가 있는데 데이터를 읽고 해당하는 이미지 데이터를 write안에 넣음
                await file.write(await response.read())

if __name__ == "__main__":
    asyncio.run(main())