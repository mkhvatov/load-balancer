# Redis API. Can be used as an independent module
#
from envparse import env
from aioredis import Redis, from_url


REDIS_PREFIX = env.str('REDIS_PREFIX', default='')
REDIS_ENDPOINT = env.str('REDIS_ENDPOINT', default='redis')
REDIS_DB = env.int('REDIS_DB', default=1)
REDIS_MAX_CONN = env.int('REDIS_MAX_CONN', default=10)
STORAGE: Redis = from_url(
    f'redis://{REDIS_ENDPOINT}',
    db=REDIS_DB,
    max_connections=REDIS_MAX_CONN,
    decode_responses=True,
)


async def down():
    """Close Redis connection pool"""
    if STORAGE:
        await STORAGE.close()


async def increment(key: str, amount: int = 1) -> int:
    """Increments the value of ``key`` by ``amount``.
    Returns incremented value"""
    counter = await STORAGE.incr(get_key(key), amount)
    return counter


def get_key(*args: str):
    return '_'.join((REDIS_PREFIX, *args))
