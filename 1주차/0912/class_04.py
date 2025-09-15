# 학생
# 이름, 학생 정보 출력
# 변수 : 이름
# 함수 : 학생 정보 출력

students=[]             # 학생들 이름 저장
class StudentMng:
    def __init__(self): # 클래스 객체 생성
        self.name=''
        self.age=0

    def info_student(self):
        print(f"이름: {self.name} 나이: {self.age}")


s1=StudentMng()  
s1.name = '홍길동'
s1.age = 27
students.append(s1)
s1.info_student() 


class Person():
    def __init__(self, name, age, addr):
        self.hello = "안녕하세요!"
        self.name = name
        self.age = age
        self.addr = addr

    def greeting(self):
        print(f"{self.hello}, 제 이름은 황수현입니다. ")

a=Person()
a.greeting