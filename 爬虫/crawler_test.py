#设置读取网页的头部，该行代码主要用于模拟浏览器来访问网站
user_header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#https://search.51job.com/
#51job


import requests,re
import excel_demo

workBook,workSheet = excel_demo.excel_init()
#
web_url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

def get_page(url):
    #<span class="td">共3页，到第</span>
    resp = requests.get(url, headers=user_header)

    # 2- 获取响应数据
    resp.encoding = 'gbk'  # 设置编码
    pages = re.findall('<span class="td">共(.*?)页，到第</span>',resp.text,re.S)[0].strip()
    return int(pages)

print('---------->:',get_page(web_url))

row = 1 #行号初始值
for page in range(1,get_page(web_url)+1):
    #1- 使用requests构建请求
    web_url = f'https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{page}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url,headers = user_header)

    #2- 获取响应数据
    resp.encoding = 'gbk'#设置编码
    #print(resp.text)#响应内容--字符串
    #print(resp.content)#byte--字节格式

    #3- 提取有效数据
    '''
    <div class="el">
            <p class="t1 ">
                <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
                <input class="checkbox" type="checkbox" name="delivery_jobid" value="122115682" jt="0" style="display:none">
                <span>
                    <a target="_blank" title="自动化测试工程师" href="https://jobs.51job.com/hangzhou-xhq/122115682.html?s=01&amp;t=0" onmousedown="">
                        自动化测试工程师                </a>
                </span>
                                                                        </p>
            <span class="t2"><a target="_blank" title="杭州雅顾科技有限公司" href="https://jobs.51job.com/all/co3736458.html">杭州雅顾科技有限公司</a></span>
            <span class="t3">杭州-西湖区</span>
            <span class="t4">1.5-2万/月</span>
            <span class="t5">05-15</span>
        </div>
    '''
    lines = re.findall('<div class="el">(.*?)</div>',resp.text,re.S)


    #获取每一行具体数据
    for line in lines:
        temp = re.findall('<a target="_blank" title="(.*?)" href=',line,re.S)#re.S  让它包含所有空格符
        #print(temp)
        #获取岗位名称
        jobName = temp[0].strip()
        workSheet.write(row,0,jobName) #将岗位名称写进第1行第0列（列是从0开始）
        #获取公司名称
        company = temp[1].strip()
        workSheet.write(row,1,company)
        #获取公司地址
        address = re.findall('<span class="t3">(.*?)</span>',line,re.S)[0].strip()
        workSheet.write(row,2,address)
        #获取薪资
        money = re.findall('<span class="t4">(.*?)</span>',line,re.S)[0].strip()
        workSheet.write(row,3,money)
        #获取发布时间
        jobTime = re.findall('<span class="t5">(.*?)</span>',line,re.S)[0].strip()
        workSheet.write(row,4,jobTime)
        #print(jobName,company,address,money,jobTime)
        row += 1


#4- 存储excel
workBook.save('D:\\ym_51job.xls')