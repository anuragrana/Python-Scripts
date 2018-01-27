# script to scrap tweets by a twitter user.
# Author - ThePythonDjango.Com
# dependencies - BeautifulSoup, requests

from bs4 import BeautifulSoup
import requests
import sys
import json


def usage():
    msg = """
    Please use the below command to use the script.
    python script_name.py twitter_username
    """
    print(msg)
    sys.exit(1)


def get_tweet_text(tweet):
    tweet_text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
    images_in_tweet_tag = tweet_text_box.find_all("a", {"class": "twitter-timeline-link u-hidden"})
    tweet_text = tweet_text_box.text
    for image_in_tweet_tag in images_in_tweet_tag:
        tweet_text = tweet_text.replace(image_in_tweet_tag.text, '')

    return tweet_text

def get_this_page_tweets(soup):
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})
    for tweet in tweets:
        tweet_data = None
        try:
            tweet_data = get_tweet_text(tweet)
        except Exception as e:
            continue
            #ignore if there is any loading or tweet error

        if tweet_data:
            tweets_list.append(tweet_data)
            print(".", end="")
            sys.stdout.flush()

    return tweets_list


def get_tweets_data(username, soup):
    tweets_list = list()
    tweets_list.extend(get_this_page_tweets(soup))

    next_pointer = soup.find("div", {"class": "stream-container"})["data-min-position"]

    while True:
        next_url = "https://twitter.com/i/profiles/show/" + username + \
                   "/timeline/tweets?include_available_features=1&" \
                   "include_entities=1&max_position=" + next_pointer + "&reset_error_state=false"

        next_response = None
        try:
            next_response = requests.get(next_url)
        except Exception as e:
            # in case there is some issue with request. None encountered so far.
            print(e)
            return tweets_list

        tweets_data = next_response.text
        tweets_obj = json.loads(tweets_data)
        if not tweets_obj["has_more_items"] and not tweets_obj["min_position"]:
            # using two checks here bcz in one case has_more_items was false but there were more items
            print("\nNo more tweets returned")
            break
        next_pointer = tweets_obj["min_position"]
        html = tweets_obj["items_html"]
        soup = BeautifulSoup(html, 'lxml')
        tweets_list.extend(get_this_page_tweets(soup))

    return tweets_list


# dump final result in a json file
def dump_data(username, tweets):
    filename = username+"_twitter.json"
    print("\nDumping data in file " + filename)
    data = dict()
    data["tweets"] = tweets
    with open(filename, 'w') as fh:
        fh.write(json.dumps(data))

    return filename


def get_username():
    # if username is not passed
    if len(sys.argv) < 2:
        usage()
    username = sys.argv[1].strip().lower()
    if not username:
        usage()

    return username


def start(username = None):
    username = get_username()
    url = "http://www.twitter.com/" + username
    print("\n\nDownloading tweets for " + username)
    response = None
    try:
        response = requests.get(url)
    except Exception as e:
        print(repr(e))
        sys.exit(1)
    
    if response.status_code != 200:
        print("Non success status code returned "+str(response.status_code))
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'lxml')

    if soup.find("div", {"class": "errorpage-topbar"}):
        print("\n\n Error: Invalid username.")
        sys.exit(1)

    tweets = get_tweets_data(username, soup)
    # dump data in a text file
    dump_data(username, tweets)
    print(str(len(tweets))+" tweets dumped.")


start()
