#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from py3comtrade.cfg.config_reader import config_reader


class TestConfigReader(unittest.TestCase):

    def setUp(self):
        file_name = r'../data/xtz.cfg'
        self.xtz = config_reader(file_name)

    def test_cursor_point_in_segment(self):
        segment_index = self.xtz.get_cursor_in_segment(1)
        self.assertEqual(0, segment_index)

    def test_get_point_between_segment(self):
        segments = self.xtz.get_point_between_segment(1200, 2700)
        self.assertEqual(3, len(segments))

    def test_equal_point_samp_rate(self):
        self.assertTrue(self.xtz.equal_point_samp_rate(0, 1))
        self.assertFalse(self.xtz.equal_point_samp_rate(1200, 1300))
        self.assertTrue(self.xtz.equal_point_samp_rate(1200, 2700))

    def test_get_cursor_cycle_point(self):
        self.assertEqual(64, self.xtz.get_cursor_cycle_point(1))
        self.assertEqual(64, self.xtz.get_cursor_cycle_point(2780))

    def test_get_analog_by_index(self):
        analog = self.xtz.get_analog_by_index(0)
        self.assertEqual('220kV母线I_Ua', analog.name)

    def test_get_digital_by_index(self):
        digital = self.xtz.get_digital_by_index(0)
        self.assertEqual('220kV母线_保护一_Ⅰ母差动动作', digital.name)

    def test_get_header(self):
        self.assertEqual('xtz', self.xtz.header.station_name)

    def test_get_channel_num(self):
        self.assertEqual(48, self.xtz.channel_num.analog_num)
        self.assertEqual(96, self.xtz.channel_num.digital_num)
        self.assertEqual(144, self.xtz.channel_num.total_num)
        # self.assertEqual(48, len(self.xtz.analogs))
        # self.assertEqual(96, len(self.xtz.digitals))

    def test_get_sample_info(self):
        self.assertEqual(3077, self.xtz.sample.count)

    def test_get_fault_time(self):
        self.assertEqual(803774, self.xtz.fault_time.time.microsecond)
        self.assertEqual(603838, self.xtz.file_start_time.time.microsecond)

    def test_get_data_file_type(self):
        self.assertEqual('BINARY', self.xtz.sample.data_file_type.name)
