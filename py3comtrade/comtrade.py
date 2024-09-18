#!/usr/bin/python3
# _*_ coding: utf-8 _*_
#
# Copyright (C) 2024 - 2024 张松贵, Inc. All Rights Reserved
#
# @Time    : 2024/3/23 11:27
# @Author  : 张松贵
# @File    : comtrade.py
# @IDE     : PyCharm
from py3comtrade.entity.cfg import Cfg
from py3comtrade.entity.comtrade import Comtrade as BaseComtrade
from py3comtrade.entity.dat import Dat
from py3comtrade.parser.cfg_parser import CfgParser
from py3comtrade.parser.dat_parser import DatParser
from py3comtrade.parser.dmf_parser import DmfParser
from py3comtrade.utils import file_tools


class Comtrade(BaseComtrade):
    """
    comtrade文件解析类
    """

    def __init__(self, _cfg_file_name: str, _dat_file_name: str = None, _dmf_file_name: str = None):
        """
        comtrade文件读取初始化
        :param _cfg_file_name: cfg文件名带后缀名,
        :param _dat_file_name: dat文件名带后缀名，当该文件为空时和cfg文件名相同，后缀大小写保持一致
        :param _dmf_file_name: dmf文件名带后缀名，当该文件为空时和cfg文件名相同，后缀大小写保持一致
        """

        self.clear()
        self._load_comtrade_file(_cfg_file_name, _dat_file_name)
        self._cfg: Cfg
        self._dat: Dat
        super().__init__(self._cfg, self._dat)

    def clear(self):
        """
        清除类内部的私有变量
        @return:
        """
        self._cfg = None
        self._dat = None
        super().clear()

    def _load_comtrade_file(self, _cfg_file_name: str, _dat_file_name: str = None):
        """
        判断是否存在cfg和dat文件
        :param _cfg_file_name: cfg文件名，不含后缀
        :param _dat_file_name: dat文件名，不含后缀
        """
        # 判断cfg文件存在且不为空，进行解析CFG文件
        if file_tools.verify_file_validity(_cfg_file_name):
            self._cfg = CfgParser(_cfg_file_name).cfg
        # 当dat文件为空，则取cfg文件名，后缀名大小写和cfg一致
        if _dat_file_name is None:
            _name, _suffix = _cfg_file_name.rsplit('.', 1)
            _dat_suffix = 'dat' if _suffix == 'cfg' else 'DAT'
            _dat_file_name = _name + '.' + _dat_suffix
        # 判断dat文件存在且不为空，进行解析DAT文件
        if file_tools.verify_file_validity(_dat_file_name):
            self._dat = DatParser(_dat_file_name, self._cfg.fault_header, self._cfg.sample_info).dat

    def _load_dmf_file(self, _dmf_file_name: str):
        """
        判断是否存在dmf文件
        :param _dmf_file_name: dmf文件名，含后缀
        """
        if not file_tools.verify_file_validity(_dmf_file_name):
            self.dmf = DmfParser(_dmf_file_name)


if __name__ == '__main__':
    file = r'../tests/data/xtz.cfg'
    ch_numbers = [1, 2, 3, 4]
    record = Comtrade(file)
    print(record.fault_header.station_name)
    stl = record.get_sample_time_lists()
    analog_channels = [record.cfg.get_analog_obj(i) for i in ch_numbers]
    ssz = record.get_analog_ssz(analog_channels)
    print(stl.shape)
