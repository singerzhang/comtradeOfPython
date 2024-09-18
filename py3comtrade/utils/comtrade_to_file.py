#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 张松贵, Inc. All Rights Reserved 
#
# @Time    : 2024/9/18 下午10:31
# @Author  : 张松贵
# @File    : comtrade_to_file.py
# @IDE     : PyCharm
import numpy as np
import pandas as pd

from py3comtrade.comtrade import Comtrade
from py3comtrade.entity.analog_channel import AnalogChannel


class ComtradeToFile(Comtrade):
    def __init__(self, _cfg_file_name: str, _dat_file_name: str = None, _dmf_file_name: str = None):
        super().__init__(_cfg_file_name, _dat_file_name, _dmf_file_name)

    def get_analog_channels(self, ch_numbers: list) -> list[AnalogChannel]:
        analog_channels = [self.cfg.get_analog_obj(i) for i in ch_numbers]
        return analog_channels

    def get_analog_ssz(self, ch_numbers: list):
        analog_channels = self.get_analog_channels(ch_numbers)
        ssz = self.get_analog_ssz(analog_channels)
        return ssz

    def write_to_csv_file(self, analog_channels: list[AnalogChannel], dat: np.ndarray, csv_file_path: str):
        """
        使用pandas保存文本文件的能力直接将numpy数组保存成csv格式
        :param dat: 数组对象
        :param filename: 保存的文件名，含目录、文件名和后缀
        :return:
        """
        """
        使用pandas将numpy数组保存为CSV格式文件，并从analog_channels获取一个属性值作为第一列。

        :param analog_channels: 模拟通道列表
        :param dat: 待保存的numpy数组
        :param csv_file_path: CSV文件路径
        :return: 文件生成成功的消息
        """
        # 验证输入数据
        if not isinstance(dat, np.ndarray) or dat.ndim != 2:
            raise ValueError("dat must be a 2D numpy array")

        if len(dat.shape) < 2 or dat.shape[1] < 1:
            raise ValueError("dat must have at least one column")

        if not analog_channels:
            raise ValueError("analog_channels cannot be empty")
        analog_channels.
        df = pd.DataFrame(dat)
        df[[0, 1]] = df[[0, 1]].astype(int)
        df.to_csv(csv_file_path, index=False, header=False)
        return f'{csv_file_path}文件生成成功！'


if __name__ == '__main__':
    file = r'../../tests/data/xtz.cfg'
    ch_numbers = [1, 2, 3, 4]
    record = ComtradeToFile(file)
    record.cfg.get_analog_obj()
