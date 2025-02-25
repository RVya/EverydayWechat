#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
程序运行入口
"""
from GFWeather import GFWeather

def run():
    """
    主程序入口
    :return: None
    """
    GFWeather().run()

def test_run():
    """
    运行前的测试
    :return: None
    """
    GFWeather().start_today_info(is_test=True)

if __name__ == '__main__':
    # test_run()
    run()
