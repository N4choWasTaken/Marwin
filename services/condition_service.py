import requests


def get_conditions():
    return requests.get("https://www.dnd5eapi.co/api/conditions/").json()['results']
