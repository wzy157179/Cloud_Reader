# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: page.py
from page.page_index_openfile import PageIndexOpenFile
from page.page_index_pencil import PageIndexPencil
from page.page_index_savefile import PageIndexSavefile


class Page:
    # 初始化 driver
    def __init__(self, driver):
        self.driver = driver

    # 获取PageIndexOpenFile对象
    def page_get_PageIndexOpenFile(self):
        return PageIndexOpenFile(self.driver)

    # 获取PageIndexPencil对象
    def page_get_PageIndexPencil(self):
        return PageIndexPencil(self.driver)

    # 获取PageIndexSavefile对象
    def page_get_PageIndexSavefile(self):
        return PageIndexSavefile(self.driver)
