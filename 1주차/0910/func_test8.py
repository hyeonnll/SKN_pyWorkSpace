# 간단한 함수
# 함수내의 로직인 한줄로 표현 가능한 함수들
def my_add(a,b):
    return a+b

# 람다 함수 - 한줄로 표현한 함수 lamb
# 간단한 함수를 즉석에서 만들떄 유용
# 값을 무조건 return하기 때문에 return 키워드를 사용하지 않음
test= lambda a,b: a+b
a=10
b=20
print(f"a+b= {test(a,b)}")
print(test(a,b))
