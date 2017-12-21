#!/usr/bin/env python
from toapi import Api

from items.image_info import ImageInfo
from items.user import User
from settings import MySettings

api = Api(settings=MySettings)

api.register(ImageInfo)
api.register(User)

if __name__ == '__main__':
    api.serve()
