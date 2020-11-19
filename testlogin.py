#test login
#Creating URL, usr/pass and user agent variables

BASE_URL = 'https://www.instagram.com/'
LOGIN_URL = BASE_URL + 'accounts/login/ajax/'
USERNAME = 'zuhrul.inc@gmail.com'
PASSWD = '#PWD_INSTAGRAM_BROWSER:10:1597642290:AUJQACdOp//rgXKjiWTxcK3xQu64UXrWlhRawK1WmpilnmV8nKZnZiwR2DoezokWLwilEAsN8+QccvMNAq50+XJoyFsILG/FoIsERIW36oqEyjq+3tPoSiNpp2tRZG+LOoW5TNf1cZXTd6s//2Y='
USER_AGENT = None
proxyAddress = None

#Setting some headers and refers
session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})

req = session.get(BASE_URL)
print(req.cookies)
