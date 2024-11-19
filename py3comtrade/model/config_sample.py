#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# Copyright (C) 2024 - 2024 张松贵, Inc. All Rights Reserved
# 故障采样段信息类，包含该段采样频率、采样点数、采样点开始位置、采样点结束位置、采样点用时、采样点结束位置、采样点原始采样值
# @FileName  :nrate.py
# @Time      :2024/07/05 13:56:30
# @Author    :张松贵
from typing import Union

from py3comtrade.model.channel_num import ChannelNum
from py3comtrade.model.nrate import Nrate
from py3comtrade.model.type.data_file_type import DataFileType


class ConfigSample:
    """
    采样信息
    """
    __freg: float  # 电网频率
    __nrate_num: int  # 采样段个数
    __nrates: list[Nrate]  # 采样段列表
    __count: int = 0  # 总采样点数
    __data_file_type = DataFileType.BINARY  # 数据文件类型
    __analog_word: int = 2
    __digital_word: int = 2
    __analog_sampe_word: int = 2  # 每采样点模拟量占用的字节数
    __digital_sampe_word: int = 2  # 每采样点开关量占用的字节数
    __total_sampe_word: int = 8  # 每采样点占用的字节数
    __channel_num: ChannelNum = None

    def __init__(
            self,
            freg: Union[float, str] = 50.00,
            nrate_num: Union[int, str] = 0,
            nrates=None
    ):
        """
        :param nrate_num: 录波文件采样段数
        :param freg: 系统频率
        """
        if nrates is None:
            nrates = []
        self.clear()
        self.__freg = freg if isinstance(freg, float) else float(freg)
        self.__nrate_num = nrate_num if isinstance(nrate_num, int) else int(nrate_num)
        self.__nrates = nrates

    def clear(self):
        self.__freg = 50.00
        self.__nrate_num = 1
        self.__nrates = []
        self.count = 0
        self.data_file_type = DataFileType.BINARY
        self.analog_sampe_word = 2
        self.digital_sampe_word = 2

    def __iter__(self):
        return iter(self.__nrates)

    def __getitem__(self, index: int):
        return self.__nrates[index]

    def __len__(self):
        return len(self.__nrates)

    def __sample_to_string(self):
        samplt_str = ""
        for nrate in self.__nrates:
            samplt_str += nrate.__str__() + "\n"
        return samplt_str

    def __str__(self):
        return f"{self.__freg}\n{str(self.nrates)}\n{self.__sample_to_string}"

    def calc_sampling(self):
        # 计算各采样段隐含信息
        for i in range(0, self.nrate_num):
            nrate: Nrate = self.nrates[i]
            nrate.index = i
            # 更新每个周波采多少个点数
            nrate.cycle_point = int(nrate.samp / self.freg)
            # 每段包含多少个采样点数
            nrate.count = (
                nrate.end_point
                if i == 0
                else nrate.end_point - self.nrates[i - 1].end_point
            )
            # 每段开始的采样点号
            nrate.start_point = 0 if i == 0 else self.nrates[i - 1].end_point

            # 计算采样段一共用了多少时间
            nrate.waste_time = int(nrate.count / nrate.cycle_point * 20)
            # 计算每个采样段结束是的时间
            nrate.end_time = (
                nrate.waste_time
                if i == 0
                else nrate.waste_time + self.nrates[i - 1].end_time
            )
        # 更新总采样点数
        self.__count = self.nrates[-1].end_point
        self.__calc_sample_words()

    def __calc_sample_words(self):
        """
        根据文件格式计算每采样点占用字节数
        """
        if self.data_file_type.BINARY32 in ("BINARY32", "FLOAT32"):
            self.analog_word = 4
        self.analog_sampe_word = self.analog_word * self.channel_num.analog_num
        self.digital_sampe_word = (self.digital_word * self.channel_num.digital_num) // 16
        self.total_sampe_word = self.analog_sampe_word + self.digital_sampe_word + 8

    def add_nrate(self, nrate: Nrate):
        """添加采样段信息"""
        self.nrates.append(nrate)

    def delete_sampling_nrate(self, index: int):
        """删除采样段信息"""
        self.nrates.pop(index)

    @property
    def count(self):
        """总采样点数"""
        return self.__count

    @count.setter
    def count(self, value):
        """设置总采样点数"""
        self.__count = value

    @property
    def freg(self):
        """电网频率"""
        return self.__freg

    @freg.setter
    def freg(self, value):
        """
        系统频率
        """
        self.__freg = value

    @property
    def nrate_num(self):
        """采样段个数"""
        return self.__nrate_num

    @nrate_num.setter
    def nrate_num(self, value):
        """
        采样段个数
        """
        self.__nrate_num = value

    @property
    def nrates(self):
        """
        采样段列表
        """
        return self.__nrates

    @nrates.setter
    def nrates(self, value):
        """
        采样段列表
        """
        self.__nrates = value

    @property
    def data_file_type(self):
        """数据文件类型"""
        return self.__data_file_type

    @data_file_type.setter
    def data_file_type(self, value: DataFileType):
        """数据文件类型"""
        self.__data_file_type = value
        if value in [DataFileType.BINARY32, DataFileType.FLOAT32]:
            self.analog_sampe_word = 4

    @property
    def analog_word(self):
        """模拟量字数"""
        return self.__analog_word

    @analog_word.setter
    def analog_word(self, value: int):
        """模拟量字数"""
        self.__analog_word = value

    @property
    def digital_word(self):
        """开关量字数"""
        return self.__digital_word

    @digital_word.setter
    def digital_word(self, value: int):
        """开关量字数"""
        self.__digital_word = value

    @property
    def analog_sampe_word(self):
        """每采样点模拟采样点占用的字节数"""
        return self.__analog_sampe_word

    @analog_sampe_word.setter
    def analog_sampe_word(self, value: int):
        """每采样点模拟采样点占用的字节数"""
        self.__analog_sampe_word = value

    @property
    def digital_sampe_word(self):
        """每采样点开关量占用的字节数"""
        return self.__digital_sampe_word

    @digital_sampe_word.setter
    def digital_sampe_word(self, value: int):
        """每采样点开关量占用的字节数"""
        self.__digital_sampe_word = value

    @property
    def total_sampe_word(self):
        """每采样点总字节数"""
        return self.__total_sampe_word

    @total_sampe_word.setter
    def total_sampe_word(self, value: int):
        """每采样点总字节数"""
        self.__total_sampe_word = value

    @property
    def channel_num(self):
        return self.__channel_num

    @channel_num.setter
    def channel_num(self, value: ChannelNum):
        self.__channel_num = value
