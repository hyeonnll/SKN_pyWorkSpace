# 가위 바위 보 게임 클래스로 구현
# 사용자로부터 입력을 받아 컴퓨터와 대결하는 간단한 가위 바위 보 게임 구현
# 사용자는 "가위", "바위", "보" 중 하나를 입력하고, 컴퓨터는 무작위로 선택
# 게임의 승패를 판단하고 결과를 출력합니다.
# 가위는 1, 바위는 2, 보는 3으로 표현합니다.
# 게임이 끝나면 계속할지 물어본다.

import random

class RSPGame:
        choice = {"가위":1, "바위":2, "보":3}
        def __init__(self):
            self.user_choice = None
            self.com_choice = None
            self.result = None
        
        def get_user_choice(self):
            while True:
                try:
                     user_input = str(input("가위, 바위, 보 중 하나를 입력하세요. (종료하려면 '종료' 입력): "))
                     if user_input == "종료":
                         return False
                     if user_input in self.choice:
                         self.user_choice = self.choice[user_input]
                         return True
                     else:
                          print("잘못된 입력입니다. 다시 입력하세요.")
                except Exception as e:
                    print(f"오류 발생: {e}. 다시 시도하세요.")
        def get_com_choice(self):
            self.com_choice = random.randint(1, 3)
        def determine_winner(self):
            if self.user_choice == self.com_choice:
                self.result = "무승부"
            elif (self.user_choice == 1 and self.com_choice == 3) or \
                 (self.user_choice == 2 and self.com_choice == 1) or \
                 (self.user_choice == 3 and self.com_choice == 2):
                self.result = "승리"
            else:
                self.result = "패배"
        def play(self):
            self.get_com_choice()
            self.determine_winner()

