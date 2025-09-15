# 숫자를 입력받습니다.
# number_input_a = int(input("정수 입력->"))


# # 출력합니다.
# print("원의 반지름:", number_input_a)
# print("원의 둘레: ", 2* 3.14 * number_input_a)
# print("원의 넓이: ", 3.14*number_input_a*number_input_a)

# 오류를 피해가는 행위 --> 예외 처리
# num1 = int(input('숫자를 입력하세요: '))
# num2 = int(input('숫자를 입력하세요: '))


try:        # 예외가 발생할 가능성이 있는 코드
    num1, num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력: ").split())
    clac_list=[num1+num2,num1-num2,num1*num2,num1/num2]


    print('1. 더하기', end='\t')
    print('2. 빼기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기')
    choice= int(input("원하는 결과를 입력하세요: "))
    print(f'결과는 = {clac_list[choice-1]}')
except:     # 예외가 발생했을 때 실행할 코드
    print("오류발생")
else:       # 예외가 발생하지 않았을 때 실행할 코드
    pass
finally:    # 무조건 실행할 코드
    print("프로그램 종료")


# 예외(Exception) 논리 오류