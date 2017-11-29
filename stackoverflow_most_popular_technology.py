# Script to find the most used tags in questions on stackoverflow
# Author - Anurag Rana
# version - 1.0.0
# usage - python script_name


import operator, os, sys
import requests
from bs4 import BeautifulSoup


# global dictionary to store the count of tags processed so far
tag_count_dict = {}


def get_soup_from_link(link):
    html_text = requests.get(link).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup


def tag_crawler(question_url):    
    soup = get_soup_from_link(question_url)
    tag_divs = soup.find_all('div', {'class': 'post-taglist'})
    for div in tag_divs:
        for tag_link in div.find_all('a'):
            tag = tag_link.string
            if tag is not None:
                tag_count_dict[tag] = tag_count_dict[tag] + 1 if tag in tag_count_dict else 1
                # print a dot to indicate script is progressing.
                print(".", end="")
                sys.stdout.flush()


def get_question_links(soup):
    return soup.find_all('a', {'class': 'question-hyperlink'})


def page_crawler(max_page_count):
    starting_url = 'http://stackoverflow.com/questions?page=PAGE_NUMBER&sort=newest'
    current_page_number = 1
    while current_page_number <= max_page_count:
        current_page_url = starting_url.replace('PAGE_NUMBER',str(current_page_number))                
        soup = get_soup_from_link(current_page_url)       
        print('Working on page number : ' + str(current_page_number))  
        # get link of all question posted on current page      
        question_links = get_question_links(soup)
        for link in question_links:
            question_url = 'http://stackoverflow.com/' + link.get('href')
            # crawl all tags on this question page
            tag_crawler(question_url)
            
        current_page_number += 1


def print_welcome_msg():
    os.system('clear')
    print("\n\n")
    print("This script will crwal stackoverflow pages to fetch the count of occurances of tags.")
    print("And then print the top 10 tags hence predicting the most popular technology on stackoverflow.")
    print("Next we will ask you the number of pages to crawl.")
    print("Remember, more the pages, better is the accuracy but at the same time script will run longer.")
    print('\n\nHow many pages would you like to crawl : ', end="")


def start():
    print_welcome_msg()
    max_page_count = int(input().strip())
    print('Starting now....')
    page_crawler(max_page_count)    
    sorted_tag_count_dict = sorted(tag_count_dict.items(), key=operator.itemgetter(1), reverse=True)[:10]
    print("")
    for tag_count in sorted_tag_count_dict:
        print("%15s : %d" %(tag_count[0], tag_count[1]))
    
start()
