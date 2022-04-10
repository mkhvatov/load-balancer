import asyncio

import pytest

from src import redis


@pytest.fixture
def app():
    from src.server import app
    return app


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.run_until_complete(redis.down())
    loop.close()


@pytest.fixture(scope='session')
async def clear_storage():
    keys = [key async for key in redis.STORAGE.scan_iter(match='*')]
    await asyncio.gather(*[redis.STORAGE.delete(key) for key in keys])
