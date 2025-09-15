# 요구 사항 분석
    # 가위 바위 보 게임 (컴퓨터 vs 휴면)
    # 가위 : 1 바위 : 2 보 : 3
    # 규칙 : 컴퓨터가 임의로 숫자를 선택  : random
    # 인간이 숫자를 입력               : input
    # 승패를 기록
    # 3번마다 계속할지 물어본다.         :for 
    # python으로 간단하게

import random

# 가위=1
# 바위=2
# 보=3
print("가위 바위 보 게임을 시작합니다.")
def get_com_num(start=1, end =3):
    return random.randint(start,end)  # 랜덤하게 선택한 컴퓨터의 값


def get_hum_num():
    return int(input("당신의 선택은?(1:가위, 2:바위, 3:보) : ")) # 인간이 입력하여 선택

# 승패 확인
def match_result(com_choice, hum_choice):
    if com_choice == hum_choice:
        print("비겼습니다!")
    elif (com_choice==1 and hum_choice==2) or \
        (com_choice==2 and hum_choice==3) or \
        (com_choice==3 and hum_choice==1):
        print("이겼습니다!")
    else:
        print("졌습니다ㅜㅜ")

    print(f"컴퓨터의 선택은 {com_choice}였습니다!")