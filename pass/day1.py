# userNmae = input("请输入用户名：")
# passWord = input("请输入口令：")
#
# if userNmae == "admin" and passWord == "123456":
#     print("身份验证成功")
# else:
#     print("身份验证失败")



# x = float(input("x="))
# if x > 1:
#     y=3*x-5
# elif x>=-1 and x<=1:
#     y=x+2
# else:
#     y=5*x+3
# print(y)


grade = float(input("请输入成绩："))
if grade >= 90:
    print("成绩为A")
elif grade>=80 and grade<90:
    print("成绩为B")
elif grade>=70 and grade<80:
    print("成绩为C")
elif grade>=60 and grade<70:
    print("成绩为D")
else:
    print("成绩为E")