#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import datetime
import base
import hour
import day_part

class cls(base.cls):
    date=None
    sunrise=None
    sunset=None
    moon_phase=None
    moonrise=None
    moonrise=None
    moonset=None
    day=None
    day_parts=None
    hours = None

    @property
    def morning(self):
        return self.day_parts[0]

    @property
    def day(self):
        return self.day_parts[1]

    @property
    def evening(self):
        return self.day_parts[2]

    @property
    def night(self):
        return self.day_parts[3]

    def hour(self,at):
        return filter(lambda x:x.at==at,self.hours)[0]

    @property
    def current(self):
        now=datetime.now()
        if 0<=now.hour<=5:
            return self.night
        if 6<=now.hour<=11:
            return self.morning
        if 12<=now.hour<=17:
            return self.day
        if 18<=now.hour:
            return self.evening

def str2date(text):
    return datetime.strptime(text,'%Y-%m-%d').date()

def time(text):
    return datetime.strptime(text,'%H:%M').time()


def factory(e):
    day_parts=map(day_part.factory,e.day_part)
    if hasattr(e,"hour"):
       hours=map(hour.factory,e.hour)
    else:
        hours=[]
    if hasattr(e,"moonset"):
        moonset=time(e.moonset.text)
    else: # maybe not exists
        moonset=None
    if hasattr(e,"moonrise"):
        moonrise=time(e.moonrise.text)
    else: # maybe not exists
        moonrise=None
    return cls(**dict(
        date=str2date(e.attrib["date"]),
        sunrise=time(e.sunrise.text),
        sunset=time(e.sunset.text),
        moon_phase=e.moon_phase.text,
        moonrise=moonrise,
        moonset=moonset,
        day_parts=day_parts,
        hours=hours
    ))