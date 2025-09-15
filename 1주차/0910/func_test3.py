#다양한 매개변수
    # 기본 매개변수 default parameter

def myadd(num1,num2=0):     # parameter에 =0을 주면 디폴트 값 0
    return num1+num2

result=myadd(10)            # 디폴트 값을 안주면 parameter 값을 두개를 줘야하지만
                            # 디폴드 값을 주게 되면 디폴드 값을 안준 한개의 변수에만 값을 부여하면 됨
print(f"result: {result}")


# def myadd(num1, num2=0, num3):     # 기본 매개변수 default parameter는 항상 변수의 마지막에만 올 수 있다. 중간에 낄 수 없음
#     return num1+num2+num3

# result=myadd(10,20)          
                            
# print(f"result: {result}")


def myadd(num1=0,num2=0, num3=0):     
    return num1+num2+num3

result1=myadd()
result2=myadd(10)
result3=myadd(10,20)
result4=myadd(10,20,30)

print(result1,result2,result3,result4)
