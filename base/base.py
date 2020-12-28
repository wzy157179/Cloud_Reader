# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: base.py
from time import sleep
import pyperclip
import allure
import pyautogui
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:
    # 初始化 -> 解决driver
    def __init__(self, driver):
        log.info("正在初始化driver对象： {}".format(driver))
        self.driver = driver

    # 查找元素 （暂时理解：输入、点击、获取）
    def base_find(self, loc, timeout=30, poll=0.5):
        """
        :param loc: By定位方式和对应的值 格式：列表或元祖
        :param timeout: 超时时间 默认30秒
        :param poll: 访问频率 默认0.5
        :return: 元素
        """
        log.info("正在查找：{}元素，访问频率：{} 超时时间：{}".format(loc, poll, timeout))
        # 重点：必须返回
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 参考查找元素
        :param value: 要输入的文本内容
        :return:
        """
        # 1. 获取元素
        el = self.base_find(loc)
        log.info("正在准备对：{}元素执行清空操作".format(loc))
        # 2. 清空操作
        el.clear()
        log.info("对：{}元素执行清空操作完成！".format(loc))
        log.info("正在准备对：{}元素执行输入：{} 操作".format(loc, value))
        # 3. 输入操作
        el.send_keys(value)
        log.info("对：{}元素执行输入：{} 操作完成！".format(loc, value))

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc: 为列表或元祖
        :return:
        """
        log.info("正在准备对：{}元素执行点击操作".format(loc))
        self.base_find(loc).click()
        log.info("对：{}元素执行点击操作完成".format(loc))

    # 获取 文本方法
    def base_get_text(self, loc):
        """
        :param loc: 为列表或元祖
        :return: 元素的文本值
        """

        log.info("正在对:{}元素获取文本操作, 获取的文本值：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc, poll=0.1).text

    # error截图
    def base_get_img(self):
        log.error("错误！，正在截图操作")
        # 1. 调用截图api
        self.driver.get_screenshot_as_file("./image/error.png")
        # 2. 将图片写入报告
        self.__write_img_report()

    # 将图片写入allure报告
    @staticmethod
    def __write_img_report():
        log.error("错误！，正在将图片写入报告操作")
        allure.attach.file(r"./image/error.png", 'error截图', attachment_type=allure.attachment_type.JPG)
        assert 1

    # 截图
    def base_get_assert_img(self):
        log.info("正在截图操作")
        # 1. 调用截图api
        self.driver.get_screenshot_as_file("./image/screenshot.png")
        # 2. 将图片写入报告
        self.__write_assert_report()

    # 将图片写入allure报告
    @staticmethod
    def __write_assert_report():
        log.info("正在将图片写入报告操作")
        allure.attach.file(r"./image/screenshot.png", '截图', attachment_type=allure.attachment_type.JPG)
        assert 1

    # 系统输入操作
    @staticmethod
    def system_write(value):
        """
        :param value: 要输入的文本内容
        :return:
        """
        sleep(3)
        log.info("正在准备对系统输入：{} 操作".format(value))
        # 输入操作
        pyperclip.copy(value)
        pyautogui.hotkey('ctrl', 'v')
        log.info("对系统输入：{} 操作完成！".format(value))

    # 系统按键操作
    @staticmethod
    def system_press(key):
        """
        :param key: 点击按键
        :return:
        """
        sleep(2)
        log.info("正在准备对系统进行点击：{} 按键操作".format(key))
        pyautogui.press(key)
        log.info("对系统进行点击：{} 按键操作完成！".format(key))

    # 系统点击操作
    @staticmethod
    def system_click(x, y, click, button):
        """
        :param x: 点击操作的X坐标
        :param y: 点击操作的Y坐标
        :param click: 点击次数
        :param button: 点击按键
        :return:
        """
        sleep(5)
        log.info("正在准备进行对坐标({},{}){}键{}此点击操作".format(x, y, click, button))
        # 点击操作
        pyautogui.click(x=x, y=y, clicks=click, button=button)
        log.info("进行对坐标({},{}){}键{}此点击操作完成！".format(x, y, click, button))

    # 绘图01
    @staticmethod
    def system_draw_01(x, y):
        """
        :param x: 绘画初始x坐标
        :param y: 绘画初始y坐标
        :return:
        """
        # 移动画笔初始位置
        pyautogui.moveTo(x=x, y=y, duration=0)
        sleep(0.5)
        distance = 300
        while distance > 0:
            # 进行绘画操作
            pyautogui.dragRel(distance, 0, duration=0.1)
            distance = distance - 50
            pyautogui.dragRel(0, distance, duration=0.1)
            pyautogui.dragRel(-distance, 0, duration=0.1)
            distance = distance - 50
            pyautogui.dragRel(0, -distance, duration=0.1)

    # 绘图02
    @staticmethod
    def system_draw_02(x, y):
        """
        :param x: 绘画初始x坐标
        :param y: 绘画初始y坐标
        :return:
        """
        # 移动画笔初始位置
        pyautogui.moveTo(x=x, y=y, duration=0)
        sleep(0.5)
        distance = 300
        # 进行绘画操作
        pyautogui.dragRel(distance, 0, duration=0.1)
