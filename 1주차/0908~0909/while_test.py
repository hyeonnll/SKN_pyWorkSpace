# while 반복횟수가 없다. 어떤 조건을 만족할때까지 계속 돌림 
# # while 조건 :
# count=0
# while True: # 무힌으로 돌림
#     print(f"순환문: {count}")
#     count+=1 

import time

count= 0
while True:
    count+= 1
    print(f" {count}초")
    time.sleep(1) # 1초 지연

    # 5초 단위로 사용자한테 계속 할껀지 물어본다 "To be continue(Y/N)"
    if count %5 == 0 :
        user_input =input("To be continue(Y/N)").upper()
    
        if user_input =='N':
            print("STOP")
            break