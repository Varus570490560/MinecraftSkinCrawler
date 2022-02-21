import connect_databases

if __name__ == '__main__':
    mark = connect_databases.open_database_mark()
    connect_databases.init_mark_to_download(mark)
    connect_databases.close_database(mark)
