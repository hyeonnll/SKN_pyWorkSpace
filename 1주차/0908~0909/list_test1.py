age = 25
array = [273, 32, 10.9, "문자열", True, False, age]
print(array[3][2]) # array 열 중 3번째 중 2번쨰 "열"
print(array[0:])   # start_index : end_index-1 
print(array[:3])   # 0, 1, 2
print(array[3:])   # 3, 4, 5, 6
print(array[-2:])  #
print(array[::2])  # 시작 지점부터 2칸씩
print(array[::-1]) # 뒤에서 

array2 = [100, array]
print(array2) 
print(array2[1][3])

temp = [
    [1,2],   # temp 0
    [10,20], # temp 1 # temp [1][2], temp[1,2] X
    [30,40] # temp 2
]
print(temp[1][1])