#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import day_part

class cls(day_part.cls):
    observation_time = None
    uptime = None
    temperature = None

def str2datetime(path):
    format='%Y-%d-%mT%H:%M:%S'
    return datetime.strptime(path,format)

    
def factory(e):
    i=day_part.factory(e)
    i.observation_time=str2datetime(e.observation_time.text)
    i.uptime=str2datetime(e.uptime.text)
    i.temperature=int(e.temperature)
    return i