# coding:utf8
import urllib.request
from urllib import parse


class HtmlDownloader(object):
    def download(self, url, obj):
        if url is None:
            return None
        response = urllib.request.urlopen(
            url + parse.urlencode(obj, encoding='gb2312'))
        if response.getcode() != 200:
            return None
        return response
