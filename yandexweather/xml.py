#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import os
from os.path import abspath, dirname, exists, expanduser
from lxml.objectify import fromstring
import forecast
import day

class cls:
    source = None
    city=None
    country=None
    link=None
    lon=None
    lat=None
    part=None
    fact=None
    yesterday=None
    informer=None
    days=None

    def __init__(self,source=None):
        self.source=source
        tree=fromstring(source.encode('ISO-8859-1'))
        self.tree=tree
        a=tree.attrib
        self.city=a['city']
        self.country=a['country']
        self.link=a['link']
        self.lon=float(a['lon'])
        self.lat=float(a['lat'])
        self.part=a['part']
        self.fact=forecast.factory(tree.fact)
        self.yesterday=forecast.factory(tree.yesterday)
        self.days=[]
        for e in tree.day:
             self.days.append(day.factory(e))

    def day(self,date):
        l=filter(lambda d:d.date==date,self.days)
        if len(l)>0:
            return l[0]

    @property
    def today(self):
        return self.day(datetime.now().date())

    @property
    def tomorrow(self):
        return self.day((datetime.now()+timedelta(days=1)).date())

    @property
    def temperature(self):
        """return current hour temperature"""
        return self.today.hour(datetime.now().hour).temperature

    @property
    def current_part(self):
        """return current weather type"""
        if self.today==self.days[0]:
            return self.fact
        else:
            return self.today.current

    @property
    def weather(self):
        """return current weather type"""
        return self.current_part.weather_type

    @property
    def wind_direction(self):
        """return current wind_direction"""
        return self.current_part.wind_direction

    @property
    def wind_speed(self):
        """return current wind_speed"""
        return self.current_part.wind_speed

    @property
    def humidity(self):
        """return current humidity"""
        return self.current_part.humidity

    @property
    def pressure(self):
        """return current pressure"""
        return self.current_part.pressure

    def save(self,f="~/Downloads/forecast.xml"):
        f=abspath(expanduser(f))
        if not exists(dirname(f)):
            os.makedirs(dirname(f))
        open(f,"w").write(self.source.encode("ISO-8859-1"))