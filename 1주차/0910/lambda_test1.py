# 람다가 사용되지 않는 상황
# def add(a,b):
#     return a+b

# def minus(a,b):
#     return a-b

def calc(func,a,b):
    return func(a,b)

# print(calc(minus,1,2))


# 람다 사용
print(calc(lambda a,b :a+b, 1,2))
print(calc(lambda x,y: x*y, 3,4))