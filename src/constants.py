import enum


URL_FORMAT = r'^(http|https)(://)([a-z]+[0-9]+)\.([a-z0-9\-]+)/(video)/' \
             r'([0-9]+)/([a-zA-Z0-9\.]+)$'


class LinkType(enum.IntEnum):
    ORIGINAL = 1
    CDN = 2
