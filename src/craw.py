import requests
import analy
import connect_databases
import asyncio


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
    page = 36
    while page < 50:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
        }
        response = requests.get(url='https://www.minecraftskins.com/' + str(page), headers=headers)
        skin_list = analy.analysis_at_minecraft_skins_com(response)
        connect_databases.insert_into_mc_skin_from_mc_com(db=db, skin_lst=skin_list)
        page += 1
    connect_databases.close_database(db=db)




