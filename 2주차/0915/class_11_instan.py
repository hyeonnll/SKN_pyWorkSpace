# isinstance() 함수 : 객체가 특정 클래스의 인스턴스(객체)인지 확인하는 데 사용
# 사용하는 이유
# 1. 타입 확인 : 함수나 메서드가 특정 클래스의 인스턴스를 기대할 때, isinstance()를 사용하여 전달된 객체가 올바른 타입인지 확인
# 2. 다형성 지원 : 상속 관계에서 부모 클래스와 자식 클래스

class Student:
    def study(self):
        print("공부 중")
class Teacher:
    def teach(self):
        print("가르치는 중")

peoples=[Student(), Teacher(), Student()]
del peoples[1]
if isinstance(peoples[0], Student):
    print(peoples[0].study())
else:
    print(peoples[0].teach())
