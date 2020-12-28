# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: page_index_openfile.py
from base.base_web import BaseWeb
from time import sleep
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageIndexOpenFile(BaseWeb):
    # 文档标题
    document_title = None
    document_author = None

    # 点击打开文件logo
    def page_click_openfile(self):
        sleep(2)
        self.base_click(page.index_openfile_logo)

    # 点击打开文件选项
    def page_click_switch_openfile(self):
        sleep(2)
        self.base_click(page.index_openfile_switch)

    # 点击打开本地文件
    def page_click_local_openfile(self):
        sleep(2)
        self.base_click(page.index_openfile_local)

    # 点击打开网络文件
    def page_click_online_openfile(self):
        sleep(2)
        self.base_click(page.index_openfile_online)

    # 输入文档路径
    def page_write_filedir(self, filedir):
        self.system_write(filedir)

    # 输入网络文件路径
    def page_write_fileurl(self, fileurl):
        self.base_input(page.index_online_url, fileurl)

    # 点击网络文件路径输入框确定按钮
    def page_click_online_button(self):
        self.base_click(page.index_online_button)

    # 点击回车按键
    def page_press_enter(self):
        self.system_press(page.press_enter)

    # 右键单击页面中心
    def page_click_screen_centre(self):
        self.system_click(page.screen_x, page.screen_y, page.click_one, page.click_right)

    # 点击打开文档信息
    def page_click_document_info(self):
        self.base_click(page.index_document_info)

    # 获取文档信息-标题
    def page_get_document_info_title(self):
        return self.base_get_text(page.index_document_info_title)

    # 获取文档信息-作者
    def page_get_document_info_author(self):
        return self.base_get_text(page.index_document_info_author)

    # 打开文档组合业务方法(点击logo)
    def page_index_openfile(self, filedir):
        log.info("正在调用打开文档组合业务方法(点击logo),路径为:{}".format(filedir))
        self.page_click_openfile()
        self.page_write_filedir(filedir)
        self.page_press_enter()

    # 打开文档组合业务方法(点击本地文件)
    def page_index_loacl_openfile(self, filedir):
        log.info("正在调用打开文档组合业务方法(点击本地文件),路径为:{}".format(filedir))
        self.page_click_switch_openfile()
        self.page_click_local_openfile()
        self.page_write_filedir(filedir)
        self.page_press_enter()

    # 打开文档组合业务方法(点击网络文件)
    def page_index_online_openfile(self, fileurl):
        log.info("正在调用打开文档组合业务方法(点击网络文件),URL为:{}".format(fileurl))
        self.page_click_switch_openfile()
        self.page_click_online_openfile()
        self.page_write_fileurl(fileurl)
        self.page_click_online_button()

    # 查看文档信息组合业务方法
    def page_index_get_document_info(self):
        log.info("正在调用查看文档信息组合业务方法")
        self.page_click_screen_centre()
        self.page_click_document_info()

    # 审核文档标题组合业务方法
    def page_index_get_filetitle(self):
        log.info("正在调用审核文档标题组合业务方法")
        # 提取文档标题的值给document_title
        self.document_title = self.page_get_document_info_title()
        log.info("所打开文档的标题为:{}".format(self.document_title))
        return self.document_title

    # 审核文档作者组合业务方法
    def page_index_get_fileauthor(self):
        log.info("正在调用审核文档作者组合业务方法")
        # 提取文档标题的值给document_author
        self.document_author = self.page_get_document_info_author()
        log.info("所打开文档的作者为:{}".format(self.document_author))
        return self.document_author