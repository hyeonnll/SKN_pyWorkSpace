# 함수
# 함수명 add
# 파라미터는 2개 op1, op2
# 결과를 반환한다.

def add(op1, op2):
    result=op1+op2
    return result

a=add(10,20)
print(a)

# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수명 : data

def show_number(data):
    return f"numbers= {data}"

a=show_number(add(10,20))
print(a)

hello=len("안녕하세요")
print(hello)

def hello1(name):
    hi=len(name)
    return hi
b=hello1("황수현")
print(b)