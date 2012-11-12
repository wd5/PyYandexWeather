#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
from requests import get
import xml

def url(id):
    return 'http://export.yandex.ru/weather-ng/forecasts/%s.xml' % id

def download(id):
    if isinstance(id,int):
        return xml.cls(get(url(id)).text)
    else:
        raise TypeError("download(int) expected")

def load(f="~/Downloads/forecast.xml"):
    return xml.cls(codecs.open(f,"r","ISO-8859-1").read())