# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: test02_index_local_openfile.py
import pytest

import page

from page.page import Page
from tools.get_driver import GetDriver

from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestIndexLocalOpenFile:

    # 初始化
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.index_url)
        self.openfile = Page(self.driver).page_get_PageIndexOpenFile()

    # 结束
    @staticmethod
    def teardown_class():
        GetDriver.close_web_driver()

    @pytest.mark.parametrize("filedir, expect", read_yaml("test02_index_local_openfile.yaml"))
    def test_index_local_openfile(self, filedir, expect):
        try:
            # 打开文档组合业务方法(点击本地文件)
            self.openfile.page_index_loacl_openfile(filedir)
            # 查看文档信息组合业务方法
            self.openfile.page_index_get_document_info()
            # 断言
            title = self.openfile.page_index_get_filetitle()
            print("title: ", title)
            assert expect == title, "断言出错, 获取的文档标题为：{}, 预期结果为：{}".format(title, expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.openfile.base_get_img()
            # 抛异常
            raise
