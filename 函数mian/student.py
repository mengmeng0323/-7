def Differ():
    if __name__ == '__main__':
        print('我正在自己执行函数，我的密码是XXX')
        print('%s'%__name__)
    else:
        print('我正在被别人调用函数')
        print('%s'%__name__)
Differ()