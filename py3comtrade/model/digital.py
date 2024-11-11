#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union

from py3comtrade.model.channel import Channel
from py3comtrade.type.phase_code import PhaseCode


class Digital(Channel):
    """
    开关量通道类
    """

    __status: int

    def __init__(
            self,
            index: Union[int, str],
            name: str,
            phase: PhaseCode = PhaseCode.NO_PHASE,
            ccbm: str = "",
            status: Union[int, str] = 0,
    ):
        """
        初始化
        :param index: 通道索引
        :param name: 通道名称
        :param phase: 通道相位
        :param ccbm: 通道CCBM
        :param status: 开关量状态
        """
        super().__init__(index, name, phase, ccbm)
        self.__status = int(status)

    def clear(self) -> None:
        super().clear()
        self.__status = 0

    def __str__(self):
        return super().__str__() + f",{self.status}"

    @property
    def status(self) -> int:
        return self.__status
