import connect_databases

if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    res = connect_databases.select_id_preview_url_1_need_be_modify(db)
    for re in res:
        url = re[1].replace('uploads%', 'uploads')
        connect_databases.update_set_preview_url_1_by_id(db=db, id=re[0], url=url)
        print(re, 'OK')
    connect_databases.close_database(db=db)
