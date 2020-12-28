# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: test06_index_savefile.py
import pytest

import page

from page.page import Page
from tools.get_driver import GetDriver

from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestIndexSavefile:

    # 初始化
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.index_url)
        self.openfile = Page(self.driver).page_get_PageIndexOpenFile()
        self.pencil = Page(self.driver).page_get_PageIndexPencil()
        self.savefile = Page(self.driver).page_get_PageIndexSavefile()

    # 结束
    @staticmethod
    def teardown_class():
        GetDriver.close_web_driver()

    @pytest.mark.parametrize("filedir, expect", read_yaml("test06_index_savefile.yaml"))
    def test_index_savefile(self, filedir, expect):
        try:
            # 打开文档组合业务方法(点击logo)
            self.openfile.page_index_openfile(filedir)
            # 铅笔绘画组合方法
            self.pencil.page_index_draw_pencil()
            self.pencil.base_get_assert_img()
            # 保存文件组合业务方法
            message = self.savefile.page_index_savefile()
            print("message: ", message)
            assert expect == message, "断言出错, 获取的文档标题为:{}, 预期结果为:{}".format(message, expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.openfile.base_get_img()
            # 抛异常
            raise
