import requests
from bs4 import BeautifulSoup as soup
import urllib

# Replace these values with your own API Keys
ELSEVIER_API_KEY = '9a5e20f17a90961fdea380dd185f1465'
WILEY_API_KEY = '103fc970-c3d8-464e-862f-950e306f3260'

def download_from_elsevier(root_path, output_filename, response_type, api_key, doi):
    """Download articles from elsevier journals

    Special Instructions: Most articles require the the download 
    request sent from an IP address inside Purdue Network. Please login to
    Purdue WiFi to run this function and get appropraite results.

    Args:
        doi (string): DOI string of requested article
        api_key (string): ELSEVIER API key to use for authentication
        response_type (string): text or html
        output_filename (): _description_
    """
    # Article url link
    url = 'http://api.elsevier.com/content/article/doi:' + doi + '?view=FULL'
    
    # HTTP headers for authentication
    # https://dev.elsevier.com/tecdoc_api_authentication.html - Read this
    headers = {
        'X-ELS-APIKEY': '{}'.format(api_key),
        'Accept': 'text/{}'.format(response_type)
    }
    
    # Make HTTP Get request
    response = requests.get(url, stream=True, headers=headers)
    
    # Save file 
    with open(root_path + output_filename + '.{}'.format(response_type), 'wb') as f:
        for chunk in response.iter_content(2048):
            f.write(chunk)
            
def download_from_mdpi(root_path, output_file, doi):
    """Download open access articles from MDPI journal

    Args:
        output_file (string): _description_
        doi (_type_): _description_
    """
    # MDPI Search URL link
    url = 'https://www.mdpi.com/search?q=' + urllib.parse.quote_plus(doi)
    
    # Make HTTP Get request
    response = requests.get(url)
    
    # Parse response for the actual article
    article_url = response.url
    full_text_url = article_url + '/htm'
    
    # Make HTTP Get request for the full text of the article
    resp_full_text = requests.get(full_text_url)
    
    # Save file
    with open('{}/{}.html'.format(root_path, output_file), "w", encoding='utf-8') as file:
        file.write(str(resp_full_text.text))

# Specifically only for IJRS Journal
def download_from_ijrs(doi, output_filename):
    url = 'https://www.tandfonline.com/doi/full/' + doi
    ijrs_raw = requests.get(url).text
    ijrs_soup = soup(ijrs_raw)
    ijrs_soup = ijrs_soup.find('article')
    print(ijrs_soup)
    with open(output_filename, "w", encoding='utf-8') as file:
        file.write(str(ijrs_soup))

# Example usage of the elsevier downloader
download_from_elsevier('', '10.1016_j.ejsobi.2021.103315', 'xml', ELSEVIER_API_KEY, '10.1016/j.ejsobi.2021.103315')