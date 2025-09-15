# list, set, tuple, dict

result=dict([['name','홍길동'], ['age',20]])

print(type(result))
print(result)

# 두개의 리스트 한개는 키에 해당하는 값들의 집합
# 다른 하나는 값에 해당하는 집합
# 이걸 dict 구조로 만들려면?

names= ["홍길동","이순신","강감찬"]
scores=[100,99,98]

studs={}
# studs["홍길동"]=100
# print(studs)

count=0
for name in names:
    studs[name]=scores[count]
    count+=1
print(name)