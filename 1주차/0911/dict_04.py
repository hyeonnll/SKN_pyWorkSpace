'''
stafe={    
    '황길동': {
        '직책':'매니저',
        '연봉':'200.000.000',
        '경력': {
            '삼성전자':5,
            '엘지전자':3,
            'sk ': 10
        },
        '취미':['낚시','헬스','수영','자전거']
        
    }
}
print(stafe['황길동']['경력']['엘지전자'])
'''


# 학생이 가지는 과목이 3과목이고 국어 영어 수학 이렇게 점수를 관리
student1 = [100,80,95]
student2 = [90,85,90]
student3 = {'국어' : 100, '영어' : 100, '수학' : 100}
student4 = {'수학' : 100, '영어' : 100, '국어' : 100}
student5 = {'영어' : 100, '국어' : 100, '수학' : 100}
element_class =[student3,student4,student5]

total_math = 0

for student in element_class:
    total_math+=student['수학']
    print(total_math)

