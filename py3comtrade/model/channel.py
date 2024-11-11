#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union

from py3comtrade.type.phase_code import PhaseCode


class Channel:
    """
    通道基类
    """

    __index: int
    __name: str
    __phase: PhaseCode
    __ccbm: str

    def __init__(
            self,
            index: Union[int, str],
            name: str,
            phase: Union[PhaseCode, str] = PhaseCode.NO_PHASE,
            ccbm: str = "",
    ):
        """
        通道基类
        :param index: 模拟通道索引号，必选，数字，整数
        :param name: 通道标识符，必选，字符串，最大长度128个字符
        :param phase: 通道相别标识，可选，字母、数字，最小0个字符，最大长度2个字符
        :param ccbm: 被监视的电路元件，可选，字母、数字，最小0个字符，最大长度64个字符
        """
        self.clear()
        self.__index = index if isinstance(index, int) else int(index)
        self.__name = name
        self.__phase = (
            phase if isinstance(phase, PhaseCode) else PhaseCode.from_string(phase)
        )
        self.__ccbm = ccbm

    def clear(self) -> None:
        self.__index = 0
        self.__name = ""
        self.__phase = PhaseCode.NO_PHASE
        self.__ccbm = ""

    def __str__(self):
        return f"{self.index},{self.name},{self.phase},{self.ccbm}"

    @property
    def index(self) -> int:
        return self.__index

    @index.setter
    def index(self, value: int) -> None:
        self.__index = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def phase(self) -> PhaseCode:
        return self.__phase

    @phase.setter
    def phase(self, value: PhaseCode) -> None:
        self.__phase = value

    @property
    def ccbm(self) -> str:
        return self.__ccbm

    @ccbm.setter
    def ccbm(self, value: str) -> None:
        self.__ccbm = value
