import connect_databases

if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    connect_databases.delete_from_skin_where_skin_url_begin_with_com(db)
    connect_databases.close_database(db)
