import requests
import bs4

sites = {
    'http://github.com/': 307,
    'https://github.com/': 200,
    'https://www.github.com/': 301,
    'https://www.github.com/test/': 301,
    'https://github.com/testlololo': 404,
    'https://github.com/test?lol': 200
}


def get_site_info(text):
    html = bs4.BeautifulSoup(text)
    title = html.title.text
    metas = html.find_all('meta')
    metas = [meta.attrs['content'] for meta in metas if ('name' in meta.attrs and meta.attrs['name'] == 'description')]
    h1_tags = html.find_all('h1')
    h1_tags = [tag.text for tag in h1_tags]
    return title, metas, h1_tags


for site in sites:
    r = requests.get(site, allow_redirects=False)
    if r.status_code == requests.status_codes.codes.OK:
        print('статус: {}. Совпадает'.format(r.status_code))
        title, meta, h1 = get_site_info(r.text)
        print('Title: {}. Meta: {}. H1: {}'.format(title, meta, h1))
    else:
        print('статус: {}. Не совпадает'.format(r.status_code))