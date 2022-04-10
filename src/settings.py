from envparse import env


# App server settings
#
HOST = env.str('HOST', default='0.0.0.0')
PORT = env.int('PORT', default=8000)
DEBUG = env.bool('DEBUG', default=False)
# tune it using your CPU's cores count
WORKERS = env.int('WORKERS', default=1)

# App logic settings
#
# frequency to redirect to the original server
# 10 means - redirect every tenth request to the original server.
# Rest 9 from 10 requests will be sent to cdn.
ORIGINAL_LINK_FREQUENCY = env.int('ORIGINAL_LINK_FREQUENCY', default=10)
CDN_HOST = env.str('CDN_HOST', default='www.awesome-cdn.ru')
