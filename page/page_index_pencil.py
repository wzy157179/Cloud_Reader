# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: page_index_pencil.py
from base.base_web import BaseWeb
from time import sleep
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageIndexPencil(BaseWeb):
    # 点击铅笔按钮
    def page_click_pencil(self):
        sleep(2)
        self.base_click(page.index_pencil_button)

    # 使用铅笔绘画01
    def page_draw_pencil_01(self):
        self.system_draw_01(page.draw_x, page.draw_y)

    # 使用铅笔绘画01
    def page_draw_pencil_02(self):
        self.system_draw_02(page.draw_x, page.draw_y)

    # 点击手型按钮
    def page_click_hand(self):
        self.base_click(page.index_hand_button)

    # 右键点击选定绘画内容01
    def page_click_draw_01(self):
        self.system_click(page.draw_x, page.draw_y, page.click_one, page.click_right)

    # 右键点击选定绘画内容02
    def page_click_draw_02(self):
        self.system_click(page.draw_x + 50, page.draw_y + 50, page.click_one, page.click_right)

    # 删除绘画内容
    def page_delete_draw(self):
        self.base_click(page.index_delete_pencil_button)

    # 铅笔属性按钮
    def page_property_pencil(self):
        self.base_click(page.index_property_pencil_button)

    # 选择黄色铅笔属性
    def page_property_yellow_pencil(self):
        self.base_click(page.index_yellow_pencil_button)

    # 设置当前属性为默认
    def page_property_default_pencil(self):
        self.base_click(page.index_default_pencil_button)

    # 点击关闭铅笔属性按钮
    def page_property_close_pencil(self):
        self.base_click(page.index_close_property_pencil_button)

    # 铅笔绘画组合方法
    def page_index_draw_pencil(self):
        log.info("铅笔绘画组合方法")
        self.page_click_pencil()
        self.page_draw_pencil_01()
        log.info("铅笔绘画组合方法完成")

    # 绘画删除组合方法
    def page_index_delete_draw_pencil(self):
        log.info("铅笔绘画删除组合方法")
        self.page_click_hand()
        self.page_click_draw_01()
        self.page_delete_draw()
        log.info("铅笔绘画删除组合方法完成")

    # 铅笔默认属性更改组合方法
    def page_index_property_pencil(self):
        log.info("铅笔默认属性更改组合方法")
        self.page_click_draw_02()
        self.page_property_pencil()
        self.page_property_yellow_pencil()
        self.page_property_default_pencil()
        self.page_property_close_pencil()
        self.page_click_pencil()
        self.page_draw_pencil_02()
        log.info("铅笔默认属性更改组合方法")
