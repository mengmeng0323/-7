#配置表导入所需的第三方库

*** Settings ***
#库的名称大小写敏感
Library  SeleniumLibrary

*** Test Cases ***
百度搜索松勤
    #打开浏览器，并访问百度
    open browser    https://www.baidu.com/  chrome
    #加上隐式等待
    set selenium implicit wait  10
    #搜索框输入松勤 带上回车字符
    input text  id=kw   松勤\n
    #进入搜索页面-查找第一个搜索结果的文本
    ${res_text}  get text   id=1
    #检查文本-判断是否包含  松勤网 - 松勤软件测试
    should contain  ${res_text}   松勤网 - 松勤软件测试
    #关闭浏览器
    close browser

