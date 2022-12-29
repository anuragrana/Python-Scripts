# python script to notify if a covid vaccine slot is available in selected district in India
# need python3 and below packages. install using command -> pip install requests
# command to run script -> python3 vaccine_slot_availability.py
# Author: Anurag Rana (https://pythoncircle.com)

import json
import time
import requests
import os
import sys

# find your district ID from cowin site drop downs
district_id = "679"
date = "04-06-2021"
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=" + district_id + "&date=" + date

payload = {}
headers = {
    'authority': 'cdn-api.co-vin.in',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'origin': 'https://www.cowin.gov.in',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.cowin.gov.in/',
    'accept-language': 'en-IN,en-US;q=0.9,en;q=0.8,hi;q=0.7',
    'if-none-match': 'W/"24cd1-gIUHe5EIOLD2Ovtn3sxK2S91wZk"'
}


def send_alert(name, count):
    for i in range(3):
        os.system("spd-say '" + str(count) + "  Slot Available at " + name + "'")
        time.sleep(5)


def search():
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    response = json.loads(response.text)

    slot_found = False

    centers = response.get("centers")
    for center in centers:
        if center.get("fee_type") == "Free":
            sessions = center.get("sessions")
            for session in sessions:
                if session.get("min_age_limit") == 18:
                    if session.get("available_capacity_dose1") > 0:
                        name = center.get("name")
                        count = session.get("available_capacity_dose1")
                        print(name, count)
                        # preform an action. send notification, play an audio file, send sms etc
                        send_alert(name, count)
                        slot_found = True
                        break

        if slot_found:
            sys.exit()


def start():
    while True:
        search()
        print("Checking...")
        time.sleep(60)


if __name__ == "__main__":
    start()
