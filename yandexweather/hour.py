#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base

class cls(base.cls):
    _at = None
    _temperature = None

    def __init__(self,at=None,temperature=None):
        self._at=None
        self._temperature=None
        if at is not None:
            self.at=at
        if temperature is not None:
            self.temperature=temperature

    @property
    def at(self):
        return self._at

    @at.setter
    def at(self, v):
        if not v in map(int,range(0, 24)):
            raise Exception("invalid hour at %s\n expected 0..23" % v)
        self._at = v

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, v):
        if not isinstance(v,int):
            raise Exception("invalid temperature. int expected")
        self._temperature = v 

    def __str__(self):
        return str(self.at)

    def __repr__(self):
        return "%sh %sC" % (self.at,self.temperature)

def factory(e):
    return cls(
        at=int(e.attrib["at"]),
        temperature=int(e.temperature)
    )