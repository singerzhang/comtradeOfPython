import unittest

from py3comtrade.comtrade import Comtrade
from py3comtrade.reader.comtrade_reader import ReadFileMode


class TestCalcius(unittest.TestCase):
    def setUp(self):
        file_name = r"../data/xtz.cfg"
        self.record = Comtrade(file_name)
        self.record.read(ReadFileMode.DAT)

    def test_calcius(self):
        analog = self.record.cfg.get_analog_by_an(1)
        calcius = self.record.calc_channel_data(analog, site_point=0, cycle_num=1, mode=1)
        self.assertEqual(complex(-5.93, -59.897), calcius.phasor)
        self.assertEqual(60.19, calcius.effective)
        self.assertEqual(-95.654, calcius.angle)


if __name__ == '__main__':
    unittest.main()
