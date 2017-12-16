#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-16 18:21
@summary: 
@author: i.melentsov
'''
if __name__ == '__main__':
    import sys
    sys.path = ['../'] + sys.path

from yandex_main_loader import YandexMainMessageProvider

class YandexMainTrafficProvider(YandexMainMessageProvider):

    def __init__(self):
        super(YandexMainMessageProvider, self).__init__()

    def get_message(self):
        soup = self.get_soup().find(id="wd-_traffic")
        traffic_ball = soup.find("a", { "data-statlog" : "traffic.ball" }).text
        traffic_more = soup.find("a", { "data-statlog" : "traffic.more" }).text
        return 'По данным яндекса, пробки - {}. {}.'.format(
                traffic_ball,
                traffic_more
            )

if __name__ == '__main__':
    ymmp = YandexMainTrafficProvider()
    print(ymmp.get_message())