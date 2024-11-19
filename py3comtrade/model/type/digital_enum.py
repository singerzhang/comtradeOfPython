#!/usr/bin/env python
# -*- coding: utf-8 -*-
from enum import Enum


class DigitalType(Enum):
    RELAY = ("Relay", "保护动作出口")
    BREAKER = ("Breaker", "断路器位置")
    SWITCH = ("SWITCH", "开关位置")
    WARNING = ("WARNING", "装置告警出口")
    OTHER = ("OTHER", "其他")


class GeneralDigitalFlag(Enum):
    GENERAL = ("general", "一般开关量")


class RelayDigitalFlag(Enum):
    TR = ("Tr", "保护跳闸")
    TRPHSA = ("TrPhsA", "跳A")
    TRPHSB = ("TrPhsB", "跳B")
    TRPHSC = ("TrPhsC", "跳C")
    OPTP = ("OPTP", "三跳信号")
    RECOPCLS = ("RecOpCls", "重合闸")
    BLKREC = ("BlkRec", "永跳信号")
    PROTTX = ("ProtTx", "发信")
    PROTRV = ("ProtRv", "收信")


class BreakerDigitalFlag(Enum):
    HWJ = ("HWJ", "不分相断路器合位")
    TWJ = ("TWJ", "不分相断路器跳位")
    HWJPHSA = ("HWJPhsA", "断路器A相合位")
    HWJPHSB = ("HWJPhsB", "断路器B相合位")
    HWJPHSC = ("HWJPhsC", "断路器C相合位")
    TWJPHSA = ("TWJPhsA", "断路器A相跳位")
    TWJPHSB = ("TWJPhsB", "断路器B相跳位")
    TWJPHSC = ("TWJPhsC", "断路器C相跳位")
    HWJHIGHT = ("HWJHight", "变压器高压侧断路器合位")
    HWJMEDIUM = ("HWJMedium", "变压器中压侧断路器合位")
    HWJLOW = ("HWJLow", "变压器低压侧断路器合位")
    TWJHIGHT = ("TWJHight", "变压器高压侧断路器跳位")
    TWJMEDIUM = ("TWJMedium", "变压器中压侧断路器跳位")
    TWJLOW = ("TWJLow", "变压器低压侧断路器跳位")


class WarningDigitalFlag(Enum):
    WARNVT = ("WarnVt", "TV断线")
    WARNCT = ("WarnCt", "CT断线")
    WARNCOMM = ("WarnComm", "通道告警")
    WARNGENERAL = ("WarnGeneral", "其他告警")


class Contact(Enum):
    NORMALLYOPEN = (0, "常开节点")
    NORMALLYCLOSED = (1, "常闭节点")
