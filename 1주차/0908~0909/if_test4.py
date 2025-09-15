# 사용자로부터 점수를 입력받아서 A B C D E F 학점을 출력

score = int(input("총점을 입력하시오: "))
print(f'score= {score}')
if score >=90 :
    print("A") #90 이상
elif score >=80 :
    print("B") # 80이상 90미만
elif score>= 70:
    print("C") # 70이상 80미만
elif score >= 60:
    print("D") # 60이상 70미만
else: 
    print("F") # 60미만