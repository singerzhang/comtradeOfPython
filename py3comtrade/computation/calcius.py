#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

from py3comtrade.computation.fourier import dft_rx
from py3comtrade.utils import math_polar_rect


class Calcius:
    __instants: np.ndarray  # 瞬时值数组
    __instant: float  # 当前采样位置的瞬时值
    __phasor: complex  # 相量值
    __phasor_decay_dc: complex  # 过滤直流分量后的向量值
    __angle: float  # 角度
    __effective: float  # 有效值

    def __init__(self, value: np.ndarray):
        self.clear()
        if isinstance(value, np.ndarray) and value.ndim == 1:
            self.__instants = value
        else:
            raise ValueError("输入的瞬时值数组必须是一维非空的numpy数组")

    def clear(self):
        self.__instants = np.zeros(self.instant.shape[0])
        self.__phasor = complex(0.0, 0.0)
        self.__angle = 0.0

    def fft(self):
        fft_result = np.fft.fft(self.instant)
        freqs = np.fft.fftfreq(self.instant.shape[0], d=self.instant[1] - self.instant[0])
        fundamental_index = np.argmax(freqs >= 50)
        # 提取基波及前几次谐波的向量值
        harmonics_indices = [fundamental_index * i for i in range(1, 6)]
        harmonics_values = fft_result[harmonics_indices]

    def dft_rx(self, num_samples: int, k: int = 1):
        """
        离散傅里叶变换实部和虚部
        :param num_samples: 采样点数
        :param k: 获取的频率
        :return: 相量值，虚部和虚部元组
        """
        # 参数校验
        if not isinstance(num_samples, int) or num_samples <= 0:
            raise ValueError("采样点数num_samples必须是正整数")
        if not isinstance(k, int) or k < 0 or k >= num_samples:
            raise ValueError("频率k必须是非负整数且小于采样点数")
        # 计算中点值，明确使用二进制除法
        m = num_samples // 2
        real = 0.0
        imag = 0.0
        for i in range(num_samples):
            real += self.instant[i] * np.sin(i * k * np.pi / m)
            imag += self.instant[i] * np.cos(i * k * np.pi / m)
        real /= m
        imag /= m
        self.phasor = complex(real, imag)

    def dft_exp_decay_dc(self, sample_rate: int = None):
        """
        消除直流分量后返回对应通道的实部和虚部，需要1.5个周波的数据。
        1.[ (第三组点的实部+第二组点的虚部)/(第一组点的虚部+第二组点的实部) ] 的平方，把这个数记为a;
        2.通过第一步的运算结果a，求K1和K2，k1是 (第一组点的实部+第三组点的实部)/ (1+a):k2是(第一组点的虚部+第三组点的虚部) / (1+0).
        3.求修改后的基波分量实部和虚部，实部=第一组点的实部-k1: 虚部= 第二组点的虚部-k2
        :param sample_rate: 采样频率
        :return: 返回一个二维数组，一维是通道列表，二维是实部虚部元祖
        """
        if sample_rate is None:
            sample_rate = int(self.instant.shape[0] / 1.5)
        elif sample_rate <= 0:
            raise ValueError("采样频率sample_rate必须是正整数。")

        # 分割数组
        arr1 = self.instant[0:sample_rate]
        arr2 = self.instant[int(sample_rate / 4):int(sample_rate / 4 + sample_rate)]
        arr3 = self.instant[int(sample_rate / 2):]

        # 进行傅里叶计算，获取实部和虚部
        arr1_dft = dft_rx(arr1, sample_rate, 1)
        arr2_dft = dft_rx(arr2, sample_rate, 1)
        arr3_dft = dft_rx(arr3, sample_rate, 1)

        # 计算常数
        fz = arr3_dft.real + arr2_dft.imag
        fm = arr1_dft.imag + arr2_dft.real
        # 避免除以零
        if fm == 0:
            raise ValueError("计算中遇到除以零的情况。")

        # 计算系数
        a = np.square(fz / fm)
        k1 = (arr1_dft.real + arr3_dft.real) / (1 + a)
        k2 = (arr1_dft.imag + arr3_dft.imag) / (1 + a)
        # 计算过滤后的实部和虚部
        real = arr1_dft.real - k1
        imag = arr1_dft.imag - k2
        return complex(real, imag)

    def calc_angle(self):
        self.__angle = math_polar_rect.complex_to_polar(self.phasor)[1]

    def calc_effective(self):
        self.__effective = math_polar_rect.polar_to_complex(abs(self.phasor), 0)

    @property
    def instant(self) -> np.ndarray:
        return self.__instants

    @property
    def phasor(self) -> complex:
        return np.around(self.__phasor, 3)

    @phasor.setter
    def phasor(self, value: complex) -> None:
        self.__phasor = value
