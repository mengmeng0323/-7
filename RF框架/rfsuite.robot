*** Test Cases ***
用例1
    #用例主体-关键字部分-另起一行,至少空两格，通常四个空格
    #关键字-大小写不敏感，关键字与参数至少空两格
    #RF中两个以上的空格就是单元格的间距
    #入股RF关键字需要接收两个以上的参数，参数与参数之间也需要空两个以上空格
    log to console  hello robot


用例2
    #配置区域--配置项，比如用例的描述，用例的标签
    [Documentation]  用例描述-做什么测试的
    [Tags]  冒烟测试    回归测试
    #主体区域--写用例步骤中的关键字
    log to console  用例2


教管系统-查询课程
    ${courses}  getCourses
    log to console   ${courses}