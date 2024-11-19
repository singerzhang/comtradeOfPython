#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import struct

import numpy as np
import pandas as pd

from py3comtrade.model.config_sample import ConfigSample
from py3comtrade.model.type.data_file_type import DataFileType
from py3comtrade.reader.config_reader import config_reader


def digital_split(datas: tuple) -> list:
    """
    将开关量整数数组拆分成数组
    :return: data
    """
    digitals = []
    for data in datas:
        binary_array = [(data >> i) & 1 for i in range(15, -1, -1)]
        binary_array.reverse()
        digitals.extend(binary_array)
    return digitals


class DataReader:
    """
    读取文件
    """

    def __init__(self, file_path, sample: ConfigSample):
        self.__file_path = file_path
        self.__sample = sample
        self.__size = os.path.getsize(self.file_path)
        self.__sample_time: np.ndarray = np.zeros((self.sample.count, 2), dtype=np.int32)
        self.__analog_value: np.ndarray = np.zeros((self.sample.count, self.sample.channel_num.analog_num),
                                                   dtype=np.float32)
        self.__digital_value: np.ndarray = np.zeros((self.sample.count, self.sample.channel_num.digital_num),
                                                    dtype=np.int32)

    def clear(self):
        self.__file_path = None
        self.__sample = None
        self.size = 0
        self.__sample_time = np.zeros((self.sample.count, 2), dtype=np.int32)
        self.__analog_value = np.zeros((self.sample.count, self.sample.channel_num.analog_num), dtype=np.float32)
        self.__digital_value = np.zeros((self.sample.count, self.sample.channel_num.digital_num), dtype=np.int32)

    def read_file(self):
        if DataFileType.ASCII == self.sample.data_file_type.value:
            self.read_ascii()
        else:
            self.read_binary()

    def read_ascii(self):
        with open(self.file_path, 'r') as f:
            content = pd.read_csv(f, header=None)
        self.sample_time = content[:, 0:2]
        self.analog_value = content[:, 2:self.sample.channel_num.analog_num + 2]
        self.digital_value = content[:, self.sample.channel_num.analog_num + 2:]

    def read_binary(self):
        str_struct = f"ii{self.sample.analog_sampe_word // 2}h{self.sample.digital_sampe_word // 2}H"
        with open(self.file_path, 'rb') as f:
            # if self.size != (self.sample.total_sampe_word + self.sample.digital_sampe_word) * self.sample.count:
            #     raise ValueError("文件长度错误")
            for i in range(self.sample.count):
                byte_str = f.read(self.sample.total_sampe_word)
                if len(byte_str) != self.sample.total_sampe_word:
                    raise ValueError("文件长度不足")
                sample_struct = struct.unpack(str_struct, byte_str)
                self.sample_time[i:] = sample_struct[0:2]
                self.analog_value[i:] = sample_struct[2:2 + self.sample.channel_num.analog_num]
                self.digital_value[i:] = digital_split(sample_struct[2 + self.sample.channel_num.analog_num:])

    @property
    def sample(self):
        return self.__sample

    @property
    def file_path(self):
        return self.__file_path

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def analog_value(self) -> np.ndarray:
        return self.__analog_value

    @analog_value.setter
    def analog_value(self, value: np.ndarray):
        self.__analog_value = value

    @property
    def digital_value(self) -> np.ndarray:
        return self.__digital_value

    @digital_value.setter
    def digital_value(self, value: np.ndarray):
        self.__digital_value = value

    @property
    def sample_time(self) -> np.ndarray:
        return self.__sample_time

    @sample_time.setter
    def sample_time(self, value: np.ndarray):
        self.__sample_time = value


if __name__ == '__main__':
    cfg_file_name = r'/tests/data/xtz.cfg'
    dat_file_name = r'/tests/data/xtz.dat'
    configure = config_reader(cfg_file_name)
    dat_content = DataReader(dat_file_name, configure.sample)
    dat_content.read_file()
    print('解析完毕')
