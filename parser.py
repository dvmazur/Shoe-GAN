import requests
from urllib import request
from bs4 import BeautifulSoup


def parse_links(base_link, max_prods):
    pic_links = list()
    LIMIT_PARAM = "?limit="

    page_html = request.urlopen(base_link + LIMIT_PARAM + str(max_prods))
    soup = BeautifulSoup(page_html, 'lxml')

    for pic in soup.find_all('a', {'class': 'product-image'}):
        pic_links.append(pic.find('img').get('src'))

    return pic_links


def link_to_pick(links, save_dir):
    for i in range(len(links)):
        with open(save_dir + str(i) + '.jpg', 'wb') as handle:
            response = requests.get(links[i], stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)
