#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-16 17:47
@summary: 
@author: i.melentsov
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
from hakaton import MessageProvider

class YandexMainMessageProvider(MessageProvider):
    __yandex_base_url = "https://yandex.ru/"

    def __init__(self):
        super(YandexMainMessageProvider, self).__init__()

    def get_soup(self):
        return BeautifulSoup(urlopen(self.__yandex_base_url).read(), 'html.parser')