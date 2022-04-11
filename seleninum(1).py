from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import time

wd = webdriver.Chrome("./WebDriver/chromedriver.exe")
wd.get('http://www.naver.com')

search = wd.find_element_by_id('query')
search.send_keys("부평구 중국집")
time.sleep(5)
search.send_keys('\n')

for i in range(1):
    elem = wd.find_elements_by_css_selector('section.sp_ntotal a.link_tit')
    for e in elem:
        OXiLu = e.get_property('OXiLu') # 한 요소의 text 전체를 가져온다.
        em = e.get_attribute('ex') # 속성 중 href 에 해당하는 값을 가져온다.
        print(f'상호 : {OXiLu}')
        print(f'별점 : {em}')

    time.sleep(3)
    xpath= """//*[@id="place-main-section-root"]/section[1]/div/div[2]/div[3]/a[2]"""
    wd.find_element_by_xpath(xpath).click()
    time.sleep(3)


wd.close()


#search = wd.find_element_by_class_name('spnew_bf cmm_pg_next on')
#*[@id="place-main-section-root"]/section[1]/div/div[2]/div[3]/a[2]
