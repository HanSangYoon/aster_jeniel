#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import os

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def __getHTMLDoc_beautifulSoup4(driver, URL):

    driver.get(URL)

    html_src_chrome = driver.page_source
    soupHTMLDoc = bs(html_src_chrome, 'html.parser')

    return soupHTMLDoc


def autoScroller(driver, URL):

    print(driver.current_url)
    # 게시글에서 좋아요 표시 갯수, 댓글 수 등의 정보 추출 >>  AUTO SCROLL 기능 필요
    SCROLL_PAUSE_TIME = 0.5

    # 화면 길이 만큼 나눠 autoScroll 하고 각 페이지마다 데이터 가져오기
    #autoScrolled_data_soup_html = bs()

    last_height = driver.execute_script("return document.body.scrollHeight")
    # 화면 사이즈 생성하기(15번의 새로고침이 있을 정도로만 데이터 추출)
    for cyc in range(0, 3):
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
        # autoScroll crawling data 가져오기
    autoScrolled_data_soup_html = bs(driver.page_source, 'html.parser')

    return autoScrolled_data_soup_html



chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

prefs = {}
prefs['profile.default_content_setting_values.notifications'] = 2
chrome_options.add_experimental_option('prefs', prefs)
#driver_chrome = r"C:\dev_tenspace\git_aster\aster_jeniel\aster_dev_201808\chromedriver.exe"


#abspath = os.path.abspath("./facebook_test_photos.py")
#현재 실행 경로를 구함. 여기서부터 상대 경로를 구해야 함.
abspath = os.getcwd()
print('##:', abspath)

relative_path2 = os.path.relpath(r"C:\dev_tenspace\git_aster\aster_jeniel\aster_dev_201808\chromedriver.exe", abspath)
                                #..\..\..\..\..\chromedriver.exe
                                #C:\dev_tenspace\git_aster\aster_jeniel\aster_dev_201808
                                #C:\dev_tenspace\git_aster\aster_jeniel\aster_dev_201808\aster879\crawling_modules_v1804\crawlerBot_package_JUST_TEST\For_test\facebook_test_photos.py
print('@@@@:    ', relative_path2)

abspath2 = os.path.abspath(relative_path2)
print(abspath2)

driver_chrome = relative_path2

# go to Google and click the I'm Feeling Lucky button
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driver_chrome)

# url
driver.get('https://www.facebook.com')

user_id = '01027746254'
user_pass = 'Gkstkddbs4$'

# id and password
driver.find_element_by_name('email').send_keys(user_id)
driver.find_element_by_name('pass').send_keys(user_pass)

# try login : 로그인 버튼의 id 값이 아래의 범위 내에서 무작위로 변경되기 때문에 이에 대한 대응차원임.
try:
    driver.find_element_by_xpath('// *[ @ id = "u_0_2"]').click()
    login_or_not = True
except Exception as ex1:
    print('로그인 버튼 id 값이 u_0_2 가 아닙니다.', ex1)

    try:
        driver.find_element_by_xpath('// *[ @ id = "u_0_3"]').click()
        login_or_not = True
    except Exception as ex2:
        print('로그인 버튼 id 값이 u_0_3 이 아닙니다.', ex2)

        try:
            driver.find_element_by_xpath('// *[ @ id = "u_0_4"]').click()
            login_or_not = True
        except Exception as ex3:
            print('로그인 버튼 id 값이 u_0_4 가 아닙니다.', ex3)

            try:
                driver.find_element_by_xpath('// *[ @ id = "u_0_b"]').click()
                login_or_not = True
            except Exception as ex4:
                print('로그인 버튼 id 값이 u_0_b 가 아닙니다.', ex4)

                try:
                    driver.find_element_by_xpath('// *[ @ id = "u_0_d"]').click()
                    login_or_not = True
                except Exception as ex5:
                    print('로그인 버튼 id 값이 u_0_d 가 아닙니다.', ex5)

                    try:
                        driver.find_element_by_xpath('// *[ @ id = "u_0_e"]').click()
                        login_or_not = True
                    except Exception as ex6:
                        print('로그인 버튼 id 값이 u_0_e 가 아닙니다.', ex6)

                        try:
                            driver.find_element_by_xpath('// *[ @ id = "u_0_f"]').click()
                            login_or_not = True
                        except Exception as ex7:
                            print('로그인 버튼 id 값이 u_0_f 가 아닙니다.', ex7)

                            try:
                                driver.find_element_by_xpath('// *[ @ id = "u_0_a"]').click()
                                login_or_not = True
                            except Exception as ex8:
                                print('로그인 버튼 id 값이 u_0_a 가 아닙니다.로그인 실패입니다. 소스를 다시 분석해야 합니다.', ex8)
                                login_or_not = False

