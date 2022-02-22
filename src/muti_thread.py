import threading
from time import sleep

import get_soup
import requests

import connect_databases
import analy


def slip(page, group_count):
    i = 0
    res_lst = list()
    while i < group_count:
        res_lst.append(list())
        i = i + 1
    i = 0
    while i < len(page):
        res_lst[i % group_count].append(page[i][0])
        i = i + 1
    return res_lst


def slip_all(page, group_count):
    i = 0
    res_lst = list()
    while i < group_count:
        res_lst.append(list())
        i = i + 1
    i = 0
    while i < len(page):
        res_lst[i % group_count].append(page[i])
        i = i + 1
    return res_lst


def craw_at_mskin_unit(pages):
    db = connect_databases.open_database_mc_skin()
    mark_db = connect_databases.open_database_mark()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    for page in pages:
        response = requests.get(url='https://mskins.net/en/skins/latest?page=' + str(page), headers=headers)
        skin_list = analy.analysis_at_mskin(response)
        connect_databases.insert_into_mc_skin_from_mskin(db=db, skin_lst=skin_list)
        connect_databases.update_set_mark(mark_db, page)
    connect_databases.close_database(db=db)
    connect_databases.close_database(db=mark_db)


class CrawlingMskinThread(threading.Thread):
    def __init__(self, thread_id, pages):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.pages = pages

    def run(self):
        print("开始线程：" + str(self.thread_id))
        craw_at_mskin_unit(pages=self.pages)
        print("退出线程：" + str(self.thread_id))


def craw_at_mskin(thread_count):
    db = connect_databases.open_database_mark()
    pages = connect_databases.select_mskin_mark(db=db)
    slip_page = slip(pages, thread_count)
    i = 0
    for page in slip_page:
        i = i + 1
        CrawlingMskinThread(i, page).start()
    connect_databases.close_database(db)


def craw_at_name_mc_unit(pages):
    db = connect_databases.open_database_mc_skin()
    mark_db = connect_databases.open_database_mark()
    for page in pages:
        soup = get_soup.get_soup('https://namemc.com/minecraft-skins?page=' + str(page), True)
        skin_list = analy.analysis_name_mc_soup(soup)
        connect_databases.insert_into_mc_skin_from_name_mc(db=db, skin_lst=skin_list)
        connect_databases.update_set_mark(mark_db, page)
    connect_databases.close_database(db=db)
    connect_databases.close_database(db=mark_db)


class CrawlingNameMC(threading.Thread):
    def __init__(self, thread_id, pages):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.pages = pages

    def run(self):
        print("开始线程：" + str(self.thread_id))
        craw_at_name_mc_unit(pages=self.pages)
        print("退出线程：" + str(self.thread_id))


class CrawlingNeedcoolshoes(threading.Thread):
    def __init__(self, thread_id, pages):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.pages = pages

    def run(self):
        print("开始线程：" + str(self.thread_id))
        craw_at_needcoolshoes_unit(pages=self.pages)
        print("退出线程：" + str(self.thread_id))


def craw_at_name_mc(thread_count):
    page = list()
    page.append(101)
    i = 0
    CrawlingNameMC(i, page).start()


class DownloadThread(threading.Thread):
    def __init__(self, thread_id, pages):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.pages = pages

    def run(self):
        print("开始线程：" + str(self.thread_id))
        download_unit(pages=self.pages)
        print("退出线程：" + str(self.thread_id))


def download_unit(pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    skins = pages
    for skin in skins:
        download_response = requests.get(url=skin[3], headers=headers)
        with open('../../downloadPNG/' + str(skin[0]) + 'download' + '.png', 'wb') as f:
            f.write(download_response.content)
        print('id= ' + str(skin[0]), 'download file', ' Saved !!!')
        preview1_response = requests.get(url=skin[4], headers=headers)
        with open('../../preview1PNG/' + str(skin[0]) + 'preview1' + '.png', 'wb') as f:
            f.write(preview1_response.content)
        print('id= ' + str(skin[0]), 'preview1 file', ' Saved !!!')
        if skin[5] is not None:
            preview2_response = requests.get(url=skin[5], headers=headers)
            with open('../../preview2PNG/' + str(skin[0]) + 'preview2' + '.png', 'wb') as f:
                f.write(preview2_response.content)
            print('id= ' + str(skin[0]), 'preview2 file', ' Saved !!!')
        db = connect_databases.open_database_mc_skin_without_print()
        connect_databases.update_skin_set_is_download_is_1(db=db, skin_id=skin[0])
        connect_databases.close_database(db)


def download(thread_count):
    db = connect_databases.open_database_mc_skin()
    skins = connect_databases.select_from_skin_where_is_download_is_0(db=db)
    pages = slip_all(skins, thread_count)
    i = 0
    for page in pages:
        i = i + 1
        DownloadThread(i, page).start()
    connect_databases.close_database(db)


def craw_at_needcoolshoes_unit(pages):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    base_url ='https://www.needcoolshoes.com/gallery?page='
    for page in pages:
        print('page=', page[0])
        response=requests.get(base_url+str(page[0]))




