

*** Test Cases ***
case1
    log to console   hello world




    #声明变量
    ${abc}  set variable    2020
    ${ac}   set variable    2020

    should be equal    ${abc}   ${ac}   #比较两个变量的值


    #判断包含--前者是否包含后者
    #should contain    helloword    hi

    #如果需要传递非字符串，如int
    #可以采用一个关键字
    ${num1}    convert to integer   2021
    ${num2}    convert to number    2020.1
    #should be equal     ${num1}    ${num2}

    #通用检查的关键字
    ${var}   set variable   hello
    #参数是python表达式--如果引用RF变量，直接$变量名传递即可
    #注意表达式的空格-不能>=2个，，最多1个
    should be true    $num1 in [i for i in range(9)]
