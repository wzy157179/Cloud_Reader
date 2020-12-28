# -*- coding:utf-8 -*-
# @Author: wangzhongyao
# @Time: 2020/12/24
# @File: __init__.py
from selenium.webdriver.common.by import By
import win32api
import win32con


"""以下为系统请求url"""
# 自媒体
index_url = "http://10.6.10.145:8080/viewer/pc/index.html"

"""以下为元素配置信息"""
# 屏幕中心x坐标
screen_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / 2
# 屏幕中心y坐标
screen_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN) / 2
# 绘制初始x坐标
draw_x = win32api.GetSystemMetrics(win32con.SM_CXSCREEN) / 3
# 绘制初始y坐标
draw_y = win32api.GetSystemMetrics(win32con.SM_CYSCREEN) / 3
# 点击次数
click_one = 1
click_double = 2
# 点击按键
click_left = "left"
click_right = "right"
click_middle = "middle"
press_enter = "enter"
# 文件图标按钮
index_openfile_logo = By.ID, "fileUploadForm2"
# 文件选项开关
index_openfile_switch = By.ID, "btn-openfile-switch"
# 文件本地文件选项
index_openfile_local = By.ID, "btnOpenLocal"
# 文件网络文件选项
index_openfile_online = By.ID, "btnOpenOnline"
# 网络文件输入框
index_online_url = By.ID, "onlineUrlInput"
# 网络文件输入框确定按钮
index_online_button = By.ID, "btnOkOpen"
# 文档信息
index_document_info = By.ID, "docViewercontextMenuDocProperties"
# 文档信息_标题
index_document_info_title = By.ID, "docViewer_docPropertiesTitle"
# 文档信息_作者
index_document_info_author = By.ID, "docViewer_docPropertiesAuthor"
# 铅笔图标按钮
index_pencil_button = By.ID, "btnPencilTool"
# 手型图标按钮
index_hand_button = By.ID, "btnHandTool"
# 铅笔删除按钮
index_delete_pencil_button = By.ID, "delete_annot"
# 铅笔属性按钮
index_property_pencil_button = By.ID, "open_property"
# 铅笔属性黄色按钮
index_yellow_pencil_button = By.XPATH, '//*[@id="fwrCommentPropertyDlg"]/div[2]/dl/dd/span[4]/span'
# 铅笔设置默认属性按钮
index_default_pencil_button = By.ID, "set_default"
# 关闭铅笔属性按钮
index_close_property_pencil_button = By.ID, "closeBtn"
# 文档保存按钮
index_savefile_button = By.ID, "btnSave"
# 文档下载按钮
index_downloadfile_button = By.ID, "btnExportPDF_li"
# 文档保存提示信息
index_savefile_text = By.XPATH, '//*[@id="fwrAlertDlg"]/div[2]'
# 选择文本按钮
index_selecttext_button = By.ID, "btnTextSelectTool_li"
# 高亮按钮
index_highlight_button = By.ID, "btnHightLightTool_li"
# 下划线按钮
index_underline_button = By.ID, "btnUnderlineTool_li"
# 文本选择高亮按钮
index_selecttext_highlight = By.ID, "highlight_annot"
# 文本选择下划线按钮
index_selecttext_underline = By.ID, "underline_annot"
# 高亮属性蓝色按钮
index_highlight_blue_button = By.ID, '//*[@id="fwrCommentPropertyDlg"]/div[2]/dl/dd/span[3]'
# 选定sign_keyword.ofd文档坐标
index_line_x1 = 540
index_line_x2 = 750
index_first_line_y = 320
index_second_line_y = 350
index_third_line_y = 380
index_fourth_line_y = 410
index_drag_left = "left"
index_drag_right = "right"
