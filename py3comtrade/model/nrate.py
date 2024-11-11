#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Nrate:
    """
    每个采样段的采样率,采样序号
    """
    __index: int  # 采样段索引号
    __samp: int  # 采样率, 单位为Hz
    __end_point: int  # 该段最末的采样序号
    __start_point: int  # 该段最开始的采样序号
    __cycle_point: int  # 该采样段每周波包含的采样点数
    __count: int  # 该采样段的采样点数
    __waste_time: int  # 该采样段时间
    __end_time: int  # 该段结束时间

    def __init__(self, samp: int = 0, end_point: int = 0):
        """
        每个采样段的采样信息
        """
        self.__samp = samp
        self.__end_point = end_point

    def clear(self):
        self.__samp = 0
        self.__end_point = 0
        self.__start_point = 0

    def __str__(self):
        return f"{self.samp},{self.end_point}"

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value):
        self.__end_point = value

    @property
    def samp(self):
        return self.__samp

    @samp.setter
    def samp(self, value):
        self.__samp = value

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value):
        self.__start_point = value

    @property
    def cycle_point(self):
        return self.__cycle_point

    @cycle_point.setter
    def cycle_point(self, value):
        self.__cycle_point = value

    @property
    def count(self):
        if self.__count != (count := self.end_point - self.start_point):
            return count
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value

    @property
    def waste_time(self):
        return self.__waste_time

    @waste_time.setter
    def waste_time(self, value):
        self.__waste_time = value

    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value
