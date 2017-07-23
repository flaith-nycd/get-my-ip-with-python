import urllib.request
import json

url_to_open = 'http://api.sotfall.com/'


def loading(what_to_load):
    url = url_to_open + what_to_load
    print('Loading {} ...'.format(url))
    res = urllib.request.urlopen(url)
    res_body = res.read().decode("utf-8")
    return json.loads(res_body)


def get_help():
    json_data = loading('get_help')
    print('-- API HELP ------')
    for key, value in json_data['help'].items():
        print('{:>12}: {}'.format(key, value))


def get_ip():
    json_data = loading('get_ip')
    print('Your IP: {}'.format(json_data['ip']))


def get_browser():
    json_data = loading('get_browser')
    print('Your browser: {}'.format(json_data['browser']))


def get_all():
    json_data = loading('get_all')
    print('Your IP: {}'.format(json_data['data'][0]['ip']))
    print('Your browser: {}'.format(json_data['data'][1]['browser']))


# get_ip()
# get_browser()
# get_all()
get_help()
