#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from enum import Enum

from py3comtrade.model.configure import Configure
from py3comtrade.reader.config_reader import config_reader
from py3comtrade.reader.data_reader import DataReader


class ReadFileMode(Enum):
    FULL = (0, "comtrade所有文件")
    CFG = (1, "仅读取cfg文件")
    DAT = (2, "读取cfg和dat文件")
    DMF = (3, "读取cfg和dmf文件")


def parse_file_path(file_path):
    try:
        # 规范化路径大小写
        normalized_path = os.path.abspath(os.path.normcase(file_path))

        # 获取目录路径
        dir_path = os.path.dirname(normalized_path)

        # 获取文件名（包括后缀）
        _file_name = os.path.basename(normalized_path)

        # 分离文件名和后缀
        name, ext = os.path.splitext(_file_name)
        if ext in ["CFG", "DAT", "DMF"]:
            cfg_path = os.path.join(dir_path, f"{name}.CFG")
            dat_path = os.path.join(dir_path, f"{name}.DAT")
            dmf_path = os.path.join(dir_path, f"{name}.DMF")
        else:
            cfg_path = os.path.join(dir_path, f"{name}.cfg")
            dat_path = os.path.join(dir_path, f"{name}.dat")
            dmf_path = os.path.join(dir_path, f"{name}.dmf")

        return {
            "cfg_path": cfg_path if os.path.exists(cfg_path) else None,
            "dat_path": dat_path if os.path.exists(dat_path) else None,
            "dmf_path": dmf_path if os.path.exists(dmf_path) else None
        }
    except (TypeError, ValueError) as e:
        print(f"文件名解析失败!!!", e)
        return {
            "cfg_path": None,
            "dat_path": None,
            "dmf_path": None
        }


class ComtradeReader:
    """
    Comtrade文件解析器，解析cfg和dat文件，返回Comtrade对象
    """
    __comtrade_files = None
    __read_mode: ReadFileMode = ReadFileMode.CFG
    __configure: Configure = None
    __data: DataReader = None

    def __init__(self, _file_name: str, read_mode: ReadFileMode = ReadFileMode.CFG):
        self.__comtrade_files = parse_file_path(_file_name)
        self.__read_mode = read_mode
        self.read_file()

    def clear(self):
        __comtrade_files = None
        __read_mode: ReadFileMode = ReadFileMode.CFG
        self.__configure.clear()
        self.__data.clear()

    def read_file(self):
        self.read_cfg_file()
        if self.__read_mode in [ReadFileMode.DAT, ReadFileMode.FULL]:
            self.read_dat_file()
        if self.__read_mode in [ReadFileMode.DMF, ReadFileMode.FULL]:
            pass

    def read_cfg_file(self):
        if os.path.exists(_cfg_path := self.__comtrade_files.get("cfg_path")):
            self.__configure: Configure = config_reader(_cfg_path)
        else:
            raise FileNotFoundError("未找到cfg文件!!!")

    def read_dat_file(self):
        if os.path.exists(_dat_path := self.__comtrade_files.get("dat_path")):
            self.__data: DataReader = DataReader(_dat_path, self.__configure.sample)
            self.__data.read_file()
        else:
            raise FileNotFoundError("未找到dat文件!!!")

    def read_dmf_file(self):
        pass

    @property
    def read_mode(self):
        return self.__read_mode

    @property
    def configure(self):
        return self.__configure

    @property
    def data(self):
        return self.__data


if __name__ == '__main__':
    file_name = r'D:\codeArea\gitee\comtradeOfPython\tests\data\xtz'
    comtrade = ComtradeReader(file_name, ReadFileMode.CFG)
    comtrade.read_file()
    comtrade.read_dat_file()
    print(comtrade.configure.header.version)
