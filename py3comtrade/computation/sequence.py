#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np


class Sequence:

    def __init__(self):
        self.__zero: float = 0.000
        self.__negative: float = 0.000
        self.__positive: float = 0.000

    def phasor_to_sequence_by_rotate(self, pa: complex, pb: complex, pc: complex):
        """
        将相分量转化为序分量,使用旋转B、C角度进行计算
        :param pa: A相相量值
        :param pb: B相相量值
        :param pc: C相相量值
        :return: 返回该组通道的序分量值,索引0为零序分量，1为正序分量，2为负序分量
        """
        # 参数校验
        if not all(isinstance(arg, complex) for arg in [pa, pb, pc]):
            raise ValueError("所有参数必须是复数类型")

        self.positive = (pa + pb * np.exp(1j * 2 * np.pi / 3) + pc * np.exp(1j * 4 * np.pi / 3)) / 3 / np.sqrt(2.0)
        self.negative = (pa + pb * np.exp(-1j * 2 * np.pi / 3) + pc * np.exp(-1j * 4 * np.pi / 3)) / 3 / np.sqrt(
            2.0)
        self.zero = (pa + pb + pc) / 3 / np.sqrt(2.0)
        return self.positive, self.negative, self.zero

    def phasor_to_sequence_by_matrix(self, phasor_arr: np.ndarray):
        """
        将相量值转化为序分量，使用numpy矩阵
        :param phasor_arr:
        :return: 返回该组通道的序分量值,索引0为零序分量，1为正序分量，2为负序分量
        """
        if not all(isinstance(p, complex) for p in phasor_arr):
            raise ValueError("参数类型输入错误")
        a = complex(-0.5, np.sqrt(3.0) / 2.0)
        # phasor_arr = np.array([pa, pb, pc])
        # 转换矩阵，零序、正序、负序
        trans_arr = np.array([[1, 1, 1], [1, a, a * a], [1, a * a, a]])
        order_arr = np.dot(trans_arr, phasor_arr) / 3
        order_arr = order_arr / np.sqrt(2.0)
        self.positive = order_arr[0]
        self.negative = order_arr[1]
        self.zero = order_arr[2]
        return self.positive, self.negative, self.zero

    @property
    def zero(self) -> float:
        return np.around(self.__zero, 3)

    @zero.setter
    def zero(self, value: float) -> None:
        self.__zero = value

    @property
    def negative(self) -> float:
        return np.around(self.__negative, 3)

    @negative.setter
    def negative(self, value: float) -> None:
        self.__negative = value

    @property
    def positive(self) -> float:
        return np.around(self.__positive, 3)

    @positive.setter
    def positive(self, value: float) -> None:
        self.__positive = value
