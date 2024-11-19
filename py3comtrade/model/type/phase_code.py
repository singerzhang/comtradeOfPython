#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum, auto


class PhaseCode(Enum):
    N_PHASE = ('N', "N相通道")
    A_PHASE = ('A', "A相通道")
    B_PHASE = ('B', "B相通道")
    C_PHASE = ('C', "C相通道")
    NO_PHASE = auto()

    @classmethod
    def from_string(cls, string: str):
        """
        尝试将给定的字符串转换为对应的枚举成员。

        :param string: 需要被解析的字符串
        :return: 对应的枚举成员或 None 如果没有匹配
        """
        string = string.upper()
        for unit in cls:
            if unit == cls.NO_PHASE:
                continue
            if string.endswith(unit.value[0].upper()):
                return unit
        return cls.NO_PHASE
