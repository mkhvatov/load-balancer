import re

from src import settings, redis
from src.constants import URL_FORMAT


def is_url_correct(url: str) -> bool:
    """Checks if url format is correct"""
    return bool(re.match(URL_FORMAT, url))


def generate_cdn_url(original_url: str) -> str:
    """Generate url to cdn for concrete video file"""
    path = re.sub(r'\.([a-z0-9\-]+)/(video)/', '/video/', original_url)
    return re.sub(r'^(http|https)(://)', f'http://{settings.CDN_HOST}/', path)


async def get_actual_url(original_url: str) -> str:
    """Returns url type according to round robin algorithm"""
    counter = await redis.increment('counter')
    if counter % settings.ORIGINAL_LINK_FREQUENCY == 0:
        return original_url
    else:
        return generate_cdn_url(original_url)
