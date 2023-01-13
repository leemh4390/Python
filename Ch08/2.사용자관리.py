"""
    날짜 : 2023/01/13
    이름 : 이민혁
    내용 : 파이썬 사용자 관리 프로그래밍 실습하기
"""

import pymysql

conn = pymysql.connect(host ='127.0.0.1',
                       user='root',
                       password='1234', 
                       db = 'java1db', 
                       charset = 'utf8')

                       
while True:  
    print('0 :종료, 1: 등록, 2:조회, 3:검색, 4:삭제')
    answer = 0

    try:
        answer = int(input('선택 : '))

    except Exception as e:
        print('다시 입력하세요.', e)
        continue

    if answer == 0:
        break
    elif answer == 1:


        print('등록완료')

    elif answer == 2:
        cur = conn.cursor()
        sql = "select * from `user1`"
        cur.execute(sql)
        conn.commit()

        print('|아이디|비밀번호|이름|연락처|나이')
        for row in cur.fetchall:
            print('-----------')
            print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2],row[3],row[4]))

        print('조회 완료')

    elif answer == 3:
        name = input('이름 검색 : ')

        cur = conn.cursor()
        cur.execute("select * from `user1` where `name` = '{}'".format(name))
        conn.commit()

        print('|아이디|비밀번호|이름|연락처|나이')
        for row in cur.fetchall:
            print('-----------')
            print('|%s|%s|%s|%s|%s|' % (row[0], row[1], row[2],row[3],row[4]))

        print('검색 완료....')

    elif answer == 4:
        name = input('이름 검색 : ')      

        cur = conn.cursor()
        cur.execute("delete from `user1` where `name` = '{}'".format(name)) 
        conn.commit()

        print('삭제 완료')

    else:
        print('0 ~ 4 까지만 입력하세요.')

# 데이터베이스 종료
conn.close()

print('프로그램 종료...')