import pytest

from src.utils import is_url_correct, generate_cdn_url
from src.settings import CDN_HOST


@pytest.mark.parametrize(
    'url,is_correct',
    [
        ('http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8', True),
        ('https://s1.origin-cluster/video/1488/xcg2djHckad.m3u8', True),
        ('http://s1AAA.origin-cluster/video/1488/xcg2djHckad.m3u8', False),
        ('http://s1.origin-cluster#/video/1488/xcg2djHckad.m3u8', False),
        ('http://s1.origin-cluster/photo/1488/xcg2djHckad.m3u8', False),
        ('http://s1.origin-cluster/video/14aa88/xcg2djHckad.m3u8', False),
        ('http://s1.origin-cluster/video/1488/xcg2djHc/kad.m/3u8', False),
    ]
)
def test_is_url_correct(url, is_correct):
    assert is_url_correct(url) == is_correct


@pytest.mark.parametrize(
    'cdn_host,server',
    [
        (CDN_HOST, 's1'),
        (CDN_HOST, 's2'),
    ]
)
def test_generate_cdn_url(cdn_host, server):
    assert generate_cdn_url(
        f'http://{server}.origin-cluster/video/1488/xcg2djHckad.m3u8') == \
           f'http://{cdn_host}/{server}/video/1488/xcg2djHckad.m3u8'
