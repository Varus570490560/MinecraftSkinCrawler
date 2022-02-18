import openpyxl
import requests
from openpyxl.drawing.image import Image
import connect_databases



def make_excel(excel_name, data_source):
    wb = openpyxl.Workbook()
    ws = wb.active
    row = 1
    for data in data_source:
        ws.cell(row=row, column=1, value=data[0])
        ws.cell(row=row, column=2, value=data[1])
        ws.cell(row=row, column=3, value=data[2])
        file = download(url=data[3], type_='d', id=str(data[0]))
        img = Image(file)
        img.width=128
        img.height=128
        ws.add_image(img, anchor='d' + str(row))
        file = download(url=data[4], type_='p1', id=str(data[0]))
        img = Image(file)
        img.width=128
        img.height=128
        ws.add_image(img, anchor='e' + str(row))
        file = download(url=data[5], type_='p2', id=str(data[0]))
        img = Image(file)
        img.width = 128
        img.height = 128
        ws.add_image(img, anchor='f' + str(row))
        ws.cell(row=row, column=7, value=data[6])
        ws.cell(row=row, column=8, value=data[7])
        ws.cell(row=row, column=9, value=data[8])
        ws.cell(row=row, column=10, value=data[9])
        ws.cell(row=row, column=11, value=data[10])
        ws.cell(row=row, column=12, value=data[11])
        ws.cell(row=row, column=13, value=data[12])
        ws.cell(row=row, column=14, value=data[13])
        print(data)
        row = row + 1
    wb.save(filename=excel_name + '.xlsx')


def download(url, type_, id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    download_response = requests.get(url=url, headers=headers)
    with open(type_+id+'.png', 'wb') as f:
        f.write(download_response.content)
    return type_+id+'.png'


if __name__ == '__main__':
    db = connect_databases.open_database_mc_skin()
    data = connect_databases.select_from_skin_where_data_source_is_name_mc_order_by_download_desc_limit_500(db)
    make_excel('name_mc', data)
    connect_databases.close_database(db)
