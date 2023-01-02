"""
날짜 : 2023/01/02
이름 : 이민혁
내용 : 파이썬 기본입출력 실습하기
"""


#파이썬 입력
num = input('숫자 입력 : ')

#파이썬 출력
print('num ' , num)
print('num type',type(num))

#문자열 순잔 변환
r1 = int(num) + 1
print('r1 : ', r1)

#출력 옵션
print('010','1234','5678', sep='-')
print('Hello',end='~')
print('Pyton',end=' ')
print('Programming')