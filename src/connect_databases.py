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
        for skin in skin_lst:
            author = skin[3].replace("Designed by ", "")
            try:
                cursor.execute(
                    'INSERT INTO `skin` (`download_url`,`preview_url_1`,`author`,`name`,`description`) VALUES (%s,%s,%s,%s,%s)',
                    (skin[1], skin[2], author, skin[0], skin[4]))
                print((skin[1], skin[2], author, skin[0], skin[4]))
                print('database saved!')
            except pymysql.Error as err:
                print(err)


def insert_into_mc_skin_from_mc_com(db, skin_lst):
    with db.cursor() as cursor:
        for skin in skin_lst:
            try:
                cursor.execute(
                    'INSERT INTO `skin` (`download_url`,`preview_url_1`,`author`,`name`,`visit`,`download`,`praise`,`comment`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',
                    skin)
                print(skin)
                print('database saved!')
            except pymysql.Error as err:
                print(err)


def delete_from_skin_where_skin_url_begin_with_com(db):
    with db.cursor() as cursor:
        try:
            cursor.execute("DELETE FROM `skin` WHERE `skin_url` LIKE 'https://www.minecraftskins.com/%'")
        except pymysql.Error as err:
            print(err)


def insert_into_mc_skin_from_mskin(db, skin_lst):
    with db.cursor() as cursor:
        for skin in skin_lst:
            try:
                cursor.execute(
                    'INSERT INTO `skin` (`download_url`,`preview_url_1`,`name`,`like`,`visit`,`download`) VALUES (%s,%s,%s,%s,%s,%s)',
                    skin)
                print(skin)
                print('database saved!')
            except pymysql.Error as err:
                print(err)


def open_database_mark():
    try:
        db = pymysql.connect(host='localhost', user='root', password='', port=3306, database='mark', autocommit=True)
        print('database "mark" open successfully!!!')
    except pymysql.Error as e:
        print('database "mark" open failed!!!')
        print(e)
        return None
    return db


def reset_table_mcskin_mark(db):
    with db.cursor() as cursor:
        try:
            cursor.execute('DELETE FROM `mskin_mark`')
            i = 1
            while i < 2223:
                cursor.execute('INSERT INTO `mskin_mark` (`page`,`mark`) VALUES (%s,0)', (i,))
                i = i + 1
        except pymysql.Error as err:
            print(err)


def select_mskin_mark(db):
    with db.cursor() as cursor:
        try:
            cursor.execute('SELECT `page` FROM `mskin_mark` WHERE `mark` = 0')
            res = cursor.fetchall()
        except pymysql.Error as err:
            print(err)
            return None
    return res


def update_set_mark(db, page):
    with db.cursor() as cursor:
        try:
            cursor.execute('UPDATE `mskin_mark` SET `mark` = 1 WHERE `page` = %s', (page,))
        except pymysql.Error as err:
            print(err)


def insert_into_mc_skin_from_name_mc(db, skin_lst):
    with db.cursor() as cursor:
        for skin in skin_lst:
            try:
                cursor.execute(
                    'INSERT INTO `skin` (`download_url`,`preview_url_1`,`preview_url_2`,`like`) VALUES (%s,%s,%s,%s)',
                    skin)
                print(skin)
                print('database saved!')
            except pymysql.Error as err:
                print(err)


def insert_into_mc_skin_from_nova(db, skin_lst):
    with db.cursor() as cursor:
        for skin in skin_lst:
            try:
                print(skin)
                cursor.execute(
                    'INSERT INTO `skin` (`name`,`author`,`download_url`,`preview_url_1`,`like`,`praise`) VALUES (%s,%s,%s,%s,%s,%s)',
                    skin)
                print(skin)
                print('database saved!')
            except pymysql.Error as err:
                print(err)
