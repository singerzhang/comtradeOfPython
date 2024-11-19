#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.config_header import ConfigHeader


def header_parser(line):
    line = line.strip().split(",")
    return ConfigHeader(line[0], line[1], line[2])
