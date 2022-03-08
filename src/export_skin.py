import random

import connect_databases


def set_in_use():
    skin = connect_databases.open_database_mc_skin()
    online = connect_databases.open_database_online_skin()
    download_image_urls = connect_databases.select_download_image_url_from_mc_skin(online)
    sha256s = connect_databases.select_sha256_from_skin_by_download_image_url(skin,
                                                                              download_image_urls=download_image_urls)
    connect_databases.update_set_in_use_by_sha256(db=skin, sha256s=sha256s)
    connect_databases.close_database(skin)
    connect_databases.close_database(online)


def export(skin_count: int, db):
    skin_lst = list(connect_databases.select_from_skin_where_in_use_is_0_single(db))
    random.shuffle(skin_lst)
    res = skin_lst[0:skin_count]
    sha256_lst = list()
    for data in res:
        sha256_lst.append(data[18])
    print(sha256_lst)
    with open("../sql/export.sql", 'wb') as writer:
        for skin in res:
            writer.write(
                "insert into `mc_skin_reserve` (name, author, skin_image_url, description, preview_image_url)values  ('{}', '{}', '{}', '{}','');\n".format(
                    change(skin[1]), change(skin[2]), change(skin[3]), change(skin[6])).replace('None', '').encode())
    connect_databases.update_set_in_use_by_sha256(db, sha256_lst)


def change(value):
    return value.replace("'", "\\'")


if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    export(skin_count=1000, db=db)
    connect_databases.close_database(db=db)
