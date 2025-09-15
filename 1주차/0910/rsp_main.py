import rsp_game


for i in range(1,101):
    
    cc=rsp_game.get_com_num()
    hc=rsp_game.get_hum_num()
    rsp_game.match_result(cc,hc)

    if i % 3==0:
            is_continue=input("계속 하시겠습니까? (y/n): ")
            if is_continue=="n":
                  break
# # if round % 3 ==0:
# while True:
#     i=input("계속 하시겠습니까? (y/n): ")
#     if i ==("y","yes"):
#         break






        


# if com_choice==1 and hum_choice==2:
#     print("이겼습니다!")

# if com_choice==1 and hum_choice==3:
#     print("졌습니다ㅜㅜ")

# if com_choice==2 and hum_choice==1:
#     print("졌습니다ㅜㅜ")

# if com_choice==2 and hum_choice==3:
#     print("이겼습니다!")

# if com_choice==3 and hum_choice==1:
#     print("이겼습니다!")

# if com_choice==3 and hum_choice==2:
#     print("졌습니다ㅜㅜ")

# print(f"컴퓨터의 선택은 {com_choice}였습니다!")


