# 숫자 맞추기 게임
# 규칙 
# 1. 컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택
# 2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞춥니다.
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "너무 큽니다." 라고 출력
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "너무 작습니다." 라고 출력
# 5. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자와 같으면 "정답입니다!" 라고 출력하고 게임을 종료합니다.
# 6. 사용자가 숫자를 맞출 때까지 계속 입력을 받습니다.

import random
class NumberGuessingGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 100)
        self.user_guess = None
    def get_user_guess(self):
        while True:
            try:
                self.user_guess = int(input("1부터 100 사이의 숫자를 입력하세요: "))
                if 1 <= self.user_guess <= 100:
                    break
                else:
                    print("1부터 100 사이의 숫자를 입력해야 합니다. 다시 시도하세요.")
            except ValueError:
                print("유효한 숫자를 입력하세요. 다시 시도하세요.")
    def check_guess(self):
        if self.user_guess < self.number_to_guess:
            print("너무 작습니다.")
            return False
        elif self.user_guess> self.number_to_guess:
            print("너무 큽니다.")
            return False
        else:
            print("정답입니다!")
            return True
    def play(self):
        print("지금부터 숫자 맞추기 게임을 시작합니다.")
        while True:
            self.get_user_guess()
            if self.check_guess():
                break
NumberGuessingGame().play() # 게임 시작1