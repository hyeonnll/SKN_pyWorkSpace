# 가변 매개변수
    # 함수정의 할 때, 매개변수의 개수를 지정하지 않습니다.
    #  함수 내부에서는 리스트로 간주합니다.
    # 함수를 호출하는 쪽에서 편안하게 1,2,3,4 or 1,2,3,4,5,1,4,5

def myFunc1(*args):     # * --> 변수를 (1,2,3,4,5) 이런식으로 여러개 받았을 때 하나의 리스트로 받아줌
    for i in args:
        print(i)

myFunc1(10,20,30,40)

def myFunc2(args):     # 위 함수와 똑같음
    for i in args:
        print(i)

myFunc2([10,20,30,40])

a,b=[10,20]
print(f"a={a}")
print(f"b={b}")
