from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)


url = 'http://t66y.com/thread0806.php?fid=25&page='




csv_file = open('avlist.csv','w',newline='',errors='ignore')
writer = csv.writer(csv_file)
writer.writerow(['标题','链接','页码'])
i = 1
while i<101:

    driver.get(url + str(i))

    datas = driver.find_elements_by_css_selector("tr.tr3.t_one.tac")
 
    for data in datas:
        TitleList = data.find_element_by_tag_name("h3")
        Title = TitleList.find_element_by_tag_name("a").text
        Link = TitleList.find_element_by_tag_name("a").get_attribute("href")
        print(Title,Link)
        writer.writerow([Title,Link,i])


    i += 1

csv_file.close();