# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리 삭제
# 딕셔너리 특정 키의 데이터를 수정

# enumerate(), zip(), .items(), .keys(), .values()
# map(), 함수의 파라미터 - 키워드 카라미터, 가변 키워드 파라미터

my_bag = {
          '필통': '파란색', 
          '공책': '수학공책', 
          '지갑' : '분홍색 지갑'
          }
# 출력
print(my_bag)
# 가방에서 필통을 꺼내서 출력
print(f"필통 {my_bag['필통']}")
# 가방에서 공책을 꺼내서 출력
print(f"공책 {my_bag['공책']}")
# 지갑이 오래되서 '가죽지갑'으로 변경
my_bag['지갑']='가죽지갑'
print(f'my_bag= {my_bag}')
# 가방에 하얀색 물통을 추가
my_bag['물통']='하얀색'
print(f'my_bag= {my_bag}')

print('-'*50)

for i in my_bag:
    print(f"key= {i} value= {my_bag[i]}")
    