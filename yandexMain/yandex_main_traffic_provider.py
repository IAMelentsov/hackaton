#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2017-12-16 18:21
@summary: 
@author: i.melentsov
'''

import sys
sys.path = ['../'] + sys.path
from yandexMainLoader import YandexMainMessageProvider

class YandexMainTrafficProvider(YandexMainMessageProvider):

    def __init__(self):
        super(YandexMainMessageProvider, self).__init__()

   
if __name__ == '__main__':
    ymmp = YandexMainTrafficProvider()
    ymmp.get_message()