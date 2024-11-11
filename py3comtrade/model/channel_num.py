#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union


class ChannelNum:
    """
    cfg文件通道数量
    """

    __total_num: int = 0
    __analog_num: int = 0
    __digital_num: int = 0

    def __init__(
            self,
            total_num: Union[str, int],
            analog_num: Union[str, int],
            digital_num: Union[str, int],
    ):
        """
        cfg文件通道数量
        :param total_num: 采样通道总数
        :param analog_num: 模拟量通道数量
        :param digital_num: 开关量通道数量
        """
        self.__total_num = self.__format_channel_num(total_num)
        self.__analog_num = self.__format_channel_num(analog_num)
        self.__digital_num = self.__format_channel_num(digital_num)

    def clear(self):
        self.__total_num = 0
        self.__analog_num = 0
        self.__digital_num = 0

    def __format_channel_num(self, value: Union[str, int]) -> int:
        if isinstance(value, str):
            return int("".join(filter(str.isdigit, value)))
        if isinstance(value, int):
            return self.__total_num
        return 0

    def __str__(self):
        return f"{self.total_num},{self.analog_num}A,{self.digital_num}D"

    @property
    def total_num(self):
        return self.__total_num

    @total_num.setter
    def total_num(self, value: Union[str, int]):
        self.__total_num = value

    @property
    def analog_num(self):
        return self.__analog_num

    @analog_num.setter
    def analog_num(self, value: Union[str, int]):
        self.__analog_num = value

    @property
    def digital_num(self):
        return self.__digital_num

    @digital_num.setter
    def digital_num(self, value: Union[str, int]):
        self.__digital_num = value
