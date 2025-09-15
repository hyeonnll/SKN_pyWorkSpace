# 사용자 입력 처리 함수
# 이름 get_data()
# perameter
    # start : 시작값
    # end : 종료값
    # input_str : 가이드 문구
# 사용자 입력은 input()
# return 정수로 변환된 입력값


def get_data(start,end):
    while True:
        try:
            data=int(input(f"정수값를 입력하시오({start}~{end}):  "))
            if not int(start)<=data<=int(end):
                raise ValueError(f"{start}~{end}초과, 사이 값을 입력하세요.")
        except Exception as e:
            print(f"오류: {e}")
        else:
            return data

    


# 게임
def check_winner(human,computer):
    count=0
    game_history=[]
    if human > computer :
        print("크다")       # 사람>콤퓨타 = 크다
        game_history.append((human,"크다"))
    elif human < computer :
        print("작다")       # 사람<콤퓨타 = 작다
        game_history.append((human,"작다"))
    else:
        print(f"정답까지 시도 횟수:{count}")
        for guss_value, state in game_history:
            print(f'{guss_value} - {state}')
        print("똑같다")
        return True
    return False
    
