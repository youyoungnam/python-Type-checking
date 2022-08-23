from odmantic import AIOEngine
from config import MONGO_DB_NAME, MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_URL)
engine = AIOEngine(motor_client=client, database=MONGO_DB_NAME)


class MongoDB:

    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(motor_client=client, database=MONGO_DB_NAME)
        print("db와 성공적으로 연결되었습니다.")

    def close(self):
        self.client.close()
        print("db와 연결이 끊어졌습니다.")

# 싱글톤 패턴 와이 단 한번만 인스턴스를 호출해서
mongodb = MongoDB()
