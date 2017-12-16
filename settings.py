import os

from toapi.cache import RedisCache, JsonSerializer
from toapi.settings import Settings


class MySettings(Settings):
    """
    Create custom configuration
    """
    cache = {
        'cache_class': RedisCache,
        'cache_config': {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0
        },
        'serializer': JsonSerializer,
        'ttl': None
    }
    storage = {
        "PATH": os.getcwd(),
        "DB_URL": None
    }
    web = {
        "with_ajax": False,
        "request_config": {
            'proxies': {
                'http': '0.0.0.0:8118',
                'https': '0.0.0.0:8118'
            }
        },
        "headers": None
    }
