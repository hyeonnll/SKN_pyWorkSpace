# random 라이브러리 사용 방법
import random
random_list=random.sample(range(100), 5) # random 라이브러리에서 sample 함수 호출
print("-"*50)
print("#random_list")
print(random_list)
print()


# 0~10 사이중에서 랜덤하게 한개 추출
random_int=random.randint(0,10)
print("#random_int")
print(random_int)
print()

random_list.append(random_int) # random_list에 random_int를 append
print( 50 in random_list) # 리스트에 50이 있는지
print(random_list)
print()


# del 삭제
del random_list[0]
print("# 위 리스트에서 0번 삭제")
print(random_list)
print()

# pop 삭제
remove_number=random_list.pop(1)
print("# remove_number: ",remove_number)
print()
print("# pop된 random_list")
print(random_list)

# clear
