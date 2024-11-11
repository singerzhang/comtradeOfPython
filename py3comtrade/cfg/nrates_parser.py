#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.config_sample import ConfigSample
from py3comtrade.model.nrate import Nrate


def create_nrates(freg, nrate_num):
    """
    创建采样段对象
    """
    freg = float(freg.strip())
    nrate_num = int(nrate_num.strip())
    return ConfigSample(freg, nrate_num)


def create_nrate(line):
    """
    解析采样段信息
    """
    line = line.strip().split(",")
    return Nrate(int(line[0]), int(line[1]))
