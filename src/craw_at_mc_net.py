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
