#!/usr/bin/env python
# -*- coding: utf-8 -*-
class cls(object):
    def __init__(self, **kwargs):
        while len(kwargs) > 0:
            setattr(self, kwargs.keys()[0], kwargs.pop(kwargs.keys()[0]))