from selenium import webdriver
import time
 
url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LSD&mid=shm&sid1=100&oid=422&aid=0000430957'
 
#웹 드라이버
driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(30)
driver.get(url)
 
#더보기 계속 클릭하기
while True:
    try:
        btn_more = driver.find_element_by_css_selector('a.u_cbox_btn_more')
        btn_more.click()
        # time.sleep(1)
    except:
        break
 
 
#기사제목 추출
article_head = driver.find_elements_by_css_selector('div.article_info > h3 > a')
print("기사 제목 : " + article_head[0].text)
 
#기사시간 추출
article_time = driver.find_elements_by_css_selector('div.sponsor > span.t11')
print("기사 등록 시간 : " + article_time[0].text)

# 성비와 연령대 추출
per = driver.find_elements_by_css_selector('span.u_cbox_chart_per')
 
print("남자 성비 : " + per[0].text)
print("여자 성비 : " + per[1].text)
print("10대 : " + per[2].text)
print("20대 : " + per[3].text)
print("30대 : " + per[4].text)
print("40대 : " + per[5].text)
print("50대 : " + per[6].text)
print("60대 이상 : " + per[7].text)
