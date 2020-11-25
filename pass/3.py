def col(x,*number):
    for y in number:
        x=x*y
    return x
print(col(5,6,7,8))