from selenium import webdriver #从 selenium 包导入了 webdriver 模块。webdriver 是用来实现浏览器自动化的。
from selenium.webdriver.chrome.options import Options #允许我们改变default的selenium的行为,比如开启headless mode
from selenium.webdriver.chrome.service import Service #从 selenium.webdriver.chrome.service 包导入了 Service 类。该类主要用于启动和停止 ChromeDriver。
import pandas as pd
#below are the lib needed to achieve this
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()  #get the current date
# MM/DD/YYYY
month_day_year = now.strftime("%m%d%Y")  #string from time, is used to get the time in String datatype

options = Options() 
options.headless = True

website = "https://www.thesun.co.uk/sport/football/"
driver = webdriver.Chrome(service=Service('/Users/sunyueqian/Desktop/chrome-mac-arm64/chromedriver-mac-arm64/chromedriver'),options=options) 
driver.get(website) 

containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title_elements = container.find_elements(by="xpath", value='./a/h3')
    subtitle_elements = container.find_elements(by="xpath", value='./a/p')
    link_elements = container.find_elements(by="xpath", value='./a')
    
    if title_elements and subtitle_elements and link_elements:
        title = title_elements[0].text
        subtitle = subtitle_elements[0].text
        link = link_elements[0].get_attribute("href")
        
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)


my_dict = {'my_title': titles, 'my_subtitle': subtitles, 'my_link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f"headlin-{month_day_year}.csv"

#这个用来避免手动输入“/”或者"\"在不同操作系统上造成的问题，最好是直接交给os.path来操作
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv(final_path)

driver.quit()
