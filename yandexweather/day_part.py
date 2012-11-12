#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base

class cls(base.cls):
    temperature=None
    weather_type = None
    weather_type_short = None
    wind_direction = None
    wind_speed = None
    humidity = None
    pressure = None
    typeid=None
    type=None
 
def factory(e):
    if 'typeid' in e.attrib:
        typeid=int(e.attrib['typeid'])
    else:
        typeid=None
    if 'type' in e.attrib:
        type=e.attrib['type']
    else:
        type=None
    if 'temperature' in e.attrib:
        temperature=int(e.attrib['temperature'])
    else:
        temperature=None
    if hasattr(e,'temperature_from'):
        temperature_from=int(e.temperature_from)
    else:
        temperature_from=None
    if hasattr(e,'temperature_to'):
        temperature_to=int(e.temperature_to)
    else:
        temperature_to=None
    if hasattr(e,'temperature-data'):
        temperature_avg=int(getattr(e,'temperature-data').avg)
    else:
        temperature_avg=None
    d=dict(
        typeid=typeid,
        type=type,
        temperature_from=temperature_from,
        temperature_to=temperature_to,
        temperature_avg=temperature_avg,
        temperature=temperature,
        weather_type=e.weather_type.text,
        weather_type_short=e.weather_type_short.text,
        wind_direction=e.wind_direction.text,
        wind_speed=float(e.wind_speed),
        humidity=int(e.humidity),
        pressure=int(e.pressure)
    )
    return cls(**d)