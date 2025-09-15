# 저금통
# list_a=[100,500,10,500,100,50,500,10]
# 저금통에 있는 동전의 종류 10,50,100,500

# set : 중복값 제거, 순서 없음

set_= {5,1,2,4,3,1,2,3,1}
print(f"set_a= {set_}")

import random

list_a = random.sample(range(10),6)
# list_b = random.sample(range(10),4)
list_b = [1,2,3,4,6,2,2,2,1,1,1,7,6,4,9,3]

find_list= []
for a in list_a:                # 여기서 set을 사용하지 않고 중복값이 제거될 수 있게 해보자
    for b in list_b:
        if a==b:
            find_list.append(a)
print(f"list_a: {list_a}")
print(f"list_b: {list_b}")
print(f"find_list: {find_list}")