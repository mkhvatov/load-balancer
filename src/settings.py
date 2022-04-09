from envparse import env


# todo:
# url = 'http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8'
# wrong = 'http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8'


# App server settings
HOST = env.str('HOST', default='0.0.0.0')
PORT = env.int('PORT', default=8000)
DEBUG = env.bool('DEBUG', default=False)
# Tune it using your CPU's cores count
# todo:
WORKERS = env.int('WORKERS', default=1)

# App logic settings
ORIGINAL_LINK_FREQUENCY = env.int('ORIGINAL_LINK_FREQUENCY', default=1)
# todo: set to 10
CDN_LINK_FREQUENCY = env.int('CDN_LINK_FREQUENCY', default=2)
CDN_HOST = env.str('CDN_HOST', default='www.awesome-cdn.ru')