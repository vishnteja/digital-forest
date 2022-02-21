# digital-forest
Repository for digital forest project

List down all the components

1. Downloader Component - responsible for downloading the full text articles from a csv. 

Goal
----
Input - CSV with article names, DOIs, publisher names and so on.
Output - List of Full Text articles. (These articles can be either xml, html or pdf).

Strategy for downloading articles
a. If we can download the xml/html through APIs or scraping the web, we would choose this option.
b. If xml/html is not possible, then we would try to download the PDF files. 


2. Data Processing Component - responsible for extracting the textual information from the downloaded articles. 

PDFtoXML conversion module
> Note: PDF files are converted to xml. 

Goal
----
Input - Article (xml, html)
Output - Text(string)

The conversion is different for every article publisher. 
a. Different file format 
b. Different article foramtting 
c. Different non text patterns

Elsevier - xml files, API is provided by publisher
MDPI - html files, this data has been web scraped
Wiley - 
Taylor & Francis - No access with purdue credentials, some articles are open access
Springer - 
IEEE - 

To do for each publisher.
1. Get the article files
2. Analyse the files and try to figure out in which sections include the text that we need. 
3. Implement a program that takes the article input and then remove unnecessary information and output the full text string. 

> Notes on processing
1. Using xml, we can identify the sections that have useful information. 
2. Using regular expressions - We can define patterns that match the not useful text. 
google search example - regular expression to remove all html tags in python.
3. Use beautiful soup / other advanced packages that could do it automatically. 

def process_elsevier(article_xml):
    useful_sections = ["introduction" .. ]
    result_text = ""
    for section in article_xml:
        result_text += extract_text_from_section(section)
    return result.

3. Data preprocessing for ML. 

Input - raw full text from each article
Output - simplified text 

Strategy
1. Convert all words to lowercase characters
2. Remove all numbers
Optional 
3. Stemming (happy happiest -> happ)
4. Lemmatization (play playing -> play)


4. Generate custom word embeddings for all the words in the corpus

Input - corpus (list of all articles )
Output - Word vector for each word in the corpus.

Steps
1. Generate dictionary from the corpus
2. Use glove pretrained embeddings
3. A ML model that is finetuned for new words.


5. Analyze the word embedding 
Study the embeddings and decide if the model learned useful information. 