facebookPageID = 'kpokem'

def findPhoto(facebookPageID):
    #사용자 나온 사진 정보 추가
    driver.get('https://www.facebook.com/' + facebookPageID + '/photos_of')
    # photos_of_html = driver.page_source
    # photos_of_soup = bs(photos_of_html, 'html.parser')
    photos_of_soup = autoScroller(driver, 'https://www.facebook.com/' + facebookPageID + '/photos_of')

    time.sleep(1)
    try:
        photos_of_cnt = photos_of_soup.select('#pagelet_timeline_medley_photos > div:nth-of-type(2) > div:nth-of-type(1) > ul > li')
        print('photos_of_cnt:', len(photos_of_cnt))

    except Exception as e:
        print('사용자 사진 정보가 공개되지 않았습니다. ')



    #모든 사진 정보 추가
    driver.get('https://www.facebook.com/' + facebookPageID + '/photos_all')
    # photos_all_html = driver.page_source
    # photos_all_soup = bs(photos_all_html, 'html.parser')
    photos_all_soup = autoScroller(driver, 'https://www.facebook.com/' + facebookPageID + '/photos_all')

    time.sleep(1)
    try:
        photos_all_cnt = photos_all_soup.select('#pagelet_timeline_medley_photos > div:nth-of-type(2) > div:nth-of-type(1) > ul > li')
        print('photos_all_cnt:', len(photos_all_cnt))

    except Exception as e:
        print('모든사진에 대한 정보가 공개되지 않았습니다. ')


    #사진첩 정보
    driver.get('https://www.facebook.com/' + facebookPageID + '/photos_albums')
    # photos_all_html = driver.page_source
    # photos_all_soup = bs(photos_all_html, 'html.parser')
    photos_albums_soup = autoScroller(driver, 'https://www.facebook.com/' + facebookPageID + '/photos_albums')
    print(driver.current_url)

    time.sleep(1)
    try:
        photos_albums_cnt_div = photos_albums_soup.select(
            '#pagelet_timeline_medley_photos > div:nth-of-type(2) > div > div')
        time.sleep(1)
        print('DIV 개수', len(photos_albums_cnt_div))


        for divlength in range(len(photos_albums_cnt_div)):
            photos_albums_cnt_tr = photos_albums_soup.select(
                '#pagelet_timeline_medley_photos > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(' + str(divlength + 1) + ') > table > tbody > tr')
            print('photos_all_cnt:', len(photos_albums_cnt_tr))

            time.sleep(1)

            albumKindCnt = 0
            i = 0
            for trlength in range(len(photos_albums_cnt_tr)):
                photos_albums_cnt_td = photos_albums_soup.select(
                    '#pagelet_timeline_medley_photos > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(1) > table > tbody > tr:nth-of-type('+ str(trlength+1)+') > td')
                i += 1
                print('photos_all_cnt', i, len(photos_albums_cnt_td))

                albumKindCnt += len(photos_albums_cnt_td)

        print('사진첩 종류 개수 :', albumKindCnt)
    except Exception as e:
        print('사진첩에 대한 정보가 공개되지 않았습니다. ', e)


    return len(photos_of_cnt), len(photos_all_cnt),albumKindCnt
returnValue = findPhoto(facebookPageID)

print('return:', returnValue)
print(returnValue[2])

