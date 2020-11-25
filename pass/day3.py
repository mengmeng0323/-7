# for num in range(100,1000):
#     low = num % 10
#     min = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + min ** 3 + high ** 3:
#         print(num)

# from module1 import foo
# foo()

import module1 as m1
import module2 as m2

m1.foo()
m2.foo()