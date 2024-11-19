#!/usr/bin/env python
# -*- coding: utf-8 -*-
from py3comtrade.model.configure import Configure


def generate_cfg_str(cfg_obj: Configure):
    """
    生成cfg文件字符串
    @param cfg_obj: cfg对象
    @return: cfg文件字符串
    """
    header = cfg_obj.header.__str__() + "\n"
    channel_num = cfg_obj.channel_num.__str__() + "\n"
    analog_channels_str = ''
    for ac in cfg_obj.analogs:
        analog_channels_str += ac.__str__() + '\n'
    digital_channels_str = ''
    for dc in cfg_obj.digitals:
        digital_channels_str += dc.__str__ + '\n'

    return header + channel_num + analog_channels_str + digital_channels_str


def cfg_to_file(cfg: Configure, filename: str):
    """
    将cfg文件写入文件
    :param cfg: cfg文件对象
    :param filename: 文件名
    """
    with open(filename, 'w', encoding='gbk') as f:
        f.write(generate_cfg_str(cfg))
    return f'{filename}文件生成成功！'
