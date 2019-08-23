#!/usr/bin/python

"""
Python script to set bing image of the day as desktop wallpaper
OS: Ubuntu 16.04
Author: Anurag Rana
More Info: https://www.pythoncircle.com
"""

import datetime
import json
import os

import requests

# get image url
response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
image_data = json.loads(response.text)

image_url = image_data["images"][0]["url"]
image_url = image_url.split("&")[0]
full_image_url = "https://www.bing.com" + image_url

# image's name
image_name = datetime.date.today().strftime("%Y%m%d")
image_extension = image_url.split(".")[-1]
image_name = image_name + "." + image_extension

# download and save image
img_data = requests.get(full_image_url).content
with open(image_name, 'wb') as handler:
    handler.write(img_data)

# ubuntu command to set wallpaper
os.system("`which gsettings` set org.gnome.desktop.background picture-uri file:$PWD/" + image_name)
