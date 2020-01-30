import csv
import argparse

from bs4 import BeautifulSoup
import requests

from urllib.parse import urlparse
import os

import json

teams = {'black':[], 'blue':[], 'brown':[], 'champion':[], 'green':[], 'purple':[], 'red':[], 'white':[], 'yellow':[]}

fieldnames = ['Name', 'Gender', 'Sign', 'Brave', 'Faith', 'Class', 'ActionSkill', 'ReactionSkill', 'SupportSkill', 'MoveSkill', 'Mainhand', 'Offhand', 'Head', 'Armor', 'Accessory', 'ClassSkills', 'ExtraSkills']

tiko_url = 'https://fftbg.com/tournament/%s/json'
latest_string = 'latest'

parser = argparse.ArgumentParser(description='Formats a folder of FFTBG team dumps')
parser.add_argument('-t', '--tournament', dest='tournament', help="Tournament ID number (or latest).", default=latest_string, nargs='?')

args = parser.parse_args()

tournament = args.tournament

url = tiko_url % tournament

data = json.loads(requests.get(url).text)
# print(json.dumps(data, sort_keys=True, indent=4))
for team in data['Teams']:
    for character in data['Teams'][team]['Units']:
        teams[team].append(character)
        
for team in teams:
    with open(team+'.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for character in teams[team]:
            writer.writerow(character)