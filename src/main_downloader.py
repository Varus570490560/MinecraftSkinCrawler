import requests

import connect_databases

if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    skins = connect_databases.select_from_skin_where_data_source_is_mskin_order_by_download_desc_limit_500(db)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    for skin in skins:
        download_response = requests.get(url=skin[3], headers=headers)
        with open('../png_container/' + str(skin[0]) + 'download' + '.png', 'wb') as f:
            f.write(download_response.content)
        print('id= ' + str(skin[0]), 'download file', ' Saved !!!')
        preview1_response = requests.get(url=skin[4], headers=headers)
        with open('../png_container/' + str(skin[0]) + 'preview1' + '.png', 'wb') as f:
            f.write(preview1_response.content)
        print('id= ' + str(skin[0]), 'preview1 file', ' Saved !!!')
        if skin[5] is not None:
            preview2_response = requests.get(url=skin[5], headers=headers)
            with open('../png_container/' + str(skin[0]) + 'preview2' + '.png', 'wb') as f:
                f.write(preview2_response.content)
            print('id= ' + str(skin[0]), 'preview2 file', ' Saved !!!')
