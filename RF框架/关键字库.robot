*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
WebUI测试
#使用非内置库关键字需要显示导入
    open browser  http://baidu.com     chrome
    close browser

自定义库
    #需要自行编写python文件
