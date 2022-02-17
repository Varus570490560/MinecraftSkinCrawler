import json

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
    j = 0
    for skin in skins:
        j = j + 1
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
        res_lst.append((skin_download_url, skin_preview_url, skin_author, skin_name, skin_visit, skin_download,
                        skin_praise, skin_comment))
        print((skin_download_url, skin_preview_url, skin_author, skin_name, skin_visit, skin_download,
               skin_praise, skin_comment))
        print("analysis progress:", j, "/", len(skins))
    return res_lst


def analysis_at_mskin(response):
    res = list()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    soup = BeautifulSoup(response.content, 'lxml')
    skins = soup.findAll(name='div', attrs='col l4 m6 s12')
    base_url = 'https://mskins.net/'
    for skin in skins:
        skin_name = ""
        skin_download_url = ""
        skin_download = ""
        skin_visit = ""
        skin_like = ""
        skin_preview_url = ""
        for i, child in enumerate(skin.descendants):
            if i == 7:
                skin_preview_url = base_url + child['src']
            if i == 14:
                skin_name = child.string
            if i == 5:
                skin_page = child['href']
                page_response = requests.get(url=skin_page, headers=headers)
                page_soup = BeautifulSoup(page_response.content, 'lxml')
                page_infos = page_soup.find(name='ul', attrs='collection skin-info')
                for page_i, page_child in enumerate(page_infos):
                    if page_i == 1:
                        skin_visit = page_child.contents[2].string
                    if page_i == 3:
                        skin_download = page_child.contents[2].string
                    if page_i == 5:
                        skin_like = page_child.contents[2].string
                download = page_soup.find(name='a', attrs='dw starting_download btn waves-effect waves-light cyan')
                skin_download_url = download['href']
        res.append((skin_download_url, skin_preview_url, skin_name, skin_like, skin_visit, skin_download))
        print((skin_download_url, skin_preview_url, skin_name, skin_like, skin_visit, skin_download))
    return res


def find_id(url):
    print(url)
    url = url.replace('/skin/', '')
    end_index = url.find('&')
    return url[0: end_index + 1]


def analysis_name_mc_soup(soup):
    skin_lst = list()
    skins = soup.findAll(name='div', attrs='card mb-2')
    for skin in skins:
        skin_id = ""
        skin_download_url = ""
        skin_preview_url = ""
        skin_preview_url_2 = ""
        skin_like = ""
        for i, child in enumerate(skin.descendants):
            if i == 0:
                skin_id = child['href']
                skin_id = skin_id.replace('/skin/', '')
                print(skin_id)
            if i == 10:
                skin_like = child.string[1:len(child.string)]
        skin_preview_url = 'https://r.nmc1.net/skin/body.png?id=' + skin_id + '&model=slim&theta=-23&phi=8&time=289.25&width=600&height=800'
        skin_preview_url_2 = 'https://r.nmc1.net/skin/body.png?id=' + skin_id + '&model=slim&theta=151&phi=9&time=1366.06&width=600&height=800'
        skin_download_url = 'https://i.nmc1.net/' + skin_id + '.png'
        skin_lst.append((skin_download_url, skin_preview_url, skin_preview_url_2, skin_like))
    return skin_lst


def analysis_at_nova(response_str):
    base_url = "https://minecraft.novaskin.me/skin/"
    lst = list()
    response_str = response_str.replace("searchData(", "")
    response_str = response_str[:-1]
    response_json = json.loads(response_str)
    page = ""
    try:
        page = response_json["pagination"]["next"]
        for skin in response_json['skins']:
            author = skin['author']
            name = skin['title']
            download_url = base_url + str(skin['id']) + '/download'
            preview_url_1 = skin['screenshot']
            like = str(skin['favorited'])
            praise = str(skin['votes'])
            lst.append((name, author, download_url, preview_url_1, like, praise))
            print((name, author, download_url, preview_url_1, like, praise))
    except KeyError as e:
        print(e)
    return page, lst


def analysis_mc_skin_top_page(response):
    lst = list()
    base_url = 'https://mcskins.top'
    name = ""
    author = ""
    preview_url_1 = ""
    download_url = ""
    like = ""
    comment = ""
    soup = BeautifulSoup(response.content, 'lxml')
    skins = soup.findAll(name='div', attrs='skin')
    for skin in skins:
        for i, child in enumerate(skin.descendants):
            if i == 2:
                skin_url = base_url + child['href']
                file_url = child['href'].replace('/skin/', '/')
                download_url = base_url + file_url
                analysis_mc_skin_top_skin(skin_url)
            if i == 3:
                name = child.string
            if i == 1:
                preview_url_1 = base_url + '/assets/images/skin' + child['src'] + '.png'
        lst.append((name, author, download_url, preview_url_1, like, comment))
        print((name, author, download_url, preview_url_1, like, comment))
    return lst


def analysis_mc_skin_top_skin(skin_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    response = requests.get(url=skin_url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    like = soup.find(name='div', id='like')
    comment = soup.find(name='commentsCount')
    if like is None:
        like = '0'
    else:
        like=like.string
    if comment is None:
        comment = '0'
    else:
        comment=comment.string
    return like, comment
