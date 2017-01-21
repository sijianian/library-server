# coding:utf8
from bs4 import BeautifulSoup
import urllib
import re


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, soup):
        reason = []
        for tr in soup.find('tbody').find_all('tr'):
            temp = {}
            temp_arr = []
            for td in tr.find_all('td'):
                temp_arr.append(td.get_text())
            temp['id'] = temp_arr[0]
            temp['name'] = temp_arr[1]
            temp['auth'] = temp_arr[2]
            temp['pubilsh'] = temp_arr[3]
            temp['date'] = temp_arr[4]
            temp['index'] = temp_arr[5]
            temp['all'] = temp_arr[6]
            temp['remain'] = temp_arr[7]
            reason.append(temp)
        return reason

    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_data = self._get_new_data(soup)
        return new_data
