import sys
import urllib
import urllib.request
import json

VK_API = 'https://vk.com/share.php'

FB_API = 'https://graph.facebook.com/'

def parse_vk_response(vk_response):
    return vk_response.split(', ')[1].split(');')[0]

def parse_fb_response(fb_response):
    return str(json.loads(fb_response)['share']['share_count'])

def get_count(url, fb_token=None):
    '''
    Returns tab separated string: url, shares on VK, shares on FB
    '''
    # VK
    vk_api_params = {
        'act': 'count',
        'url': url
    }
    vk_response = urllib.request.urlopen(
        VK_API + '?' + urllib.parse.urlencode(vk_api_params)
    ).read().decode('utf-8')
    vk_count = parse_vk_response(vk_response)

    # FB
    fb_api_params = {
        'fields': 'share',
        'id': url,
        'access_token': fb_token
    }
    if fb_token:
        fb_response = urllib.request.urlopen(
            FB_API + '?' + urllib.parse.urlencode(fb_api_params)
        ).read().decode('utf-8')
        fb_count = parse_fb_response(fb_response)
    else:
        fb_count = 'no_fb_token'

    return '\t'.join([url, vk_count, fb_count])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please specify at least 1 parameter (url to check)')
        exit()

    print('\t'.join(['url', 'vk_count', 'fb_count']))

    url = sys.argv[1]
    parameter_name = parameter_num = fb_token = None
    if len(sys.argv) > 2:
        parameter_name = sys.argv[2]
        parameter_num = int(sys.argv[3])
    if len(sys.argv) > 4:
        fb_token = sys.argv[4] # https://developers.facebook.com/tools/accesstoken/

    url = url.strip('/')
    print(get_count(url, fb_token))
    print(get_count(url + '/', fb_token))

    if parameter_num:
        for i in range(parameter_num):
            print(
                get_count(url + '?' + parameter_name + '=' + str(i), fb_token)
            )