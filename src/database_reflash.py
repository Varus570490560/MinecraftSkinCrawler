import connect_databases


def get_download_url(skin_id):
    base_url = 'https://cdn.ezjojoy.com/mcskins'
    append_1 = str(skin_id % 100)
    append_2 = str(int(skin_id / 100) % 100)
    if len(append_1) == 1:
        append_1 = "0" + append_1
    if len(append_2) == 1:
        append_2 = "0" + append_2
    return base_url + '/' + str(append_1) + '/' + str(append_2) + '/' + str(skin_id) + '.png'


def get_preview1_url(skin_id):
    base_url = 'https://cdn.ezjojoy.com/mcskins'
    append_1 = str(skin_id % 100)
    append_2 = str(int(skin_id / 100) % 100)
    if len(append_1) == 1:
        append_1 = "0" + append_1
    if len(append_2) == 1:
        append_2 = "0" + append_2
    return base_url + '/' + str(append_1) + '/' + str(append_2) + '/' + str(skin_id) + '_preview1.webp'


def get_preview2_url(skin_id):
    base_url = 'https://cdn.ezjojoy.com/mcskins'
    append_1 = str(skin_id % 100)
    append_2 = str(int(skin_id / 100) % 100)
    if len(append_1) == 1:
        append_1 = "0" + append_1
    if len(append_2) == 1:
        append_2 = "0" + append_2
    return base_url + '/' + str(append_1) + '/' + str(append_2) + '/' + str(skin_id) + '_preview2.webp'


if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    skins = connect_databases.select_from_skin(db=db)
    for skin in skins:
        skin_id = skin[0]
        connect_databases.update_skin_set_download_url_by_id(db=db, skin_id=skin_id, url=get_download_url(skin_id))
        connect_databases.update_skin_set_preview_url_1_by_id(db=db, skin_id=skin_id, url=get_preview1_url(skin_id))
        if skin[13] == 'NameMC':
            connect_databases.update_skin_set_preview_url_2_by_id(db=db, skin_id=skin_id,
                                                                  url=get_preview2_url(skin_id=skin_id))
        print(skin_id)
    connect_databases.close_database(db=db)

