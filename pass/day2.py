# sum = 0
# for i in range(2,100,2):
#     sum = sum + i
# print(sum)

import random
answer = random.randint(1,100)
count = 0
while True:
    count+=1
    number = int(input("请输入："))
    if answer > number:
        print("往大点猜")
    elif answer < number:
        print("往小点猜")
    else:
        print("恭喜你，猜对了！")
        break
print("你总共猜了%d次"%count)
if count>7:
    print("你的智商不足啊")
