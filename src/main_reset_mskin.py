import connect_databases

if __name__ == '__main__':
    db = connect_databases.open_database_mark()
    connect_databases.reset_table_mcskin_mark(db)
    connect_databases.close_database(db)
