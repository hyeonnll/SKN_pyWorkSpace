# pip install pymysql
# pip install dotenv : 환경변수 .env를 로드할 수 있는 라이브러리
import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()
# 1. DB 연결
conn=pymysql.connect(
host = os.getenv('DB_HOST'),
user = os.getenv('DB_USER'),    
password = os.getenv('DB_PASSWORD'), 
database = os.getenv('DB_NAME')
)
print('접속성공!')


# 2. 각 테이블별
    # C - insert
    # R - select
    # U - update
    # D - delete

# 고객 - customer
# C - insert
def create_customer(name):
    sql = 'insert into customer values(null, %s)'
    with conn.cursor() as cur:
        cur.execute(sql,name)
        conn.commit()
    print('고객 추가 완료')

# R - select
def readAll_customer(isDict= False):
    sql = 'select * from customer'
    result=[]

    if isDict:
        with conn.cursor(pymysql.cursors.DictCursor) as cur:
            cur.execute(sql)
            for i in cur.fetchall():
                print(f'{i['customer_id']} {i['name']}')

    else:
        with conn.cursor() as cur:
            cur.execute(sql)
            for i in cur.fetchall():
                print(f'{i[0]} {i[1]}')
                result.append(
                    {"회원아이디": i[0], "회원이름": i[1]},
                    )
    print(f'조회 완료 {result}')
    return result

# U - update
def update_customer(customer_id,name):
    sql = '''
    update customer
    set name = %s
    where customer_id = %s
    '''
    with conn.cursor() as cur:
        cur.execute(sql,(name,customer_id))
    conn.commit()
    print(f'{customer_id}, {name}님이 업데이트 되었습니다.')

# D - delete
def delete_customer(customer_id):
    sql = 'delete from customer where customer_id = %s'
    with conn.cursor() as cur:
        cur.execute(sql,customer_id)
    conn.commit()
    print(f'{customer_id}님이 삭제되었습니다.')

# create_customer('황길동')
readAll_customer()
# update_customer()


# 3. 메쏘드
    # 회원가입
    # 상품정보 출력
    # 상품구입
    # 상품정보 입력
    # 대쉬보드 : 고객별 상품별 구매회수, 평균구매액

# 4. 기능구현과 테스트가 되면 streamlit으로 UI 구성 - 템플릿 화면을 보고 유사한 형태로 구현
conn.close() #접속해제