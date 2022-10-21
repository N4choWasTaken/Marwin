import requests


def get_german_name():
    return requests.get('https://api.namefake.com/german_germany/random').json()['name']
