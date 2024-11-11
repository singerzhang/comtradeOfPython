#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime

time_format = "%d/%m/%Y,%H:%M:%S.%f"  # 时间格式字符串


def format_time(time):
    if isinstance(time, datetime):
        return time

    try:
        str_time = time.strip()
        return datetime.strptime(str_time, time_format)
    except ValueError as e:
        raise ValueError(f"时间格式错误:{e}")


class PrecisionTime:
    __time: datetime

    def __init__(self, time: str):
        self.__time = format_time(time)

    def clear(self):
        self.__time = datetime.now()

    def __str__(self):
        return f"{self.__time.strftime(time_format)}\n"

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = format_time(value)
