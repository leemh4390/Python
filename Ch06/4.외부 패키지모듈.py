"""
    날짜 : 2023/01/12
    이름 : 이민혁
    내용 : 파이썬 외부패키지 모듈

"""

from openpyxl import Workbook


#새로운 엑셀파일 생성

workbook = Workbook()

#현재 시트 활성화
sheet = workbook.active

#데이터 입력
sheet['A1'] = '파이썬 Excel 실습'
sheet.append(['아이디','이름','휴대폰','나이','주소'])
sheet.append(['a101','김유신','010-1234-1234','20','부산'])
sheet.append(['a102','김유신1','010-1234-1235','21','부산'])
sheet.append(['a103','김유신1','010-1234-1236','22','부산'])

#파일 저장
workbook.save('C:/Users/java1/Desktop/Member.xlsx')
workbook.close()

print('프로그램 종료...')





