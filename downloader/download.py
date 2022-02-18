import requests
from bs4 import BeautifulSoup as soup

ELSEVIER_API_KEY = '9a5e20f17a90961fdea380dd185f1465'
WILEY_API_KEY = '103fc970-c3d8-464e-862f-950e306f3260'

def download_from_elsevier(doi, api_key, response_type, output_filename):
    url='http://api.elsevier.com/content/article/doi:' + doi + '?view=FULL'
    headers = {
        'X-ELS-APIKEY': '{}'.format(api_key),
        'Accept': 'text/{}'.format(response_type)
    }
    r = requests.get(url, stream=True, headers=headers)
    with open("/Users/vnarapar/Google Drive/My Drive/digital-forest/elsevier/" + output_filename+'.{}'.format(response_type), 'wb') as f:
        for chunk in r.iter_content(2048):
            f.write(chunk)
            
def download_from_ijrs(doi, output_filename):
    url = 'https://www.tandfonline.com/doi/full/' + doi
    ijrs_raw = requests.get(url).text
    ijrs_soup = soup(ijrs_raw)
    ijrs_soup = ijrs_soup.find('article')
    print(ijrs_soup)
    with open(output_filename, "w", encoding='utf-8') as file:
        file.write(str(ijrs_soup))

download_from_elsevier('10.1016/j.ejsobi.2021.103315', ELSEVIER_API_KEY, 'xml', '10.1016_j.ejsobi.2021.103315')
# download_from_ijrs('10.1080/01431161.2020.1811917', 'ijrs.html')