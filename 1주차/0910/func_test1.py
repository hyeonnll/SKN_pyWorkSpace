import random
import datetime

# print(random.randint(1,5)) # 1~5 랜덤 int 반환\

# 함수정의 def 키워드 사용
# 매개변수(Parameter) : 함수가 전달받는 값
# 인자 (Argument)    : 함수를 호출할때 전달하는 값
# 반환값(Retrun value) : 함수가 작업을 마치고 호출한 곳으로 돌려주는 값, return 키워드 사용

# 함수의 구성요소
def mycalc(num1, num2):
   
    result= num1+num2
    return result


# 1. 매개변수와 반환값이 없는 함수
def say_hello():
    print("안녕하세요.")

# 2. 매개변수가 있고 반환값이 없는 함수
def say_hello_name(name):
    print(f"{name}님 안녕하세요!")
    

# 3. 매가변수가 없고 변환값이 있는 함수
def get_current_time():
    return datetime.datetime.now()

# 함수 호출
mycalc(1,2)
say_hello()
say_hello_name("황수현")
print(get_current_time())