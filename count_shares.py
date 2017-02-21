#!/usr/local/bin/python3
import urllib.request
import json
import datetime

###
# Script counts Facebook shares of url and its variations
# with different values (integers) of specified parameter
###

url = 'https://yandex.ru/company/researches/2017/moscow_districts/' # target url
api_url = 'https://graph.facebook.com/?fields=share&id=' # Facebook api url
param_codes = range(118)  # range of integers in parameters of url or None
param_name = 'res'  # name of parameter containing codes

# You need to set up a Facebook app
# and get an access_token to run this script.
# Details: https://developers.facebook.com/tools/accesstoken/
# Save your token into the TOKEN file
with open('TOKEN', 'r') as f:
    TOKEN = f.read()

# You can add human-readable labels for your codes in parameters.
# Save them in param_names file in the same order as codes go (1-...)
add_names = False
if param_codes and add_names:
    with open('param_names.txt', 'r') as f:
        param_names = f.readlines()
        param_names = [x.strip() for x in param_names]
else:
    param_names = [str(x+1) for x in param_codes]

if url[-1] == '/':
    url = url[:-1]

def count_fb_shares(url, api_url=api_url):
    req_url = api_url + url + '&access_token=' + TOKEN
    with urllib.request.urlopen(req_url) as response:
        html = response.read().decode('utf-8')

    _count = json.loads(html)['share']['share_count']
    print(url + '\t' + str(_count))
    return _count

def stringify_result(name, _count):
    return name + '\t' + str(_count) + '\n'

if __name__ == '__main__':
    with open('count.txt', 'w') as f:
        f.write(str(datetime.datetime.now()) + '\n')

        f.write(stringify_result(url, count_fb_shares(url)))
        f.write(stringify_result(url + '/', count_fb_shares(url + '/')))

        if param_codes:
            for c in param_codes:
                _count = count_fb_shares(url + '/?res=' + str(c+1))
                result = stringify_result(param_names[c], _count)
                f.write(result)