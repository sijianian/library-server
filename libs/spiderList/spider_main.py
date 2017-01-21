# coding:utf8
from . import url_manager
from . import html_downloader
from . import html_parser
from . import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, dict_obj):
        html_cont = self.downloader.download(root_url, dict_obj)
        new_data = self.parser.parse(html_cont)
        return new_data
if __name__ == '__main__':
    root_url = 'http://222.200.122.171:7771/search.aspx'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
