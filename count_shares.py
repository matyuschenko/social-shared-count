#!/usr/local/bin/python3
import urllib.request
import json
import datetime

###
# Script counts Facebook shares of url and its variations
# with different values (integers) of specified parameter
###

url = 'https://yandex.ru/company/researches/2017/moscow_districts/' # target url
fb_api_url = 'https://graph.facebook.com/?fields=share&id=' # Facebook api url
vk_api_url = 'https://vk.com/share.php?act=count&url='  # VK api url
param_codes = range(5)  # range of integers in parameters of url or None
add_names = True  # replace param codes with names in result
param_name = 'res'  # name of parameter containing codes

# You need to set up a Facebook app
# and get an access_token to run this script.
# Details: https://developers.facebook.com/tools/accesstoken/
# Save your token into the TOKEN file
with open('TOKEN', 'r') as f:
    TOKEN = f.read()

# You can add human-readable labels for your codes in parameters.
# Save them in param_names file in the same order as codes go (1-...)
if param_codes and add_names:
    with open('param_names.txt', 'r') as f:
        param_names = f.readlines()
        param_names = [x.strip() for x in param_names]
else:
    param_names = [str(x+1) for x in param_codes]

if url[-1] == '/':
    url = url[:-1]

def get_response(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def parse_fb_response(text):
    _count = str(json.loads(text)['share']['share_count'])
    print('FB\t' + _count)
    return _count

def parse_vk_response(text):
    _count = text\
        .replace('VK.Share.count(0, ', '')\
        .replace(');', '')
    print('VK\t' + _count)
    return _count

def count_shares(url, social_name, api_url, token=''):
    html = get_response(api_url + url + token)

    print(url)
    if social_name == 'fb':
        _count = parse_fb_response(html)
    elif social_name == 'vk':
        _count = parse_vk_response(html)
    return _count

def stringify_result(name, *_counts):
    return name + '\t' + '\t'.join(_counts) + '\n'

if __name__ == '__main__':
    with open('count.txt', 'w') as f:
        f.write('Scraping time: ' + str(datetime.datetime.now()) + '\n')
        f.write('url\tFB\tVK\n')

        f.write(stringify_result(
            url,
            count_shares(url, 'fb', fb_api_url, '&access_token=' + TOKEN),
            count_shares(url, 'vk', vk_api_url)
        ))
        f.write(stringify_result(
            url + '/',
            count_shares(url + '/', 'fb', fb_api_url, '&access_token=' + TOKEN),
            count_shares(url + '/', 'vk', vk_api_url)
        ))

        if param_codes:
            for c in param_codes:
                _count_fb = count_shares(url + '/?res=' + str(c+1), 'fb', fb_api_url, '&access_token=' + TOKEN)
                _count_vk = count_shares(url + '/?res=' + str(c+1), 'vk', vk_api_url)
                result = stringify_result(param_names[c], _count_fb, _count_vk)
                f.write(result)