"""
날짜 : 2023/01/11 
이름 : 이민혁
내용 : 파이썬 클래스 실습하기
"""

class Car:

    #생성자
    def __init__(self,brand,color,price): 
        #속성
        self.brand = brand
        self.color = color
        self.price = price

    #기능
    def speedUp(self):
        print('%s 속도 올리기...' % self.brand)

    def speedDown(self):
        print('%s 속도 내리기...' % self.brand)

    def show(self):
        print('차량명 : ', self.brand)
        print('차량색 : ', self.color)
        print('가격 : ', self.price)


