
#!/usr/bin/python
import pymysql

'''
Python에서 MySQL에 있는 데이타를 사용하는 일반적인 절차는 다음과 같다.

1. PyMySql 모듈을 import 한다
2. pymysql.connect() 메소드를 사용하여 MySQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정한다.
3. DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을 관리하는데 사용되는데, 만약 DB 자체가 커서를 지원하지 않으면, Python DB API에서 이 커서 동작을 Emulation 하게 된다.
4. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.
5. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용한다.
6. 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이타를 확정 갱신한다.
7. Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.
'''

class DatabaseConnection_jeniel:
    def __init__(self):

        try:
            self.connection = pymysql.connect(host='uml.kr', port=3366,
                       user='just_aster_dba', password='!just716811',
                       db='just', charset='utf8')

            self.connection.autocommit = True
            self.cursor = self.connection.cursor()

            print('DB connection completed')

        except:
            print('Cannot connect to Database')

    def create_table(self):
        create_table_query = "CREATE TABLE `facebook_crawled_just` (\
                                `no_index` INT(11) NOT NULL AUTO_INCREMENT,\
                                `insertedTime` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
                                `userName` VARCHAR(50) NULL DEFAULT NULL,\
                                `birthday` VARCHAR(50) NULL DEFAULT NULL,\
                                `birthday_luna` VARCHAR(50) NULL DEFAULT NULL,\
                                `sex` VARCHAR(50) NULL DEFAULT NULL,\
                                `bloodType` VARCHAR(50) NULL DEFAULT NULL,\
                                `addr` VARCHAR(100) NULL DEFAULT NULL,\
                                `facebookUrl` VARCHAR(50) NULL DEFAULT NULL,\
                                `website` VARCHAR(50) NULL DEFAULT NULL,\
                                `snsLink` VARCHAR(50) NULL DEFAULT NULL,\
                                `religion` VARCHAR(50) NULL DEFAULT NULL,\
                                `cellPhone` VARCHAR(50) NULL DEFAULT NULL,\
                                `introduceText` VARCHAR(200) NULL DEFAULT NULL,\
                                `profileTotCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `profileTotInfo` VARCHAR(300) NULL DEFAULT NULL,\
                                `friendsCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `likePeopleCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `imgLikeCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `vodCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `picCnt` VARCHAR(50) NULL DEFAULT NULL,\
                                `tscore` VARCHAR(50) NULL DEFAULT NULL,\
                                `cscore` VARCHAR(50) NULL DEFAULT NULL,\
                                `mscore` VARCHAR(50) NULL DEFAULT NULL,\
                                PRIMARY KEY (`no_index`)\
                            )\
                            ENGINE=InnoDB\
                            ;"

        self.cursor.execute(create_table_query)
        self.connection.close()

    #str(ResultDict['해당월게시물개수']),  # thisMnthArticleCnt
    #str(ResultDict['전월게시물개수'])  # preMnthArticleCnt
    '''
                    ResultDict['사용자이름'],
                ResultDict['페이스북페이지ID'],
                ''.join(ResultDict['전체기본정보']),
                '_'.join(ResultDict['전체연락처정보']),
                '_'.join(ResultDict['웹사이트및소셜링크정보']),
                '_'.join(ResultDict['소개글']),
                str(ResultDict['프로필게시개수']),
                ResultDict['전체프로필정보'],
                str(ResultDict['친구수']),
                str(ResultDict['좋아요클릭한사람수']),
                str(ResultDict['이미지에좋아요클릭한사람수']),
                str(ResultDict['동영상수']),
                str(ResultDict['사진수']),
                str(ResultDict['T_SCORE']),
                str(ResultDict['C_SCORE']),
                str(ResultDict['M_SCORE']),
                '_'.join(ResultDict['DETAIL']),
                str(ResultDict['모든친구']),  # allFrndCnt
                str(ResultDict['함께아는친구']),  # knowEachFrnd
                str(ResultDict['최근추가한친구']),  # latestAddFrnd
                str(ResultDict['대학교']),  # univFrnd
                str(ResultDict['거주지']),  # homeFrnd
                str(ResultDict['출신지']),  # homeTwnFrnd
                str(ResultDict['팔로워']),  # fllwerCnt
                str(ResultDict['좋아요모두']),  # likeHobbyAllCnt
                str(ResultDict['영화']),  # movieLikeCnt
                str(ResultDict['TV프로그램']),  # tvLikeCnt
                str(ResultDict['음악']),  # musicLikeCnt
                str(ResultDict['책']),  # bookLikeCnt
                str(ResultDict['스포츠팀']),  # sportsTemaLikeCnt
                str(ResultDict['음식점']),  # foodPlaceCnt
                str(ResultDict['앱과게임']),  # appAndGamesCnt
                str(ResultDict['장소']),  # visitedPlc
                str(ResultDict['도시']),  # visitedCity
                str(ResultDict['최근에가본곳']),  # recentVisitPlc
                str(ResultDict['이벤트내용개수']),  # evntCnt
                str(ResultDict['이벤트내용']),  # eventContents
                str(ResultDict['봤어요']),  # sawItCnt
                str(ResultDict['영화']),  # sawMovieCnt
                str(ResultDict['영화내용개수']),  # sawMovieContentCnt
                str(ResultDict['영화제목']),  # sawMovieTitle
                str(ResultDict['댓글개수']),  # replyCnt
                str(ResultDict['댓글내용']),  # replyContents
                str(ResultDict['게시글좋아요수']),  # articleLikeCnt
                str(ResultDict['게시글공유수']),  # articleShareCnt
                str(ResultDict['평균댓글개수']),  # avgReplyCnt
                str(ResultDict['평균덧글개수']),  # avgReplyAndReply
                str(ResultDict['전체긍정어사용빈도']),  # gdExpssCnt
                str(ResultDict['평균긍정어사용비율']),  # avgGdExpssRate
                str(ResultDict['개요항목개수']),  # aboutInfoCnt
                str(ResultDict['해당월게시글개수']),    #thisMnthArticleCnt
                str(ResultDict['전월게시글개수']),      #preMnthArticleCnt
				str(ResultDict['운영년수']),			#arrangeYears
                str(ResultDict['전화번호']),          #cellPhone
                str(ResultDict['주소']),             #addr
                str(ResultDict['소셜링크']),          #snsLink
                str(ResultDict['웹사이트']),         #website
                str(ResultDict['생일']),             #birthday
                str(ResultDict['음력생일'])         #birthday_luna
    '''

    #INSERT facebook
    def insert_record_origin_version(self, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17,
                                     f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45,
                                     f46, f47, f48, f49, f50, f51, f52, f53, f54, f55, f56, f57, f58, f59):
        try:
            insert_command = "INSERT INTO facebook_crawled_just (" \
                             "userName, facebookUrl, basicInfo_tot, contctInfo_tot, websiteSnsInfo, " \
                             "introduceText, profileTotCnt, profileTotInfo, friendsCnt, likePeopleCnt, " \
                             "imgLikeCnt, vodCnt, picCnt, fb_tscore, fb_cscore, " \
                             "fb_mscore, detail_info, allFrndCnt,knowEachFrnd,latestAddFrnd," \
                             "univFrnd,homeFrnd,homeTwnFrnd,fllwerCnt,likeHobbyAllCnt," \
                             "movieLikeCnt,tvLikeCnt,musicLikeCnt,bookLikeCnt,sportsTemaLikeCnt," \
                             "foodPlaceCnt,appAndGamesCnt,visitedPlc,visitedCity,recentVisitPlc," \
                             "evntCnt,eventContents,sawItCnt,sawMovieCnt,sawMovieContentCnt," \
                             "sawMovieTitle,replyCnt,replyContents,articleLikeCnt,articleShareCnt," \
                             "avgReplyCnt,avgReplyAndReply,gdExpssCnt,avgGdExpssRate,aboutInfoCnt," \
                             "thisMnthArticleCnt,preMnthArticleCnt,arrangeYears," \
                             "cellPhone,addr,snsLink,website,birthday,birthday_luna) VALUES('" \
                             + f1 + "','" + f2 + "','" + f3 + "','" + f4 + "','" + f5 + "','" + f6 + "','"\
                             + f7 + "','" + f8 + "','" + f9 + "','" + f10 + "','" + f11 + "','" + f12 + "','"\
                             + f13 + "','" + f14 + "','" + f15 + "', '" + f16 + "', '" + f17 + "','"\
                             + f18 + "','" + f19 + "','" + f20 + "','" + f21 + "','" + f22 + "','" + f23 + "','" \
                             + f24 + "','" + f25 + "','" + f26 + "','" + f27 + "','" + f28 + "','" + f29 + "','" \
                             + f30 + "','" + f31 + "','" + f32 + "', '" + f33 + "', '" + f34 + "','" + f35 + "','" \
                             + f36 + "','" + f37 + "','" + f38 + "', '" + f39 + "', '" + f40 + "','" + f41 + "','" \
                             + f42 + "','" + f43 + "','" + f44 + "', '" + f45 + "', '" + f46 + "', '" + f47 + "', '" \
                             + f48 + "', '" + f49 + "', '" + f50 + "', '" + f51 + "', '" + f52 + "', '" + f53 + "', '" \
                             + f54 + "','" + f55 + "','" + f56 + "','" + f57 + "','" + f58 + "','" + f59 + "' )"

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print(e)

    '''
    
    
    
    
    
                str(ResultDict['사용자이름']),                   #userName
                str(ResultDict['페이스북페이지ID']),		        #facebookUrl
                str(ResultDict['전체기본정보']),			        #basicInfo_tot
                str(ResultDict['전체연락처정보']),			    #contctInfo_tot
                str(ResultDict['웹사이트및소셜링크정보']),		    #websiteSnsInfo
                str(ResultDict['소개글']),				        #introduceText
                str(ResultDict['프로필게시개수']),			    #profileTotCnt
                str(ResultDict['전체프로필정보']),			    #profileTotInfo                
                str(ResultDict['친구수']),				        #friendsCnt
                str(ResultDict['좋아요(image)__표시전체갯수']),   #imgLikeCnt
                str(ResultDict['동영상수']),				        #vodCnt
                str(ResultDict['사진수']),				        #picCnt                
                str(ResultDict['팔로워']),				        #fllwerCnt
                str(ResultDict['DETAIL']),                      #detail_info
                str(ResultDict['좋아요__사람전체명수']),		    #likePeopleCnt                
                str(ResultDict['생일']),					        #birthday
                str(ResultDict['음력생일']),				        #birthday_luna
                str(ResultDict['성별']),					        #sex
                str(ResultDict['혈액형']),				        #bloodType
                str(ResultDict['주소']),					        #addr
                str(ResultDict['웹사이트']),				        #website
                str(ResultDict['소셜링크']),				        #snsLink
                str(ResultDict['종교관']),				        #religion                
                str(ResultDict['휴대폰']),				        #cellPhone           
                str(ResultDict['모든친구']),				        #allFrndCnt
                str(ResultDict['함께아는친구']),			        #knowEachFrnd
                str(ResultDict['최근추가한친구']),			    #latestAddFrnd
                str(ResultDict['대학교']),				        #univFrnd
                str(ResultDict['거주지']),				        #homeFrnd
                str(ResultDict['출신지']),				        #homeTwnFrnd                
                str(ResultDict['고등학교']),				        #highschoolFrnd
                str(ResultDict['좋아요모두']),				    #likeHobbyAllCnt
                str(ResultDict['영화']),					        #movieLikeCnt
                str(ResultDict['TV프로그램']),				    #tvLikeCnt
                str(ResultDict['음악']),					        #musicLikeCnt
                str(ResultDict['책']),					        #bookLikeCnt
                str(ResultDict['스포츠팀']),				        #sportsTemaLikeCnt
                str(ResultDict['음식점']),				        #foodPlaceCnt
                str(ResultDict['앱과게임']),				        #appAndGamesCnt
                str(ResultDict['장소']),					        #visitedPlc
                str(ResultDict['도시']),					        #visitedCity
                str(ResultDict['최근에가본곳']),			        #recentVisitPlc
                str(ResultDict['이벤트내용개수']),			    #evntCnt
                str(ResultDict['이벤트내용']),				    #eventContents
                str(ResultDict['봤어요']),				        #sawItCnt
                str(ResultDict['영화내용개수']),			        #sawMovieContentCnt
                str(ResultDict['영화제목']),				        #sawMovieTitle
                str(ResultDict['댓글개수']),				        #replyCnt
                str(ResultDict['댓글내용']),				        #replyContents
                str(ResultDict['게시글좋아요수']),			    #articleLikeCnt
                str(ResultDict['게시글공유수']),			        #articleShareCnt
                str(ResultDict['수집한게시글개수']),			    #articleCnt
                str(ResultDict['평균댓글개수']),			        #avgReplyCnt
                str(ResultDict['평균덧글개수']),			        #avgReplyAndReply
                str(ResultDict['전체긍정어사용빈도']),		        #gdExpssCnt    
                str(ResultDict['평균긍정어사용비율']),		        #avgGdExpssRate
                str(ResultDict['페이스북게시글등록시간']),		    #fbacrticleRegTime                     
                str(ResultDict['개요항목개수']),			        #aboutInfoCnt                
                str(ResultDict['해당월게시글개수']),			    #thisMnthArticleCnt
                str(ResultDict['전월게시글개수']),			    #preMnthArticleCnt
                str(ResultDict['운영년수']),				        #arrangeYears
                str(ResultDict['T_SCORE']),                     #fb_tscore
                str(ResultDict['C_SCORE']),                     #fb_cscore
                str(ResultDict['M_SCORE'])                      #fb_mscore
    '''
    '''
    def insert_record_origin_version(self, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17,
                                     f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33, f34,
                                     f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45, f46, f47, f48, f49, f50, f51,
                                     f52, f53,f54, f55, f56, f57, f58, f59, f60, f61, f62, f63, f64):
        try:
            insert_command = "INSERT INTO facebook_crawled_just (userName, facebookUrl, basicInfo_tot, contctInfo_tot, websiteSnsInfo, introduceText, profileTotCnt, profileTotInfo," \
                             "friendsCnt, imgLikeCnt, vodCnt, picCnt, fllwerCnt, detail_info, likePeopleCnt, birthday, " \
                             "birthday_luna, sex, bloodType, addr, website, snsLink, religion, cellPhone, " \
                             "allFrndCnt, knowEachFrnd, latestAddFrnd, univFrnd, homeFrnd, homeTwnFrnd, highschoolFrnd, likeHobbyAllCnt, " \
                             "movieLikeCnt, tvLikeCnt, musicLikeCnt, bookLikeCnt, sportsTemaLikeCnt, foodPlaceCnt, appAndGamesCnt, visitedPlc, " \
                             "visitedCity, recentVisitPlc, evntCnt, eventContents, sawItCnt, sawMovieContentCnt, sawMovieTitle, replyCnt, " \
                             "replyContents, articleLikeCnt, articleShareCnt, articleCnt, avgReplyCnt, avgReplyAndReply, gdExpssCnt, avgGdExpssRate, " \
                             "fbacrticleRegTime, aboutInfoCnt, thisMnthArticleCnt, preMnthArticleCnt, arrangeYears, fb_tscore, fb_cscore, fb_mscore) VALUES('" \
                             + f1 + "','" + f2 + "','" + f3 + "','" + f4 + "','" + f5 + "','" + f6 + "','"\
                             + f7 + "','" + f8 + "','" + f9 + "','" + f10 + "','" + f11 + "','" + f12 + "','"\
                             + f13 + "','" + f14 + "','" + f15 + "', '" + f16 + "', '" + f17 + "','"\
                             + f18 + "','" + f19 + "','" + f20 + "','" + f21 + "','" + f22 + "','" + f23 + "','" \
                             + f24 + "','" + f25 + "','" + f26 + "','" + f27 + "','" + f28 + "','" + f29 + "','" \
                             + f30 + "','" + f31 + "','" + f32 + "', '" + f33 + "', '" + f34 + "','" + f35 + "','" \
                             + f36 + "','" + f37 + "','" + f38 + "', '" + f39 + "', '" + f40 + "','" + f41 + "','" \
                             + f42 + "','" + f43 + "','" + f44 + "', '" + f45 + "', '" + f46 + "', '" + f47 + "', '" \
                             + f48 + "', '" + f49 + "', '" + f50 + "', '" + f51 + "', '" + f52 + "', '" + f53 \
                             + f54 + "','" + f55 + "','" + f56 + "','" + f57 + "','" + f58 + "','" + f59 + "','" \
                             + f60 + "','" + f61 + "','" + f62 + "','" + f63 + "','" + f64 + "' )"

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print(e)

    '''
    # #INSERT
    # def insert_record_facebookInfo(self, f1, f2, f3, f4, f5, f6, f7):
    #
    #     print('f4 :', f4)
    #     try:
    #         insert_command = "INSERT INTO facebook_crawled_just (" \
    #                          "userName, facebookUrl, basicInfo_tot, detail_info,  fb_tscore, fb_cscore, fb_mscore" \
    #                          ") VALUES('" \
    #                          + f1 + "','" + f2 + "','" + f3 + "','" + f4 + "','" + f5  + "','" + f6 + "','" + f7 +"')"
    #
    #         print(insert_command)
    #         self.cursor.execute(insert_command)
    #         self.connection.commit()
    #         self.connection.close()
    #
    #     except Exception as e:
    #         print(e)


    # UPDATE
    def update_ReviewCnt(self, f1, f2):
        print('update_ReviewCnt')
        try:
            insert_command = "UPDATE facebook_crawled_just SET " \
                        "reviewsCnt='" + f1 + "' WHERE facebookUrl='" + f2 + "'; "

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()

            print('DB insert of reviewsCnt success')
            self.connection.close()

        except Exception as e:
            print(e)

    # UPDATE
    def update_FollowCnt(self, f1, f2):
        print('update_FollowerCnt')
        try:
            insert_command = "UPDATE facebook_crawled_just SET " \
                        "fllwCnt='" + f1 + "' WHERE facebookUrl='" + f2 + "'; "

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()

            print('DB insert of fllwCnt success')
            self.connection.close()

        except Exception as e:
            print(e)



    # UPDATE
    def update_PhotoLikeCmntCnt(self, f1, f2, f3):
        print('update_PhotoLikeCmntCnt')
        try:
            insert_command = "UPDATE facebook_crawled_just SET " \
                        "phdatgulCnt='" + f1 + "', photoLikeCnt='" + f2 + "' WHERE facebookUrl='" + f3 + "'; "

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()

            print('DB insert of update_PhotoLikeCmntCnt success')
            self.connection.close()

        except Exception as e:
            print(e)






