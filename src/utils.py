import re

import settings
from constants import LinkType, URL_FORMAT


def is_url_correct(url: str) -> bool:
    return bool(re.match(URL_FORMAT, url))


def generate_cdn_url(original_url: str) -> str:
    path = re.sub(r'\.([a-z0-9\-]+)/(video)/', '/video/', original_url)
    return re.sub(r'^(http|https)(://)', f'http://{settings.CDN_HOST}/', path)


def round_robin():
    """Round robin algorithm to select link type"""
    while True:
        for i in range(settings.CDN_LINK_FREQUENCY):
            yield LinkType.CDN
        for i in range(settings.ORIGINAL_LINK_FREQUENCY):
            yield LinkType.ORIGINAL


link_selector = round_robin()


def get_actual_url(original_url: str) -> str:
    link_type = next(link_selector)
    if link_type == LinkType.CDN:
        return generate_cdn_url(original_url)
    if link_type == LinkType.ORIGINAL:
        return original_url
