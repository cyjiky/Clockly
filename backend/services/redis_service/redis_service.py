from redis.asyncio import Redis

from typing import Dict

class RedisService:
    @staticmethod
    def __define_redis_connection_parameters() -> Dict[str, str]:
        pass

    def __init__(self):
        self.__regis = Redis(**self.__define_redis_connection_parameters())

    