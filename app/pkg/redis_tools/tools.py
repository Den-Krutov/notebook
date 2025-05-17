import redis


class RedisTools:
    __redis_connect = redis.Redis(host='localhost', port=6379)

    @classmethod
    def get_pair(cls, phone: str):
        return cls.__redis_connect.get(phone)

    @classmethod
    def write_pair(cls, phone: str, address: str):
        cls.__redis_connect.set(phone, address)

    @classmethod
    def get_keys(cls):
        return cls.__redis_connect.keys(pattern='*')
