import requests
from bs4 import BeautifulSoup


def analysis_at_minecraft_skins_net(response):
    res_lst = list()
    soup = BeautifulSoup(response.content, 'lxml')
    base_url = 'https://www.minecraftskins.net'
    skins = soup.findAll(name='div', attrs="card")
    for skin in skins:
        skin_name = ""
        skin_url = ""
        skin_preview_url = ""
        skin_author = ""
        skin_description = ""
        for i, child in enumerate(skin.descendants):
            if i == 5:
                skin_name = child['alt']
                skin_preview_url = base_url + child['src']
            if i == 3:
                skin_url = base_url + child['href'] + '/download'
            if i == 19:
                skin_author = child.string
            if i == 21:
                skin_description = child.string
        res_lst.append((skin_name, skin_url, skin_preview_url, skin_author, skin_description))
    return res_lst


def analysis_at_minecraft_skins_com(response):
    res_lst = list()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 '
    }
    base_url = 'https://www.minecraftskins.com'
    soup = BeautifulSoup(response.content, 'lxml')
    skins = soup.findAll(name='div', attrs="skin")
    for j, skin in skins:
        skin_name = ""
        skin_page = ""
        skin_preview_url = ""
        skin_author = ""
        skin_praise = ""
        skin_comment = ""
        for i, child in enumerate(skin.descendants):
            if i == 3:
                skin_page = base_url + child['href']
            if i == 12:
                skin_name = child.string
            if i == 22:
                skin_author = child
            if i == 34:
                skin_praise = child.string
            if i == 45:
                skin_comment = child.string
            if i == 5:
                skin_preview_url = base_url + child['src']
        skin_response = requests.get(url=skin_page, headers=headers)
        skin_soup = BeautifulSoup(skin_response.content, 'lxml')
        skin_visit = skin_soup.find(name='div', attrs='sid-views').string
        skin_download = skin_soup.find(attrs={'data-role': "skin-total-amount-of-downloads"}).string.replace('\n', '')
        skin_download_url = base_url + skin_soup.find(name='a', attrs='btn btn-download')['href']
        skin_id = hash(skin_name)
        if skin_id < 0:
            skin_id = -skin_id
        res_lst.append((skin_id, skin_download_url, skin_preview_url, skin_author, skin_name, skin_visit, skin_download,
                        skin_praise, skin_comment))
        print("analysis progress:", j, "/", len(skins))
    return res_lst
