# !/usr/bin/python
import pymysql

class DatabaseConnection_zeniel:

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


    # INSERT facebook
    def insert_record_origin_version(self, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17,
                                     f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, f32, f33,
                                     f34, f35, f36, f37, f38, f39, f40, f41, f42, f43, f44, f45,
                                     f46, f47, f48, f49, f50, f51, f52, f53, f54, f55, f56, f57, f58, f59, f60):
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
                             "cellPhone,addr,snsLink,website,birthday,birthday_luna,photobookCnt) VALUES('" \
                             + f1 + "','" + f2 + "','" + f3 + "','" + f4 + "','" + f5 + "','" + f6 + "','" \
                             + f7 + "','" + f8 + "','" + f9 + "','" + f10 + "','" + f11 + "','" + f12 + "','" \
                             + f13 + "','" + f14 + "','" + f15 + "', '" + f16 + "', '" + f17 + "','" \
                             + f18 + "','" + f19 + "','" + f20 + "','" + f21 + "','" + f22 + "','" + f23 + "','" \
                             + f24 + "','" + f25 + "','" + f26 + "','" + f27 + "','" + f28 + "','" + f29 + "','" \
                             + f30 + "','" + f31 + "','" + f32 + "', '" + f33 + "', '" + f34 + "','" + f35 + "','" \
                             + f36 + "','" + f37 + "','" + f38 + "', '" + f39 + "', '" + f40 + "','" + f41 + "','" \
                             + f42 + "','" + f43 + "','" + f44 + "', '" + f45 + "', '" + f46 + "', '" + f47 + "', '" \
                             + f48 + "', '" + f49 + "', '" + f50 + "', '" + f51 + "', '" + f52 + "', '" + f53 + "', '" \
                             + f54 + "','" + f55 + "','" + f56 + "','" + f57 + "','" + f58 + "','" + f59 + "', '" + f60 + "' )"

            print(insert_command)
            self.cursor.execute(insert_command)
            self.connection.commit()
            self.connection.close()

        except Exception as e:
            print(e)

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
