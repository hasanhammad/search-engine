# for crawler just import requests library
import requests
# import all the functions in index file
from index import *

# to get html page
def get_htlm(link):
    # set headers
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,de;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "dnt": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/74.0.3729.169 Chrome/74.0.3729.169 Safari/537.36",
    }
    try:
        # get the page
        page = requests.get(link, headers=headers)
        return page.text

    except requests.exceptions.RequestException as ex:
        print("connection error", ex)
        return " "


# returns the union of two lists
def union(lst1, lst2):
    final_list = list(set(lst1) | set(lst2))
    return final_list


# to add new links to to_crawl list
def append_list(to_crawl, links):
    for link in links:
        to_crawl.append(link)


# returns a link from the passed page
def get_next_link(page):
    # get the position of the 'a href' tag in the page
    start_link = page.find('a href="http')
    # if no link found return none and 0
    if start_link == -1:
        return None, 0
    # get the position of the start double quotes
    start_qoute = page.find('"', start_link)
    # get the position of the end double quotes
    end_qoute = page.find('"', start_qoute+1)
    # extract the url which is located between the stat and the end double quotes
    url = page[start_qoute+1: end_qoute]
    # return the link
    # return end double quotes position to know where to start the next time
    return url, end_qoute


# get the links in a page
def get_all_links(link):
    # get the page
    page = get_htlm(link)
    # clean the page from all tags
    clean_page = clean_web_page(page)
    # remove the special characters
    words = remove_special_characters(clean_page)
    # index the content of the page
    indexing(link, words)
    # create new list to store the links
    Links = []
    # while the page contains links
    while True:
        # get a link
        url, end_pos = get_next_link(page)
        # if there is a link
        if url:
            # check if the link is new
            if url not in Links:
                # add the new link to the links list
                Links.append(url)
            # get the rest of the page
            page = page[end_pos:]
        # if no link found
        else:
            break
    # return all links that found in the page
    return Links


# to crawl web
def crawl_web(seed):
    global to_crawl
    global crawled
    # add the given link to to_crawl list
    to_crawl.append(seed)
    # while there is a link to crawl
    while len(to_crawl) != 0 and len(crawled) < 500:
        # pop a link from to_crawl list
        link = to_crawl.pop()
        # if the link was not crawled before
        if link not in crawled:
            # crawl that link and add the new links found in the page
            links = union(to_crawl, get_all_links(link))
            # add the link to crawled list
            crawled.append(link)
            # add the new links th to_crawl list
            append_list(to_crawl, links)
    # return crawled and to_crawl lists
    return crawled, to_crawl


# start crawling
def crawl():
    # the seed links
    seeds = ['https://en.wikipedia.org/wiki/Ai']
    # crawl every links in the seeds lists
    for seed in seeds:
        crawled, to_crawl = crawl_web(seed)
    # print result
    print("crawled : ", len(crawled))
    print("to crawled : ", len(to_crawl))