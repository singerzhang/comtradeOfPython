#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.analog import Analog
from py3comtrade.model.channel_num import ChannelNum
from py3comtrade.model.config_header import ConfigHeader
from py3comtrade.model.config_sample import ConfigSample
from py3comtrade.model.digital import Digital
from py3comtrade.model.nrate import Nrate
from py3comtrade.model.precision_time import PrecisionTime
from py3comtrade.model.timemult import TimeMult


class Configure:
    """
    配置文件类，用于存储配置文件信息
    """

    __header: ConfigHeader
    __channel_num: ChannelNum
    __analogs: list[Analog] = []
    __digitals: list[Digital] = []
    __sample: ConfigSample = ConfigSample()
    __file_start_time: PrecisionTime
    __fault_time: PrecisionTime
    __timemult: TimeMult

    def __init__(self, file_path):
        self.__file_path = file_path

    def clear(self):
        self.header.clear()
        self.channel_num.clear()
        self.analogs = []
        self.digitals = []
        self.sample.clear()
        self.file_start_time.clear()
        self.fault_time.clear()
        self.timemult.clear()

    def get_cursor_in_segment(self, cursor_site: int) -> int:
        """
        获取游标位置所在的采样段
        :param cursor_site: 游标采样点位置
        :return: 游标位置所在的采样段,当采样点位置传入错误是返回-1
        """
        for nrate in self.sample.nrates:
            if nrate.start_point <= cursor_site <= nrate.end_point:
                return nrate.index
        return -1

    def get_point_between_segment(self, point1: int, point2: int) -> list[Nrate]:
        """
        获取两个点之间的采样段
        :param point1: 点1
        :param point2: 点2
        :return: 采样段列表
        """
        point1_segment = self.get_cursor_in_segment(point1)
        point2_segment = self.get_cursor_in_segment(point2)
        return self.sample.nrates[point1_segment:point2_segment + 1]

    def equal_point_samp_rate(self, point1: int, point2: int) -> bool:
        """
        判断两个点之间是否是相同的采样率
        :param point1: 点1
        :param point2: 点2
        :return: True:是相同的采样率,False:不是相同的采样率
        """
        segments = self.get_point_between_segment(point1, point2)
        if segments[0].samp == segments[-1].samp:
            return True
        return False

    def get_cursor_cycle_point(self, cursor_site: int) -> int:
        """
        获取游标位置的每周波采样点数
        :param cursor_site: 游标采样点位置
        :return: 游标位置每周波采样点数,当采样点位置传入错误是返回-1
        """
        for nrate in self.sample:
            if nrate.start_point <= cursor_site <= nrate.end_point:
                return nrate.cycle_point
        return -1

    def get_analog_by_index(self, index: int) -> Analog:
        """
        根据索引获取模拟量
        :param index: 索引
        :return: 模拟量对象
        """
        return self.analogs[index]

    def get_digital_by_index(self, index: int) -> Digital:
        """
        根据索引获取开关量
        :param index: 索引
        :return: 开关量对象
        """
        return self.digitals[index]

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, value):
        self.__header = value

    @property
    def channel_num(self):
        return self.__channel_num

    @channel_num.setter
    def channel_num(self, value):
        self.__channel_num = value

    @property
    def analogs(self):
        return self.__analogs

    @analogs.setter
    def analogs(self, value):
        self.__analogs = value

    def add_analog(self, analog: Analog):
        """
        添加模拟量
        """
        if self.analogs is None and analog.index != 1:
            self.header.analog_first_index = analog.index
        self.__analogs.append(analog)

    @property
    def digitals(self):
        return self.__digitals

    @digitals.setter
    def digitals(self, value):
        self.__digitals = value

    def add_digital(self, digital: Digital):
        """
        添加开关量
        """
        if self.digitals is None and digital.index != 1:
            self.header.digital_first_index = digital.index
        self.__digitals.append(digital)

    @property
    def sample(self):
        return self.__sample

    @sample.setter
    def sample(self, value):
        self.__sample = value

    @property
    def file_start_time(self):
        return self.__file_start_time

    @file_start_time.setter
    def file_start_time(self, value):
        self.__file_start_time = value

    @property
    def fault_time(self):
        return self.__fault_time

    @fault_time.setter
    def fault_time(self, value):
        self.__fault_time = value

    @property
    def timemult(self):
        return self.__timemult

    @timemult.setter
    def timemult(self, value):
        self.__timemult = value.strip()
