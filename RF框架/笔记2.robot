

*** Test Cases ***
case1
    log to console   hello world




    #声明变量
    ${abc}  set variable    2020
    ${ac}   set variable    2020

    should be equal    ${abc}   ${ac}   #比较两个变量的值


    #判断包含--前者是否包含后者
    should contain    helloword    hi