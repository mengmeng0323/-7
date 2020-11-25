# l = list(range(100))
# print(l[-10:])
# print(l[10:20])
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    else:
        min = max = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return (min,max)

