"""
날짜 : 2023/01/17
이름 : 이민혁
내용 : Python 가상브라우저 실습하기
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome('./chromedriver.exe',options=chrome_options)

# 네이버 이동
browser.get('https://www.naver.com')

# 로그인 클릭
btnLogin = browser.find_element(By.CSS_SELECTOR,'#account > a')
btnLogin.click()

# 아이디/비밀번호 입력
input_id = browser.find_element(By.CSS_SELECTOR,'#id')
input_pw = browser.find_element(By.CSS_SELECTOR,'#pw')
input_id.send_keys('yamyame03')
input_pw.send_keys('a43900810')

btnSubmit= browser.find_element(By.CSS_SELECTOR,'#log\.login > span')
btnSubmit.click()
