#!/usr/bin/python

"""
Python script to set bing image of the day as desktop wallpaper
OS: Ubuntu 16.04
Author: Anurag Rana
More Info: https://www.pythoncircle.com
"""

"""
LICENCE

Copyright 2020 Anurag Rana
Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in the 
Software without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies 
or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

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
