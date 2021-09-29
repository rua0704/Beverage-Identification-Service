# selenium, requests
from selenium import webdriver
import time
import urllib.request
import os

def main():
    driver = webdriver.Chrome()
    driver.get("http://cu.bgfretail.com/product/product.do?category=product&depth2=4&depth3=6")
    f = open("nameList.txt", "w")

    # 스크롤을 먼저 다 내린다
    SCROLL_PAUSE_TIME = 8.0

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # 로딩 되는 동안 대기
        time.sleep(SCROLL_PAUSE_TIME)

        # 스크롤 내리기
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Calculate new scroll height and compare with last scroll height 이전 높이와 다음 높이가 같다면 스탑
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try: # 더보기 버튼 클릭
                driver.find_element_by_css_selector("#dataTable > div.prodListBtn > div.prodListBtn-w > a").click()
            except:
                break
        last_height = new_height

    # 사진 선택
    container = driver.find_elements_by_css_selector("#dataTable > div.prodListWrap > ul > li")

    count = 0

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating' + directory)

    createFolder("./" + "download")
    nameList = []

    for item in container:
        # 몇개 음료수 수집
        if count > 100:
            break
        try:
            src = item.find_element_by_css_selector("div.photo > a > img").get_attribute("src")
            name = item.find_element_by_css_selector("p.prodName > span").text
            nameList.append(name)
            createFolder("./download/" + name)
            urllib.request.urlretrieve(src, "./download/" + name + "/" + str(0) + ".jpg")
            count += 1
        except Exception as e:
            print(e)
            pass
    #
    driver.close()

    f.write(','.join(nameList))
    f.close()

    ## 셀레니움 이용하여 상품명 가져오기 끝