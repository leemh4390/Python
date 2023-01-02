"""

날짜 : 2023/01/02
이름 : 이민혁
내용 : 파이썬 연산자 실습하기

"""

#대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'apple'

print('a : ', a)
print('b : ', b)
print('e : ', e)
print('f : ', f)
print('g : ', g)

#산술연산자
num1 = 1
num2 = 2
num3 = 100
r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = num2 // num3
r5 = num2 - num3
r6 = num2 * num3
r7 = num2 ** num3
print('r1 ' , r1)
print('r2 ' , r2)
print('r3 ' , r3)
print('r4 ' , r4)
print('r5 ' , r5)
print('r6 ' , r6)
print('r7 ' , r7)

#복합대입연산자
num5, num6, num7, num8 = 5,6,7,8
num5 += 1
num6 -= 2
num7 *= 3
num8 /= 4

print('num5 : ', num5)
print('num6 : ', num6)
print('num7 : ', num7)
print('num8 : ', num8)

#비교연산자
var1 = 1
var2 = 2

rs1 = var1 > var2
rs2 = var1 < var2
rs3 = var1 >= var2
rs4 = var1 <= var2
rs5 = var1 == var2
rs6 = var1 != var2

print('var1 : ' , rs1)
print('var2 : ' , rs2)
print('var3 : ' , rs3)
print('var4 : ' , rs4)
print('var5 : ' , rs5)
print('var6 : ' , rs6)

#논리연산자
var3 = 3
var4 = 4

res1 = var3 > 2 and var4 > 3
res2 = var3 > 2 and var4 > 4
res3 = var3 > 2 or var4 > 3
res4 = var3 > 4 or var4 > 5
res5 = not var3 > var4

print('rest1 : ' , res1)
print('rest2 : ' , res2)
print('rest3 : ' , res3)
print('rest4 : ' , res4)
print('rest5 : ' , res5)