# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: page_index_savefile.py
from base.base_web import BaseWeb
from time import sleep
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageIndexSavefile(BaseWeb):
    # 保存文档提示信息
    message_text = None

    # 点击保存按钮
    def page_click_savefile(self):
        sleep(2)
        self.base_click(page.index_savefile_button)

    # 点击下载按钮
    def page_click_downloadfile(self):
        self.base_click(page.index_downloadfile_button)

    # 获取保存文件提示文字
    def page_get_savefile_text(self):
        return self.base_get_text(page.index_savefile_text)

    # 保存文件组合业务方法
    def page_index_savefile(self):
        log.info("正在调用保存文件组合业务方法")
        self.page_click_savefile()
        self.message_text = self.page_get_savefile_text()
        log.info("获取到的提示信息为:{}".format(self.message_text))
        return self.message_text
