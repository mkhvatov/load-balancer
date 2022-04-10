## Description
Load balancer service.  
The service accepts requests of the form:
> GET http://balancer-domain/?video=http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8

where:
* "balancer-domain" - balancer service hostname
* "http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8" - url of the video file on the original server s1

The service sends every tenth request of the described format to the original server.  
The rest of the requests are sent to cdn - to the url like:  
"http://$CDN_HOST/s1/video/1488/xcg2djHckad.m3u8", where:
* "s1" - server in originals cluster
* "$CDN_HOST" - configurable with environment variable url of the CDN service  

Requests are redirected by 301 HTTP redirect.

## Instruction
### Set environment variables in docker-compose.yml
_Below you can see the default values from settings.py_
```python
# App server settings
#
HOST = env.str('HOST', default='0.0.0.0')  # service host
PORT = env.int('PORT', default=8000)  # service port
DEBUG = env.bool('DEBUG', default=False)  # debug mode
WORKERS = env.int('WORKERS', default=1)  # the number of workers - tune it using your CPU's cores count

# App logic settings
#
ORIGINAL_LINK_FREQUENCY = env.int('ORIGINAL_LINK_FREQUENCY', default=10)  # frequency to redirect to the original server
CDN_HOST = env.str('CDN_HOST', default='www.awesome-cdn.ru')  # cdn host
```
For example, if you want to send every tenth request to the original server, set ORIGINAL_LINK_FREQUENCY=10.  
Rest 9 from 10 requests will be sent to cdn.

### How to build
> make build

### How to run service
> make up

Check it out:
> curl -i http://localhost:8000\?video\=http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8

### How to run tests
> make test

### Examples
Response from the first to the ninth calls:
> HTTP/1.1 301 Moved Permanently  
> Location: http://www.awesome-cdn.ru/s1/video/1488/xcg2djHckad.m3u8

Response to the every tenth call:
> HTTP/1.1 301 Moved Permanently  
> Location: http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8

Request with wrong url format:
> curl -i http://localhost:8000\?video\=http://s1.origin-cluster/vide/1488/xcg2djHckad.m3u8

Response:
> HTTP/1.1 400 Bad Request  
> {"error":"video-url format is not correct"}

Request with other query parameter in url:
> curl -i http://localhost:8000\?photo\=test.jpg

Response:
> HTTP/1.1 200 OK