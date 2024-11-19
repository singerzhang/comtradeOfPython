#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum


class DataFileType(Enum):
    ASCII = ("ASCII", "ASCII格式")
    BINARY = ("BINARY", "二进制格式")
    BINARY32 = ("BINARY32", "32位二进制文件")
    FLOAT32 = ("FLOAT32", "32位浮点数")

    @classmethod
    def from_string(cls, string: str):
        """
        尝试将给定的字符串转换为对应的枚举成员。

        :param string: 需要被解析的字符串
        :return: 对应的枚举成员或 None 如果没有匹配
        """
        string = string.strip().upper()
        for ft in cls:
            if string == ft.value[0]:
                return ft
        return cls.BINARY
