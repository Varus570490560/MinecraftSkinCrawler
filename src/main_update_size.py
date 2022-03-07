import PIL
from PIL import Image
import os
import connect_databases


def get_id(file_name):
    res = ""
    for c in file_name:
        if '0' <= c <= '9':
            res += c
    return res


if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    for root, dirs, files in os.walk('../../pythonProject5/downloadPNG/'):
        for file in files:
            try:
                skin_id = get_id(file)
                img = Image.open('../../pythonProject5/downloadPNG/' + file)
                size = str(img.size)
                connect_databases.update_skin_set_size_by_id(db=db, skin_id=skin_id, size=size)
                img.close()
            except PIL.UnidentifiedImageError:
                pass
    connect_databases.close_database(db)
