#test login
#Creating URL, usr/pass and user agent variables

import requests
import json
import sys
import time
import random


BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"
proxyAddress = None

#Setting some headers and refers
session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})

req = session.get(BASE_URL)
req = session.get(BASE_URL)
print(req.cookies)
