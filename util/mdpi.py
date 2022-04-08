from bs4 import BeautifulSoup
import re


def extract_text_from_html(mdpi_file_name):
    """Extract text content from html file

    Args:
        mdpi_file_name (string): path to the mdpi file 

    Returns:
        string: processed text content
    """
    with open(mdpi_file_name, "r", encoding='utf-8') as f:
        html_file = f.read()
    soup = BeautifulSoup(html_file, 'html.parser')
    
    article = soup.find('article')
    text_list = article.find_all(text=True)
    article_text = " ".join(text_list)
    
    # Remove \n characters
    clean_text = article_text.replace('\n', ' ')
    # Remove special characters and numbers
    clean_text = re.sub('[^A-Za-z\-]', ' ', clean_text)
    # Convert all text to lower
    clean_text = clean_text.lower()
    
    return clean_text
    