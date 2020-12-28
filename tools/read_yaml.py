# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: read_yaml.py
import os
import yaml

from config import base_path


def read_yaml(filename):
    arr = []
    filepath = base_path + os.sep + "data" + os.sep + filename
    with open(filepath, "r", encoding="utf-8")as f:
        for i in yaml.safe_load(f).values():
            arr.append(tuple(i.values()))
        return arr
