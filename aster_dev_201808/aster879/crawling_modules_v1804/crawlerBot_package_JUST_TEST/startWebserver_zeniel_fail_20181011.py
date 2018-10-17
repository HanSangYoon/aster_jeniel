#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

from aster_dev_201808.aster879.crawling_modules_v1804.crawlerBot_package_JUST_TEST.NotUsingJSONDATAType import facebookCrawlerBot_zeniel_linux_fail_20181011 as snsScrapBot

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'origin, x-requested-with, content-type, accept')
        self.send_header('Pragma', 'No-Cache')
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('Expires', 'Sun, 01 Jan 2014 00:00:00 GMT')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Cache-Control', 'post-check=0, pre-check=0, FALSE')
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()


    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.parsed_POST_data(post_data)

    def parsed_POST_data(self, post_data):
        #getParam = urllib.parse.unquote(post_data.decode('utf-8'))
        getParam = urllib.parse.unquote(post_data.decode())

        print('입력한 데이터: ', getParam)
        #http://172.30.1.33:8000/kakao_story=https%3A%2F%2Fstory.kakao.com%2F_9W0DZ3&naver_blog=https%3A%2F%2Fblog.naver.com%2Ftramper2&facebook=https%3A%2F%2Fwww.facebook.com%2Fdanny.woo.33&instagram=XXXX&username=%EA%B9%80%ED%83%9C%ED%98%B8
        # kakao_story=https%3A%2F%2Fstory.kakao.com%2F_9W0DZ3&
        # naver_blog=https%3A%2F%2Fblog.naver.com%2Ftramper2&
        # facebook=https%3A%2F%2Fwww.facebook.com%2Fdanny.woo.33&
        # instagram=&
        # username=%EA%B9%80%ED%83%9C%ED%98%B8

        userData = {}

        if getParam is not None:
            snsURL_ADDR_fromWeb = getParam.split('&')
            #print(snsURL_ADDR_fromWeb[0], snsURL_ADDR_fromWeb[1], snsURL_ADDR_fromWeb[2], snsURL_ADDR_fromWeb[3], snsURL_ADDR_fromWeb[4])
            #kakao_story=XXXX&naver_blog=XXXX&facebook=XXXX&instagram=XXXX&username=XXXX
            print('&로 나눠진 데이터 리스트:', snsURL_ADDR_fromWeb)

            if snsURL_ADDR_fromWeb[0]:
                kakaoStory_USERURL_tot= snsURL_ADDR_fromWeb[0].split("=")[1].replace(" ", "")
                try:
                    print('kakaoStory SNS 주소가 존재합니다.')
                    kakaoStory_USERURL_pre = kakaoStory_USERURL_tot.split('//')[1]
                    kakaoStory_USERURL = kakaoStory_USERURL_pre.split('/')[1]
                    userData['kakao_story'] = kakaoStory_USERURL
                except Exception as e:
                    print('kakaoStory SNS 주소가 존재하지 않습니다.', e)
                    kakaoStory_USERURL = None
            else:
                print('kakaoStory SNS 주소가 존재하지 않습니다.')
                kakaoStory_USERURL = None

            naverBlog_USERURL = None

            if snsURL_ADDR_fromWeb[2]:

                if 'profile' in snsURL_ADDR_fromWeb[2]:
                    print('문자형식의 페이지ID 값을 갖지 않은 사용자 입니다.')

                    facebook_USERURL_tot = snsURL_ADDR_fromWeb[2].split("=")[2].replace(" ", "")
                    facebook_USERURL = facebook_USERURL_tot

                    print('1', facebook_USERURL_tot)
                    print('2', facebook_USERURL)

                    userData['facebook'] = facebook_USERURL

                else:
                    facebook_USERURL_tot = snsURL_ADDR_fromWeb[2].split("=")[1].replace(" ", "")

                    try:
                        print('facebook SNS 주소가 존재합니다.')
                        facebook_USERURL_pre = facebook_USERURL_tot.split('//')[1]
                        facebook_USERURL = facebook_USERURL_pre.split('/')[1]
                        userData['facebook'] = facebook_USERURL
                    except Exception as e:
                        print('facebook SNS 주소가 존재하지 않습니다.', e)
                        facebook_USERURL = None

            else:
                print('facebook SNS 주소가 존재하지 않습니다.')
                facebook_USERURL = None


            if snsURL_ADDR_fromWeb[3]:
                instagram_USERURL_tot= snsURL_ADDR_fromWeb[3].split("=")[1].replace(" ", "")

                try:
                    instagram_USERURL_pre = instagram_USERURL_tot.split('//')[1]
                    instagram_USERURL = instagram_USERURL_pre.split('/')[1]
                    print('instagram SNS 주소가 존재합니다.')
                    userData['instagram_USERURL'] = instagram_USERURL
                except Exception as e:
                    print('instagram SNS 주소가 존재하지 않습니다.', e)
                    instagram_USERURL = None
            else:
                print('instagram SNS 주소가 존재하지 않습니다.')
                instagram_USERURL = None

            if snsURL_ADDR_fromWeb[4]:
                print('사용자 이름이 존재합니다.', snsURL_ADDR_fromWeb[4])
                try:
                    userName = snsURL_ADDR_fromWeb[4].split("=")[1].replace(" ", "")
                    userData['username'] = userName
                except Exception as e:
                    print('사용자 이름이 존재하지 않습니다.', e)
                    userName = None
            else:
                print('사용자 이름이 존재하지 않습니다.')
                userName = None

            print('전달 받은 계정정보 값 :', kakaoStory_USERURL, facebook_USERURL, instagram_USERURL, userName)
            print('user Data : ', userData)

            tot_TSCORE = 0
            tot_CSCORE = 0
            tot_MSCORE = 0

            #FACEBOOK
            if facebook_USERURL is not None:
                try:
                    #CrawlingByFacebookCrawlBot
                    ResultDict1 = snsScrapBot.login_facebook(self, 1, facebook_USERURL, userName, 'zeniel')

                    if ResultDict1['trueOrFalse'] == True:
                        print('페이스북 크롤링 성공, Score : ', ResultDict1['tcmScore']['T_SCORE'], ResultDict1['tcmScore']['C_SCORE'], ResultDict1['tcmScore']['M_SCORE'])

                        tot_TSCORE += ResultDict1['tcmScore']['T_SCORE']
                        tot_CSCORE += ResultDict1['tcmScore']['C_SCORE']
                        tot_MSCORE += ResultDict1['tcmScore']['M_SCORE']

                        print('facebook : ', tot_TSCORE, tot_CSCORE, tot_MSCORE)

                        jsonData = {'TSCORE': ResultDict1['tcmScore']['T_SCORE'], 'CSCORE':ResultDict1['tcmScore']['C_SCORE'], 'MSCORE':ResultDict1['tcmScore']['M_SCORE'], 'DETAILINFO':ResultDict1['tcmScore']['DETAIL'] }
                        data = json.dumps(jsonData).encode("utf-8")
                        data1 = json.dumps(jsonData).encode("utf-16")
                        print('data 값:', data)
                        self.wfile.write(data)
                        print('data  전달 끝')

                        return
                    else:
                        print('페이스북 크롤링이 내부 요인에 의해 결과 값이 제대로 전달되지 않았습니다.')

                except Exception as ex_facebook:
                    print('페이스북 크롤링이 내부 요인에 의해 중지 되었습니다. -> ', ex_facebook)

                    try:
                        ResultDict2 = snsScrapBot.login_facebook(self, 1, facebook_USERURL, userName, 'zeniel')
                        if ResultDict2 == True:
                            print('2차 페이스북 크롤링 성공, Score : ', ResultDict2['tcmScore'])
                            tot_TSCORE += ResultDict2['tcmScore']['T_SCORE']
                            tot_CSCORE += ResultDict2['tcmScore']['C_SCORE']
                            tot_MSCORE += ResultDict2['tcmScore']['M_SCORE']

                            data = json.dumps(ResultDict2['tcmScore'])
                            print('data 값:', data)
                            self.wfile.write(data).encode()
                            print('data  전달 끝')

                            return
                        else:
                            print('2차 페이스북 크롤링이 내부 요인에 의해 결과 값이 제대로 전달되지 않았습니다.')
                    except Exception as ex_facebook2:
                        print('2차 페이스북 크롤링이 내부 요인에 의해 중지 되었습니다. -> ', ex_facebook2)


        else:
            print("전달받은 데이터가 없습니다. ")

#zeniel
#httpd = HTTPServer(('172.30.1.211', 8000), SimpleHTTPRequestHandler)
#10.0.2.15
httpd = HTTPServer(('10.0.2.15', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()