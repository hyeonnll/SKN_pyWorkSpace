import random

list_a = random.sample(range(11),7)     # 0~10 중복되지 않은 임의이 7개
list_b = random.sample(range(11),7)

#중복을 허용하면서 0~10 임의의 7 추출
# random.randint(0,10) -> 임의의 한개 값

list_c = []
for i in range(7):
    list_c.append(random.randint(0,10))
print(list_c)

# 합집합
    # 연산자 | (파이프 연산자)
set_a={1,2,3}
set_b={3,4,5}
print("합집합")
print(set_a | set_b)
    # 메서드 .union()
print(set_a.union(set_b))
    


# 교집합
    # 연산자 & --> and
set_a, set_b ={1,2,3,4},{2,3,5}
print("교집합")
print(set_a & set_b)
    # 메서드 .intersection
print(set_a.intersection(set_b))

# 차집합
    # 연산자 -
print("차집합") 
print(set_a - set_b)
    # 메서드 .difference
print(set_a.difference(set_b))
