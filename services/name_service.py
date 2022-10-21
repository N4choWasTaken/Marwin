import requests


def get_german_name():
    return requests.get('https://api.namefake.com/german_germany/random').json()['name']

def get_english_name():
    return requests.get('https://api.namefake.com/english-united-kingdom/random').json()['name']
