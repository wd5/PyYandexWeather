#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from datetime import date, datetime, time
import os
from os.path import abspath, dirname, join
import yandexweather


class TestCase(unittest.TestCase):
    filename=join(dirname(abspath(__file__)),'test.xml')
    def test_load(self):
        yandexweather.load(self.filename)

    def day_part_test(self,p):
        if p.temperature:
            self.assertIsInstance(p.temperature,int)
        self.assertIsInstance(p.wind_speed,float)
        self.assertIsNotNone(p.wind_speed)
        self.assertIsInstance(p.humidity,int)
        self.assertIsNotNone(p.humidity)
        self.assertIsInstance(p.pressure,int)
        self.assertIsNotNone(p.pressure)

    def forecast_test(self,p):
        self.assertIsInstance(p.observation_time,datetime)
        self.assertIsNotNone(p.observation_time)
        self.assertIsInstance(p.uptime,datetime)
        self.assertIsNotNone(p.uptime)  

    def day_test(self,day):
        self.assertIsInstance(day.date,date)
        self.assertIsNotNone(day.date)
        # sunrise
        self.assertIsInstance(day.sunrise,time)
        self.assertIsNotNone(day.sunrise)
        # sunset
        self.assertIsInstance(day.sunset,time)
        self.assertIsNotNone(day.sunset)
        # moonrise
        if day.moonrise:
            self.assertIsInstance(day.moonrise,time)
        # moonset
        if day.moonset:
            self.assertIsInstance(day.moonset,time)
        # day_parts
        for p in day.day_parts:
            # typeid
            self.assertIsInstance(p.typeid,int)
            self.assertIsNotNone(p.typeid)
            # type
            self.assertIsInstance(p.type,str)
            types=["morning","day","evening","night","day_short","night_short"]
            self.assertIn(p.type,types)

            self.day_part_test(p)
        # hours
        self.assertIsInstance(day.hours,list)
        for h in day.hours:
            self.assertIsInstance(h.at,int)
            self.assertIsNotNone(h.at)
            self.assertIsInstance(h.temperature,int)
            self.assertIsNotNone(h.temperature)

    def test_download(self):
        xml=yandexweather.download(26686)
        test=self.filename+"2"
        xml.save(test)
        os.unlink(test)
        # fact
        self.forecast_test(xml.fact)
        self.day_part_test(xml.fact)
        # yesterday
        self.forecast_test(xml.yesterday)
        self.day_part_test(xml.yesterday)
        self.assertIsInstance(xml.days,list)
        for d in xml.days:
            self.day_test(d)
        # shorthands
        self.assertIsNotNone(xml.today)
        self.assertIsNotNone(xml.tomorrow)
        self.assertIsInstance(xml.temperature,int)
        self.assertIsNotNone(xml.weather)
        self.assertIsNotNone(xml.wind_direction)
        self.assertIsInstance(xml.wind_speed,float)
        self.assertIsInstance(xml.humidity,int)
        self.assertIsInstance(xml.pressure,int)


if __name__ == "__main__":
    unittest.main()