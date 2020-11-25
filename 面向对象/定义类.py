class Student(object):
    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def study(self,course_name):
        print("%s正在学习%s."%(self.name,course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s只能观看《熊出没》."%self.name)
        else:
            print("%s正在观看电影."%self.name)

# 写在类中的函数，我们通常称之为（对象的）方法，这些方法就是对象可以接收的消息