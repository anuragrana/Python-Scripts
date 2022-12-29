import requests
import json
import time

url = "https://www.olx.in/api/locations?parent={parent_location}&withStats=true&hideAddressComponents=true&lang=en-IN"

headers = {
    'authority': 'www.olx.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9',
    'cookie': 'bm_sv=DFF51C5DF6385866C12732BC2F3D291C~YAAQvyEPF+iEEFiFAQAAUwC3WRI4JpG0IPgyWlh8nRH+DNHVAiK26LYDu3uEGpFRy9R8jNGi4VrUjcUS9RNfvPwvJKKcFXOGq6FxRErkoljeNDlTUdcfbzorVFUF/wwx5qSSrggf4vid/UuClaqMKmmjCyidFaoJCMVOZslp93VuwUfh1ohLqbntmxygnvrXI5sboH1Cu1j8rnBwppPkHUujmg48Nrl5PE/5wQbwQ8/BQhqrGV84fXELYfjIzUZs9w==~1',
    'referer': 'https://www.olx.in/post/attributes',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-panamera-fingerprint': '103da644705db87cc823a99d71e93bce#1672235552859'
}

############## step 1 - get the response of fetching states and dump in a file ##############
############## Now get the cities in each state by hitting the curl #########################
############## If 401 response, get the new cookies from browser and use them ###############

# state_data = None
# with open("/home/rana/parent-state.txt", "r") as fh:
#     state_data = fh.read()
#
#
# state_data = json.loads(state_data)
# print(state_data)
# print(type(state_data))
#
# state_data = state_data['data']
# for state in state_data:
#     response = requests.get(url.format(parent_location=state['id']), headers=headers)
#
#     print(response.status_code)
#
#     with open("/home/rana/city_" + str(state['id'] ) + '.txt', 'w') as f:
#         f.write(response.text)
#     time.sleep(5)

########## step 2 - get all cities from the cities files ##############################
# import os
#
# files = os.listdir("/home/rana/")
#
# all_cities = []
#
# for f in files:
#     if "city_" in f:
#         print(f)
#         with open("/home/rana/" + f, 'r') as fh:
#             data = fh.read()
#             data = json.loads(data)
#             data = data['data']
#             for city in data:
#                 city.pop('stats', None)
#                 all_cities.append(city)
#
# with open("/home/rana/" + 'all_cities.txt', 'w') as fh:
#     fh.write(json.dumps(all_cities))



############# step 3 - for each city, get locality list ################

# city_data = None
# with open("/home/rana/all_cities.txt", "r") as fh:
#     city_data = fh.read()
#
#
# city_data = json.loads(city_data)
#
# cookies = None
#
# for city in city_data:
#     if cookies is None:
#         response = requests.get(url.format(parent_location=city['id']), headers=headers)
#     else:
#         # if we have collected cookies from response, use them for next request
#         headers.pop('cookie', None)
#         response = requests.get(url.format(parent_location=city['id']), headers=headers, cookies=cookies)
#
#     print(response.status_code)
#     if response.status_code == 401:
#         exit
#
#     if response.status_code == 200:
#         with open("/home/rana/locality/locality_" + str(city['id'] ) + '.txt', 'w') as f:
#             f.write(response.text)
#
#         for cookie in response.cookies:
#             print(cookie)
#
#         # use cookie from this response in next request
#         cookies = response.cookies
#
#         time.sleep(2)


############# step 4 - parse all state, city and locality files and store in DB or create a single JSON file ########

# I have placed files in separate folder. Content is original as received from API
home = '/home/rana/'
state = home + 'state/'
city = home + 'city/'
locality = home + 'locality/'




