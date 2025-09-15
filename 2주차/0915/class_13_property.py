# @property 의 개념 함수를 변수사용하듯이 함수 이름만 가지고 사용하는 방법

import random
class Person:
    def __init__(self, name, age):
        self.name= name     # private  변수로 설정
        self._age = age      # private  변수로 설정
    
    @property       # == getter
    def age(self):
        return self._age
    
    
    @age.setter
    def age(self, value):
        self._age=value


p1=Person("황길동",20)
print(p1.age)
p1.age = 30
print(p1.age)


