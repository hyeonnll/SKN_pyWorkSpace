# remove
list_a=[1,1,1,2]
#list_a.remove(2) # 리스트 안에 가장 앞에 있는 숫자 2를 지운다. 한번만 지움
#print(list_a)

# 1. solution
# for i in range(len(list_a)-1, -1, -1):
#     if list_a[i]==1:
#         del list_a[i]

# print(list_a)

# remove
list_a=[1,2,2,2,2,2,2,2,2]
for i in range(len(list_a)): # 리스트 갯수만큼 돌린다
    print(list_a)
    if 1 in list_a:
        list_a.remove(1)
    else:
        break

print(list_a)

number=[273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in number:
    if number>=100:
        print(f"100이상의 상수: {number}")