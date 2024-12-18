#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright (c) [2019] [name of copyright holder]
#  [py3comtrade] is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan
#  PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#           http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY
#  KIND, EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
#  NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.
from enum import Enum


class PhaseCode(Enum):
    N_PHASE = ('N', "N相")
    A_PHASE = ('A', "A相")
    B_PHASE = ('B', "B相")
    C_PHASE = ('C', "C相")
    NO_PHASE = ('', "无相别")

    def __init__(self, code, descripton):
        self.code = code
        self.descripton = descripton

    def get_code(self) -> str:
        return self.code

    def get_description(self) -> str:
        return self.descripton

    @classmethod
    def from_string(cls, string: str):
        """
        尝试将给定的字符串转换为对应的枚举成员。

        :param string: 需要被解析的字符串
        :return: 对应的枚举成员或 None 如果没有匹配
        """
        string = string.upper()
        for phase in cls:
            if phase == cls.NO_PHASE:
                continue
            if phase.get_code() == string:
                return phase
        return cls.NO_PHASE
