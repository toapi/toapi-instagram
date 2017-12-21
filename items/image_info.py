#!/usr/bin/env python
from toapi import Item, Css


class ImageInfo(Item):
    __base_url__ = "https://www.instagram.com"

    image_url = Css('head > meta[property="og:image"]', attr='content')
    description = Css('head > meta[property="og:description"]', attr='content')
    source_url = Css('head > meta[property="og:url"]', attr='content')
    user_id = Css('head > meta[property="instapp:owner_user_id"]', attr='content')
    user_info_url = Css('head > meta[property="instapp:owner_user_id"]', attr='content')

    def clean_user_info_url(self, user_info_url):
        return "https://i.instagram.com/api/v1/users/{}/info/".format(user_info_url)

    class Meta:
        source = None
        route = {
            '/p/:path': '/p/:path'
        }

        web = {
            "with_ajax": False
        }
