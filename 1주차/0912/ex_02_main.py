import random as rm
import ex_02 

start, end =1, 100
computer=rm.randint(start,end)
count=0
game_history=[]
while True:
    count+=1
    human=ex_02.get_data(start,end)
    if ex_02.check_winner(human,computer,count,game_history):
        break