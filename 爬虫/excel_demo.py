import xlwt #excel写模块

#创建excel文件对象
def excel_init():
    workBook = xlwt.Workbook(encoding='utf-8')

    #在excel对象新建一个sheet
    workSheet = workBook.add_sheet('51job')
    colName = ['岗位','公司名称','地址','薪资','发布时间'] #创建exce表头名

    #excel-sheet   行与列都是从下标0开始的
    for one in range(len(colName)):
        workSheet.write(0,one,colName[one]) #write(行数，列数，字符串内容)

    return workBook,workSheet
    #workBook.save('D:\\ym_51job.xls')

