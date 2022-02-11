# coding=utf-8
import pymysql


def open_database_mc_skin():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='mc_skin', autocommit=True)
        print('database "mc_skin" open successfully!!!')
    except pymysql.Error as e:
        print('database "mc_skin" open failed!!!')
        print(e)
        return None
    return db


def close_database(db):
    db.close()


def insert_into_mc_skin_from_mc_net(db, skin_lst):
    with db.cursor() as cursor:
        try:
            for skin in skin_lst:
                skin_id = hash(skin[4])
                if skin_id < 0:
                    skin_id = -skin_id
                author = skin[3].replace("Designed by ", "")
                cursor.execute(
                    'INSERT INTO `skin` (`id`,`skin_url`,`skin_preview`,`author`,`name`,`description`) VALUES (%s,%s,%s,%s,%s,%s)',
                    (skin_id, skin[1], skin[2], author, skin[0], skin[4]))
                print((skin_id, skin[1], skin[2], author, skin[0], skin[4]))
                print('database saved!')
        except pymysql.Error as err:
            print(err)


def insert_into_mc_skin_from_mc_com(db, skin_lst):
    with db.cursor() as cursor:
        try:
            for skin in skin_lst:
                cursor.execute(
                    'INSERT INTO `skin` (`id`,`skin_url`,`skin_preview`,`author`,`name`,`visit`,`download`,`praise`,`comment`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    skin)
                print(skin)
                print('database saved!')
        except pymysql.Error as err:
            print(err)