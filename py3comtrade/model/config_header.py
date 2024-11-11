#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import Union


class ConfigHeader:
    """
    cfg文件头部信息，变电站名称，录波设备名称和录波格式版本号
    """

    __station_name: str
    __recorder_name: str
    __version: int

    def __init__(self, station_name: str, recorder_name: str, version: Union[str, int] = 1991):
        """
        cfg文件头部信息，变电站名称，录波设备名称和录波格式版本号
        :param station_name: 变电站名称
        :param recorder_name: 录波设备名称
        :param version: 录波格式版本号
        """
        self.__station_name = station_name
        self.__recorder_name = recorder_name
        if isinstance(version, int):
            self.__version = int(version)
        self.__version = version

    def clear(self):
        self.__station_name = ""
        self.__recorder_name = ""
        self.__version = 1991

    def __str__(self):
        return f"{self.station_name},{self.recorder_name},{self.version}"

    @property
    def station_name(self) -> str:
        return self.__station_name

    @station_name.setter
    def station_name(self, value: str) -> None:
        self.__station_name = value

    @property
    def recorder_name(self) -> str:
        return self.__recorder_name

    @recorder_name.setter
    def recorder_name(self, value: str) -> None:
        self.__recorder_name = value

    @property
    def version(self) -> int:
        return self.__version

    @version.setter
    def version(self, value: Union[str, int]) -> None:
        if isinstance(value, int):
            self.__version = int(value)
        self.__version = value
