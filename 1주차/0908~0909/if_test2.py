# kor, eng, math 각 변수에 사용자로부터 값을 받아서
# avg 변에 평균값을 저장하고, 조건을 평균이 60이상이고 
# kor, eng, math 변수의 각 값이 40 이상때만
# 합격을 출력하는 프로그램

kor = int(input("국어 점수 입력: "))
eng = int(input("영어 점수 입력: "))
math = int(input("수학 점수 입력: "))

avg = (kor + eng + math) / 3
print(avg)
if avg >= 60 and kor >= 40 and eng >= 40 and math >= 40:
    print("합격")  
else:
    print("불합격")