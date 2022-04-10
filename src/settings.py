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
# frequency to redirect to the original server (1 means 1 time out of 10)
ORIGINAL_LINK_FREQUENCY = env.int('ORIGINAL_LINK_FREQUENCY', default=1)
# frequency to redirect to cdn (9 means 9 times out of 10)
CDN_LINK_FREQUENCY = env.int('CDN_LINK_FREQUENCY', default=9)
CDN_HOST = env.str('CDN_HOST', default='www.awesome-cdn.ru')
