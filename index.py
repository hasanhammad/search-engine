# Importing the necessary libraries

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from posting_list import *

nltk.download('punkt')
nltk.download('stopwords')
Stopwords = set(stopwords.words('english'))

linked_list_data = {}
dictionary = set()
pages_with_index = {}
titles = []
to_crawl = []
crawled = []
idx = 1


# remove html tags using regular expresion
def remove_html_tags(page):
    page = re.sub('(\&lt\;).*?(\&gt\;)', ' ', page)
    page = re.sub(r"&nbsp;", ' ', page)
    pattern = re.compile(r'<\/?\w+\s*[^>]*?\/?>', re.DOTALL | re.MULTILINE | re.IGNORECASE | re.UNICODE)
    page = re.sub(pattern, ' ', page)
    pattern = re.compile(r'<([A-Z][A-Z0-9]*)(\b[^>src]*)(src\=[\'|"|\s]?[^\'][^"][^\s]*[\'|"|\s]?)?(\b[^>]*)>')
    page = re.sub(pattern, ' ', page)
    page = re.sub(r'<.*?>', ' ', page)
    return page


# clean web page from all kinds of tags
def clean_web_page(page):
    # remove <SCRIPT> to </script> and variations
    pattern = r'<[ ]*script.*?\/[ ]*script[ ]*>'  # mach any char zero or more times
    page = re.sub(pattern, '', page, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # remove HTML <STYLE> to </style> and variations
    pattern = r'<[ ]*style.*?\/[ ]*style[ ]*>'  # mach any char zero or more times
    page = re.sub(pattern, '', page, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # remove HTML <META> to </meta> and variations
    pattern = r'<[ ]*meta.*?>'  # mach any char zero or more times
    page = re.sub(pattern, '', page, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # remove HTML COMMENTS <!-- to --> and variations
    pattern = r'<[ ]*!--.*?--[ ]*>'  # mach any char zero or more times
    page = re.sub(pattern, '', page, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))

    # remove HTML DOCTYPE <!DOCTYPE html to > and variations
    pattern = r'<[ ]*\![ ]*DOCTYPE.*?>'  # mach any char zero or more times
    page = re.sub(pattern, '', page, flags=(re.IGNORECASE | re.MULTILINE | re.DOTALL))
    # remove HTML tags
    page = remove_html_tags(page)

    return page


# to remove special characters
def remove_special_characters(text):

    # compile a regular expression pattern into a regular expression object
    # regex will match any charecter except
    regex = re.compile('[^a-zA-Z0-9\s]')
    # \s --  it matches any whitespace character, this is equivalent to the set [ \t\n\r\f\v].
    # if the regular expression (regex) found in text then replace it with ('') nohing
    text_returned = re.sub(regex, '', text)
    # matches any decimal digit; this is equivalent to the set [0-9].
    # remove all decimal digit
    text_returned = re.sub(re.compile('\d'), '', text_returned)
    # break the page content into words
    words = word_tokenize(text_returned.lower())

    # define a set
    clean_words = set()
    for word in words:
        if word not in Stopwords and len(word) > 2 and word not in clean_words:
            # store unique words in clean_word set
            clean_words.add(word)
    # return unique words
    return clean_words


# index the content of the page
def indexing(link, clean_words):
    global linked_list_data
    global dictionary
    global pages_with_index
    global idx

    for word in clean_words:
        if word not in dictionary:
            # add new word to dictionary
            dictionary.add(word)
            # make a posting list for the word
            linked_list_data[word] = SlinkedList()
            linked_list_data[word].head = Node(idx)
        linked_list = linked_list_data[word].head
        # fill the posting list
        while linked_list.nextval is not None:
            linked_list = linked_list.nextval
        linked_list.nextval = Node(idx)
    # store the processed page name with its number
    pages_with_index[idx] = link
    # idx: is used for page numbering
    idx = idx + 1


#idx => link => word1 => word2 ....