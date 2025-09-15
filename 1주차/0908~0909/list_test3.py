""
# 리스트 생성
list_a=[1, 2, 3]

# append()함수 = 리스트 뒤에 요소를 추가 
# 리스트명.append(요소)
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# insert()함수 = 리스트 중간에 요소를 추가
# 리스트명.insert(위치,요소)
list_a.insert(0,10)
print(list_a)
print()


# append()를 했을 때와 
list_b=[1,2,3]
list_b+=([4,5,6])
print(list_b)
print()

# extend()를 했을 떄 +=와 같음
list_b.extend([4,5,6])
print(list_b)
print()


