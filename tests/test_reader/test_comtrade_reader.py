#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from py3comtrade.comtrade import Comtrade
from py3comtrade.reader import ReadFileMode


class TestComtrade(unittest.TestCase):

    def setUp(self):
        file_nme = r'../data/xtz.dat'
        self.comtrade = Comtrade(file_nme)
        self.comtrade.read(read_mode=ReadFileMode.CFG)

    def test_read(self):
        self.assertIsNotNone(self.comtrade.cfg)
        self.assertIsNone(self.comtrade.dat)
        self.comtrade.read(ReadFileMode.DAT)
        self.assertIsNotNone(self.comtrade.dat)

    def test_get_ysz_by_analog(self):
        self.comtrade.read(ReadFileMode.DAT)
        ch1_ysz = self.comtrade.get_raw_samples_by_index(1, 0, 3077)
        self.assertEqual(3077, len(ch1_ysz[0]))
        ch2_ysz = self.comtrade.get_raw_samples_by_index(2)
        self.assertEqual(3077, len(ch2_ysz[0]))

    def test_get_ssz_by_analog(self):
        self.comtrade.read(ReadFileMode.DAT)
        analog = self.comtrade.cfg.get_analog_by_an(1)
        ch1_ssz = self.comtrade.get_instant_samples_by_analog(analog, primary=False)
        self.assertEqual(-84.691, ch1_ssz[0][0])
        self.assertEqual(65.465, ch1_ssz[0][602])
        self.assertEqual(85.316, ch1_ssz[0][1282])

        analog = self.comtrade.cfg.get_analog_by_an(11)
        ch11_ssz = self.comtrade.get_instant_samples_by_analog(analog, primary=False)
        self.assertEqual(0.136, ch11_ssz[0][0])
        self.assertEqual(0.327, ch11_ssz[0][600])
        self.assertEqual(0.682, ch11_ssz[0][1281])
