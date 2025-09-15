# 사용자 입력 처리 함수
# 이름 get_data()
# perameter
    # start : 시작값
    # end : 종료값
    # input_str : 가이드 문구
# 사용자 입력은 input()
# return 정수로 변환된 입력값


def get_data(start,end,input_str):
    while True:
        try:
            data=int(input(f"정수값를 입력하시오({start}~{end},{input_str}):  "))
            if not int(start)<=data<=int(end):
                raise ValueError(f"{start}~{end}초과, 사이 값을 입력하세요.")
        except Exception as e:
            print(f"오류: {e}")
        else:
            return data

    

get_data(31,110,"정수")