# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: test05_index_pencil.py
import page

from page.page import Page
from tools.get_driver import GetDriver

from tools.get_log import GetLog

log = GetLog.get_logger()


class TestIndexPencil:

    # 初始化
    def setup_class(self):
        self.driver = GetDriver.get_web_driver(page.index_url)
        self.pencil = Page(self.driver).page_get_PageIndexPencil()

    # 结束
    @staticmethod
    def teardown_class():
        GetDriver.close_web_driver()

    def test_index_pencil(self):
        try:
            # 铅笔绘画组合方法
            self.pencil.page_index_draw_pencil()
            self.pencil.base_get_assert_img()
            # 绘画删除组合方法
            self.pencil.page_index_delete_draw_pencil()
            self.pencil.base_get_assert_img()
            # 铅笔默认属性更改
            self.pencil.page_index_property_pencil()
            self.pencil.base_get_assert_img()
        except Exception as e:
            # 日志
            log.error(e)
            # 抛异常
            raise
