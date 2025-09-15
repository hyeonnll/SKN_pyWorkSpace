# 집합을 이루는 요소 : 숫자, 문자, 문자열, 리스트, 셋, 튜플
[1, 1.5, "1212","2",[1,2],(1,5,6),{2,3} ]
# dict
# 키와 값의 쌍으로 구성
# 순서가 없다
# 키는 중복 안됨
# 키는 변하지 않는 자료형만 가능(문자열, 숫자, 투플)
# CRUD 가능
#  각 요소에 접근할 때는 키값으로 접근 (인덱스가 아님)


# Create
student= {
    "name" : "홍길동",
    "age"  : 20,
    "major" : "컴퓨터"
}
# Read
print(f"student['name']= {student['name']}")

# Update
student['name']='이순신'
print(f"student={student}")

# Delete
del student['name']
print(f"student={student}")

#Add
student['addr']= '서울시 강남구'
print(f"student={student}")
