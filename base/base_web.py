# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: base_web.py
from time import sleep
import pyautogui
from selenium.webdriver.common.by import By
import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class BaseWeb(Base):
    # 1. 下拉框定位
    def base_web_select_input_ul(self, click_text, placeholder_value):
        # 1. 定位input 注意：{}需要在单引号中
        loc = By.CSS_SELECTOR, "[placeholder='{}']".format(placeholder_value)
        log.info("正在准备点击：{} 元素！".format(loc))
        self.base_click(loc)
        log.info("{} 元素，执行点击完毕！".format(loc))
        # 2. 暂停1秒
        sleep(1)
        # 3. 定位具体文本
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        log.info("正在准备点击：{} 元素！".format(loc))
        self.base_click(loc)
        log.info("{} 元素，执行点击完毕！".format(loc))

    # 判断当前页面是否包含指定字符串元素
    def base_if_text_exists_element(self, text):
        # 1. 组合文本元素定位信息
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            log.info("正在准备查找：{}元素".format(loc))
            # 查找元素 建议：将查找时间修改为5秒内，避免找不到，等待30秒
            self.base_find(loc, timeout=5)
            log.info("找到包含:{}文本的元素啦！".format(text))
            print("找到包含:{}文本的元素啦！".format(text))
            # 返回True  代表存在
            return True
        except False:
            print("没有找到，包含：{}文本的元素！".format(text))
            log.info("没有找到，包含：{}文本的元素！".format(text))
            # 返回False 代表不存在
            return False

    # 选取一段区域
    def system_dragto(self, x1, x2, y, button, isselect=0):
        # 1. 点击要选取的行首
        log.info("正在点击要选定的行首,坐标为:{}{}".format(x1, y))
        pyautogui.click(x1, y, duration=0.5)
        # 2. 拖拽鼠标选取内容
        log.info("正在进行拖拽操作,向{}拖拽到的坐标为:{}{}".format(button, x2, y))
        pyautogui.dragTo(x2, y, duration=0.5, button=button)
        log.info("拖拽选取操作完成")
        # 3. 是否选定文本
        log.info("是否选择文本:{}".format(isselect))
        if isselect == 0:
            self.system_click(x1, y, page.click_one, page.click_right)
        elif isselect == 1:
            return
        else:
            print("参数错误, 参数为0选择文本, 参数为1不选择文本, 请按要求输入")
