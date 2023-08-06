from selenium import webdriver #从 selenium 包导入了 webdriver 模块。webdriver 是用来实现浏览器自动化的。
from selenium.webdriver.chrome.options import Options #允许我们改变default的selenium的行为,比如开启headless mode
from selenium.webdriver.chrome.service import Service #从 selenium.webdriver.chrome.service 包导入了 Service 类。该类主要用于启动和停止 ChromeDriver。
import pandas as pd


#headless mode:
options = Options() #让自动化selenium在background运行，不要再打卡一个网页
options.headless = True

website = "https://www.thesun.co.uk/sport/football/"
driver = webdriver.Chrome(service=Service('/Users/sunyueqian/Desktop/chrome-mac-arm64/chromedriver-mac-arm64/chromedriver'),options=options) 
#创建了一个 webdriver.Chrome 对象,它会启动一个新的 Chrome 浏览器窗口。你将使用这个对象来与浏览器进行交互。 后面是chrome driver的路径
driver.get(website) #导航到 website 变量所定义的 URL。



#find_element只会返回第一个值,但是find_elements()会返回全部值在一个list中,所以我们可以遍历这个list
containers = driver.find_elements(by="xpath",value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

#driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]/a/h2')
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

'''代码尝试寻找每个container元素中的 <a> 标签下的 <h3> 和 <p> 元素。
这是通过调用 container.find_elements 方法并使用 XPath 查询实现的。这个查询的值 './a/h3' 和 './a/p' 分别代表查找当前元素('./')的子元素 <a> 下的 <h3> 和 <p> 标签。

接着,代码尝试在每个 container 元素中寻找 <a> 标签,并获取它的 href 属性,也就是该链接的URL。

如果这三个元素(title_elements,subtitle_elements 和 link_elements)都存在,
那么它们的第一个元素(即索引为0的元素,因为find_elements返回的是一个列表)将被分别提取为标题,副标题和链接。
注意,text 方法用于获取元素的文本内容,get_attribute("href") 方法用于获取元素的 href 属性值,也就是链接的URL。

然后,这些提取出来的标题,副标题和链接将被添加到之前初始化的三个列表(titles,subtitles 和 links)中。

'''

my_dict = {'my_title': titles, 'my_subtitle': subtitles, 'my_link': links}
df_headlines = pd.DataFrame(my_dict)
#df_headlines.to_csv("headline.csv")
df_headlines.to_csv("headline_headless.csv")

driver.quit()
