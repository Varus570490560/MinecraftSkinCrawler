import json

import requests
import analy
import connect_databases


def craw_at_mc_net():
    db = connect_databases.open_database_mc_skin()
    page = 1
    while page < 25:
        response = requests.get('https://www.minecraftskins.net/page/' + str(page))
        skin_list = analy.analysis_at_minecraft_skins_net(response)
        connect_databases.insert_into_mc_skin_from_mc_net(db=db, skin_lst=skin_list)
        page += 1
    connect_databases.close_database(db=db)


def craw_at_mc_com():
    db = connect_databases.open_database_mc_skin()
    page = 1
    while page < 50:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get(url='https://www.minecraftskins.com/' + str(page), headers=headers)
        skin_list = analy.analysis_at_minecraft_skins_com(response)
        connect_databases.insert_into_mc_skin_from_mc_com(db=db, skin_lst=skin_list)
        page += 1
    connect_databases.close_database(db=db)


def craw_at_nova():
    db = connect_databases.open_database_mc_skin()
    page = 'CjoKFAoHaG90bmVzcxIJIRgmUwXjt5JAEh5qDHN-c2tpbmVkaXRvcnIOCxIEU2tpbhjC5YuIBgwYACAB'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    while page != "":
        param = {
            'json': 'true',
            'callback': 'searchData',
            'next': page
        }
        print('page code:', page)
        response = requests.get(url='https://minecraft.novaskin.me/gallery/tag/skins', headers=headers, params=param)
        response_str = response.content.decode('utf8')
        page, skins = analy.analysis_at_nova(response_str)
        connect_databases.insert_into_mc_skin_from_nova(db=db, skin_lst=skins)
    print('OK')
    connect_databases.close_database(db)


def craw_at_mc_skin_top():
    db = connect_databases.open_database_mc_skin()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    page = 217
    while page <= 240:
        print('page = ', page, '/240')
        response = requests.get(url='https://mcskins.top/page/' + str(page), headers=headers)
        lst = analy.analysis_mc_skin_top_page(response=response)
        connect_databases.insert_into_mc_skin_from_mcskin_top(db=db, skin_lst=lst)
        page = page + 1
    connect_databases.close_database(db=db)


def craw_at_needcoolshoes():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    base_url = 'https://www.needcoolshoes.com/gallery?page='
    page = 1
    while page < 57998:
        print('page=', page)
        response = requests.get(base_url + str(page), headers=headers)
        analy.analysis_needcoolshoes(response=response)
