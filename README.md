1. 目录结构

   -base 存放基类

   -data 存放测试数据

   -image 存放截图

   -log 存放日志

   -page 存放页面方法

   -scripts 存放测试用例

   -testcase 存放测试文档

   -tools 存放工具

   -pytest.ini pytest配置文件

   -venv 虚拟环境

2. 运行方式

   按照testcase里的测试文档路径和文档信息来修改data里的测试数据 ( 可自行添加文档 )

   在 pycharm 下方 Terminal 中输入pytest运行自动化测试

   测试完成后 在 Terminal 中输入 allure generate report/ -o report/html --clean  生成HTML报告

   HTML报告生成在 report/html目录下