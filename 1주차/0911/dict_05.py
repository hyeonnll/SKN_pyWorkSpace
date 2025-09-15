# 선거 시스템
# 유권자들이 기호로 투표를 진행, 결과를 리스트에 저장
# ex) 1,2,3
# 투표는 순환문을 이용해서 유권자가 10명이라면 10번 순환하면서 후보자(1~5)선택
# [1,1,2,3,4,1,5,1]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력

candidate = ['홍길동', '이순신', '강감찬', '율곡', '신사임당']
vote = [] # 투표 번호 저장 리스트
count = 10
result={} # 투표 카운트

for _ in range(count):
     vote.append(int(input('투표하세요!(1~5) : ')))

print(f"vote= {vote}")


for i in vote:           # vote의 0번째 숫자를 가져오고 result{}안에 숫자가 없으면 else 1 : 1추가 하고 
    if i in result:      # 그 뒤에 숫자가 있으면 value에 +1
        result[i]+=1
    else:
        result[i] = 1
print(f'result = {result}')


# 키의 값을 가져올 때.. 딕셔너리 변수 ['키값'] 없으면 에러
# 딕셔너리 변수 .get('키값') 없으면 None
max_key=max(result, key=result.get)
print(f"당선자 : {candidate[max_key-1]},득표수: {result[max_key]}")

            



    

