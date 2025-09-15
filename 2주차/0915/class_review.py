#  기본 클래스 생성
class Review:
    #클래스 변수 생성 -> 모든 인스턴스(객체)가 공유
    count = 0
    # 생성자 메쏘드 
    def __init__(self, name=""):
        self.name=name

# 인스턴스 생성 -> 클래스를 마치 함수처럼 호출
r1= Review(100,"황길동")
r2= Review()

# 인스턴스 변수 변경
r1.name="첫번째 리뷰"
print(f"r1 인스턴스 변수: {r1.name}/ r2 인스턴스 변수 : {r2.name}")
print(f" 클래스 변수 : {Review.count} / r1 클래스 변수 : {r1.count} \
         /r2 클래스 변수 : {r2.count}")
