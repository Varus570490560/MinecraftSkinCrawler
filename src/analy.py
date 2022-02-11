from bs4 import BeautifulSoup


def analysis_at_minecraft_skins_net(response):
    res_lst = list()
    # response = requests.get('https://www.minecraftskins.net/page/3')
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
