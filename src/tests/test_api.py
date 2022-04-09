import pytest


ORIGINAL_URL = "http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8"
CDN_URL = "http://www.awesome-cdn.ru/s1/video/1488/xcg2djHckad.m3u8"
WRONG_URL = "http://s1.origin-cluster/111/1488/xcg2djHckad.m3u8"


@pytest.mark.asyncio
async def test_basic(app):
    request, response = await app.asgi_client.get("/")
    assert request.method.lower() == "get"
    assert response.status == 200


@pytest.mark.parametrize(
    'status_code,redirect_to',
    [
        (301, CDN_URL),
        (301, CDN_URL),
        (301, ORIGINAL_URL),
        (301, CDN_URL),

    ]
)
@pytest.mark.asyncio
async def test_redirect(app, status_code, redirect_to):
    request, response = await app.asgi_client.get(f"/?video={ORIGINAL_URL}")
    assert response.status == status_code
    assert response.headers["Location"] == redirect_to


@pytest.mark.asyncio
async def test_wrong_url_format(app):
    request, response = await app.asgi_client.get(f"/?video={WRONG_URL}")
    assert response.status == 400
    assert response.json['error'] == 'video-url format is not correct'


@pytest.mark.asyncio
async def test_other_query_args(app):
    request, response = await app.asgi_client.get(f"/?photo=test.jpg")
    assert response.status == 200
