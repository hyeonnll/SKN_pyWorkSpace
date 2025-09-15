import random
# 매개변수 o, 반환값 o
def check_human(name):
    human_list= []
    human_list.append(name)
    return human_list
 
# 매개변수 o, 반환값 x
def welcome(name,set_number):
    print(f"어서오세요! {name}님! {name}님 자리는 {set_number}번 입니다")
    
# 매개변수 x, 반환값 o
def get_human_number():
    set_number=random.sample(range(999),1)
    return set_number


    

# 매개변수 x, 반환값 x

welcome("황수현",1)
print(get_human_number())