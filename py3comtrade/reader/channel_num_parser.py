#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.channel_num import ChannelNum


def channel_num_parser(line):
    line = line.strip().split(",")
    return ChannelNum(line[0], line[1], line[2])
