try:        # 예외가 발생할 가능성이 있는 코드
    num1, num2 = map(int, input("공백을 기준으로 두개의 숫자를 입력: ").split())
    clac_list=[num1+num2,num1-num2,num1*num2,num1/num2]


    print('1. 더하기', end='\t')
    print('2. 빼기', end='\t')
    print('3. 곱하기', end='\t')
    print('4. 나누기')
    choice= int(input("원하는 결과를 입력하세요: "))
    print(f'결과는 = {clac_list[choice-1]}')
except ValueError as e:    
    print(f"오류발생 : {e}")
except IndexError as e:    
    print(f"오류발생 : {e}")
except Exception as e:    
    print(f"에러종류 : {e.__class__.__name__}, 설명 : {e}")

print('프로그램 종료')