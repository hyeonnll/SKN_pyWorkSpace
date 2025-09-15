print('='*50)
# 딕셔너리
    # .item()   .keys()     .values()
dict_1 = {
    '국어': 100,
    '수학': 90,
    '영어' : 80 
}
print(dict_1)
print('-'*50)

# 정렬
    # sorted()
print(dict(sorted(dict_1.items(),key=lambda data : data[1])))
print(dict(sorted(dict_1.items(),key=lambda data : data[1],reverse=True)))
print('-'*50)

# max
    # 딕셔너리 max()

#enumerate
    # 순환문에서 리스트를 감싸면 (인덱스, 리스트의 값)

# zip()
    # 여러개의 interable 들을 각 원소를 쌍으로 하는 집합
    # (1,2), ('사과', '배')
    #[ (1,'사과'), (2,'배') ]

# map()
    # interable(list) 한 객체의 각 요소에 특정 함수를 적용
    # map(int,['1','2']) -> [1,2]









# import collections 

#datas=[1,1,1,2,3,3,4,2,3,5,12,1]           정렬 쉽게 하는거
# print(collections.Counter(datas))