"""
날짜 : 2023/01/11
이름 : 이민혁
내용 : 파이썬 상속 실습하기
"""

from sub2.StockAccount import StockAccount 

kb = StockAccount('kb증권', '101-11-1110', '홍길동', 50000,1, '삼성전자', 60000)
kb.deposit(100000)
kb.sell(5, 70000)
kb.show()