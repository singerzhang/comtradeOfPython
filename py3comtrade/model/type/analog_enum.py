#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, auto


class ElectricalUnit(Enum):
    KILOVOLT = ('kV', '千伏')
    VOLT = ('V', '伏特')
    KILOAMPERE = ('kA', '千安')
    AMPERE = ('A', '安培')
    NO_UNIT = auto()  # 表示无单位的情况

    @classmethod
    def from_string(cls, string: str):
        """
        尝试将给定的字符串转换为对应的枚举成员。

        :param string: 需要被解析的字符串
        :return: 对应的枚举成员或 None 如果没有匹配
        """
        string = string.lower()
        for unit in cls:
            if unit == cls.NO_UNIT:
                continue
            if string.endswith(unit.value[0].lower()):
                return unit
        return cls.NO_UNIT


class PsType(Enum):
    P = ('P', "一次值")
    S = ('S', "二次值")

    @classmethod
    def from_string(cls, string: str):
        """
        尝试将给定的字符串转换为对应的枚举成员。
        :param string: 需要被解析的字符串
        """
        string = string.upper()
        for ps in cls:
            if string.endswith(ps.value[0].upper()):
                return ps
        return cls.P


class AnalogType(Enum):
    AC = ('A', "交流通道")
    DC = ('D', "直流通道")
    OTHER = ('O', "其他通道")


class AnalogFlag(Enum):
    ACV = ('ACV', "电压")
    ACC = ('ACC', "电流")
    HF = ('HF', "高频")
    FQ = ('FQ', "频率")
    AG = ('AG', "相位")
    AMP = ('AMP', "幅值")
    PW = ('PW', "功率")
    ZX = ('ZX', "阻抗")
    CONST = ('CONST', "常量")
