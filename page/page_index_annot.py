# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: page_index_annot.py
from base.base_web import BaseWeb
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageIndexAnnot(BaseWeb):

    # 点击选择文本
    def page_click_selecttext(self):
        self.base_click(page.index_selecttext_button)

    # 点击高亮按钮
    def page_click_highligh(self):
        self.base_click(page.index_highlight_button)

    # 点击下划线按钮
    def page_click_underline(self):
        self.base_click(page.index_underline_button)

    # 点击文本选择高亮按钮
    def page_click_selecttext_highlight(self):
        self.base_click(page.index_selecttext_highlight)

    # 点击文本选择下划线按钮
    def page_click_selecttext_underline(self):
        self.base_click(page.index_selecttext_underline)

    # 点击属性按钮
    def page_click_property(self):
        self.base_click(page.index_property_pencil_button)

    # 点击删除按钮
    def page_click_delete(self):
        self.base_click(page.index_delete_pencil_button)

    # 点击高亮蓝色按钮
    def page_click_blue_highlight(self):
        self.base_click(page.index_highlight_blue_button)

    # 点击关闭属性弹窗
    def page_click_close_property(self):
        self.base_click(page.index_close_property_pencil_button)

    # 选取Sign_keyword.ofd文档第一行
    def page_drag_first_line(self):
        self.system_dragto(page.index_line_x1, page.index_line_x2, page.index_first_line_y, page.index_drag_left)

    # 选取Sign_keyword.ofd文档第二行
    def page_drag_second_line(self):
        self.system_dragto(page.index_line_x1, page.index_line_x2, page.index_second_line_y, page.index_drag_left)

    # 选取Sign_keyword.ofd文档第三行
    def page_drag_third_line(self):
        self.system_dragto(page.index_line_x1, page.index_line_x2, page.index_third_line_y, page.index_drag_left)

    # 选取Sign_keyword.ofd文档第四行
    def page_drag_fourth_line(self):
        self.system_dragto(page.index_line_x1, page.index_line_x2, page.index_fourth_line_y, page.index_drag_left)

    # 选择文本高亮组合业务方法
    def page_index_selecttext_highlight(self):
        log.info("正在执行选择文本高亮组合业务方法")
        self.page_click_selecttext()
        self.page_drag_first_line()
        self.page_click_selecttext_highlight()

    # 选择文本下划线组合业务方法
    def page_index_selecttext_underline(self):
        log.info("正在执行选择文本下划线组合业务方法")
        self.page_click_selecttext()
        self.page_drag_second_line()
        self.page_click_selecttext_underline()


