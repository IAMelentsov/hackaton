#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-16 18:21
@summary: 
@author: i.melentsov
'''

import sys
sys.path = ['../'] + sys.path
from yandex_main_loader import YandexMainMessageProvider

class YandexMainTrafficProvider(YandexMainMessageProvider):

    def __init__(self):
        super(YandexMainMessageProvider, self).__init__()

    def get_message(self):
        soup = self.get_soup()
        traffic_ball = soup.findAll("a", { "data-statlog" : "traffic.ball" })[0].text
        traffic_more = soup.findAll("a", { "data-statlog" : "traffic.more" })[0].text
        return 'По данным яндекса, пробки - {}. {}.'.format(
                traffic_ball,
                traffic_more
            )

   
if __name__ == '__main__':
    ymmp = YandexMainTrafficProvider()
    print(ymmp.get_message())