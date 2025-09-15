# 학생 클래스 생성
# 인스턴스(객체) 변수 : 이름, 국어, 영어, 수학
# 인스턴스 메서드 : 총점, 평균, 학점

class Student:
    def __init__(self, name, kor, eng, mat):
        # 인스턴스 변수
        self.name=name
        self.kor=kor
        self.eng=eng
        self.mat=mat
    def total(self):
        return self.kor+self.eng+self.mat
    def avg(self):
        return self.total()/3
    def grade(self):
        if self.avg()>=90:
            return 'A'
        elif self.avg()>=80:
            return 'B'
        elif self.avg()>=70:
            return 'C'
        elif self.avg()>=60:
            return 'D'
        else:
            return 'F'
    def __str__(self):
        return f"이름 : {self.name}, 총점 : {self.total()}, 평균 : {self.avg()}, 학점 : {self.grade()}"

# 인스턴스 생성
s1=Student("황길동", 90, 80 , 80)
print(s1)
