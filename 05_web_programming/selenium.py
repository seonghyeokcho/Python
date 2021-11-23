from selenium.webdriver import Chrome
import time

browser = Chrome("/Users/csh/jupytercreation/Python_Practice/webcrawling/chromedriver")

# 1. 네이버로 이동
url = "http://www.naver.com"

#  1. 네이버 이동
browser.get(url)

#  2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

#  3. id, pw 입력
browser.find_element_by_id("id").send_keys("fprwmfdlek")
browser.find_element_by_id("pw").send_keys("skdmlpassword!")

#  4. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("btn_login")
elem.click()

browser.quit()