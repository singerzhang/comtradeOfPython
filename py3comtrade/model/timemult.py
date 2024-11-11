#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union


class TimeMult:
    def __init__(self, timemult: Union[float, int] = 1.0):
        self.clear()
        if not isinstance(timemult, (float, int)):
            raise TypeError("timemult must be float or int")
        self.__timemult = timemult

    def clear(self):
        self.__timemult = 1.0

    @property
    def timemult(self):
        return self.__timemult

    @timemult.setter
    def timemult(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("timemult must be float or int")
        self.__timemult = value
