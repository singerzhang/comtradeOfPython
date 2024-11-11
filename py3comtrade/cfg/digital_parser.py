#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.digital import Digital
from py3comtrade.type.phase_code import PhaseCode


def digital_parser(line):
    line = line.strip().split(",")
    index = line[0]
    name = line[1]
    phase = PhaseCode.from_string(line[2])
    ccbm = line[3]
    status = line[4]
    return Digital(index, name, phase, ccbm, status)
