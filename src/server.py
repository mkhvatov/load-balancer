from sanic import Sanic
from sanic.response import HTTPResponse, redirect, json
from sanic.request import Request

from src import settings
from src.utils import is_url_correct, get_actual_url


app = Sanic(name='load-balancer')


@app.route("/")
async def index(request: Request) -> HTTPResponse:
    video_url = request.args.get('video')

    if video_url and is_url_correct(video_url):
        url = get_actual_url(video_url)
        return redirect(to=url, status=301)

    if video_url and not is_url_correct(video_url):
        return json(
            {'error': 'video-url format is not correct'},
            status=400
        )
    return HTTPResponse()


if __name__ == '__main__':
    app.run(
        host=settings.HOST,
        port=settings.PORT,
        debug=settings.DEBUG,
        workers=settings.WORKERS,
    )
