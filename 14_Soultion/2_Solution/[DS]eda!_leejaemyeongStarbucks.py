import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


import folium
rc('font', family = 'Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
#get_ipython().run_line_magic("matplotlib", "inline")

starbucks_url = "https://www.starbucks.co.kr/store/store_map.do"

starbucks_driver = webdriver.Chrome('./chromedriver.exe')

starbucks_driver.implicitly_wait(5)

starbucks_driver.get(starbucks_url)
time.sleep(2)
starbucks_driver.find_element(By.CSS_SELECTOR,
    '#container > div > form > fieldset > div > section > article.find_store_cont > article > header.loca_search'
).click()
time.sleep(2)

starbucks_driver.find_element(By.CSS_SELECTOR,'#container > div > form > fieldset > div > section > article.find_store_cont > article > article:nth-child(4) > div.loca_step1 > div.loca_step1_cont > ul > li:nth-child(1) > a').click()
time.sleep(2)

starbucks_driver.find_element(By.CSS_SELECTOR,'#mCSB_2_container > ul > li:nth-child(1) > a').click()
time.sleep(2)
starbucks_page = starbucks_driver.page_source

starbucks_soup = BeautifulSoup(starbucks_page,'html.parser')

starbucks_content = starbucks_soup.select("#mCSB_3_container > ul > li")
#starbucks_content =soup.find('div','#mCSB_3_container')
#print(starbucks_content)

# one = starbucks_content[0].select_one('strong').text[:-2]
#two = starbucks_content[1].select_one('p').text[:-9]
# three = starbucks_content[0].select_one('p').text.split(" ")[1]
time.sleep(1)
starbucks_list = []

for s_data in starbucks_content:
    s_name = s_data.select_one('strong').text[:-2]
    s_address = s_data.select_one('p').text[:-9]
    s_gu_name = s_data.select_one('p').text.split(" ")[1]

    s_data_frame = {
        "이름" : s_name,
        "주소" : s_address,
        "구" : s_gu_name
    }
    starbucks_list.append(s_data_frame)

time.sleep(1)
starbucks_driver.quit()
#print(len(starbucks_list))

df_starbucks = pd.DataFrame(starbucks_list)
df_starbucks.head(599)
#print(df_starbucks)

ediya_url = 'https://www.ediya.com/contents/find_store.html'

ediya_driver = webdriver.Chrome('chromedriver.exe')

ediya_driver.implicitly_wait(5)

ediya_driver.get(ediya_url)

ediya_gu_list = list(df_starbucks["구"].unique())
#print(ediya_gu_list)
ediya_driver.find_element(By.CSS_SELECTOR,'#contentWrap > div.contents > div > div.store_search_pop > ul > li:nth-child(2) > a').click()
time.sleep(1)
ediya_list = []

for gu in ediya_gu_list:
    ediya_driver.find_element(By.CSS_SELECTOR, '#keyword')
    time.sleep(1)

    ediya_driver.find_element(By.CSS_SELECTOR, '#keyword').clear()
    time.sleep(1)

    ediya_driver.find_element(By.CSS_SELECTOR, '#keyword').send_keys(f'서울 {gu}')
    time.sleep(1)

    ediya_driver.find_element(By.CSS_SELECTOR, '#keyword_div > form > button').click()
    time.sleep(1)

    ediya_page = ediya_driver.page_source
    ediya_soup = BeautifulSoup(ediya_page,'html.parser')
    ediya_info = ediya_soup.select('#placesList > li')
    #print(ediya_info)
    # dl = ul.find_all("dl")

    for e_data in ediya_info:
        e_name = e_data.select_one('dt').text
        e_address = e_data.select_one('dd').text
        e_gu_name = e_data.select_one('dd').text.split(" ")[1]

        e_data_frame = {
            "이름": e_name,
            "주소": e_address,
            "구": e_gu_name
        }
        ediya_list.append(e_data_frame)

ediya_driver.find_element(By.CSS_SELECTOR,'#keyword').clear()
time.sleep(0.5)
#print(ediya_list)
ediya_driver.quit()


df_ediya = pd.DataFrame(ediya_list)
df_ediya.head()

df_starbucks["brand"] = "starbucks"
df_ediya["brand"] = "ediya"
df_total = pd.concat([df_ediya, df_starbucks])
df_total = df_total.reset_index(drop=True)
print(df_total)




