# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: test04_index_pdf_openfile.py
import pytest

import page

from page.page import Page
from tools.get_driver import GetDriver

from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestIndexPdfOpenFile:

    # 初始化
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.index_url)
        self.openfile = Page(self.driver).page_get_PageIndexOpenFile()

    # 结束
    @staticmethod
    def teardown_class():
        GetDriver.close_web_driver()

    @pytest.mark.parametrize("filedir, expect", read_yaml("test04_index_pdf_openfile.yaml"))
    def test_index_online_openfile(self, filedir, expect):
        try:
            # 打开文档组合业务方法(点击logo)
            self.openfile.page_index_openfile(filedir)
            # 查看文档信息组合业务方法
            self.openfile.page_index_get_document_info()
            # 断言
            author = self.openfile.page_index_get_fileauthor()
            print("author: ", author)
            assert expect == author, "断言出错, 获取的文档作者为：{}, 预期结果为：{}".format(author, expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.openfile.base_get_img()
            # 抛异常
            raise
