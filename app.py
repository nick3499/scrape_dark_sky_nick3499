#!/usr/bin/env python
'''Scrape weather data from Dark Sky for personal/non-commercial use.
Review DarkSky's TOS darksky.net/tos'''
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import timedelta
from requests import get
from figlet import get_figlet


print(get_figlet())  # FIGlet ASCII art title

REQ = get('https://darksky.net/forecast/40.9322,-73.899/us12/en')  # get HTML data
SOUP = BeautifulSoup(REQ.text, 'html5lib')  # instantiate parse tree
THEME = {
    'c1': '\x1b[38;2;140;28;32m',
    'c2': '\x1b[38;2;119;121;174m',
    'c3': '\x1b[38;2;213;122;100m',
    'rset': '\x1b[0m'}  # 3-color theme; `rset` resets color to default
PG_TITLE = SOUP.title.string.strip()  # web page title

print(f" {THEME['c1']}Weather data scraped from:{THEME['rset']} {PG_TITLE}")
print(f"{THEME['c1']}―――――――――――――――――――――――――――――――――――――{THEME['rset']}")
print(f" {THEME['c1']}Current conditions:{THEME['rset']}")  # subtitles

CURR_COND_STR_1 = [
    ['Current', 'summary swap', ''],
    ['Feels like', 'feels-like-text', 'F'],
    ['Low', 'low-temp-text', 'F'],
    ['High', 'high-temp-text', 'F']]  # current condition strings 1

for s1 in CURR_COND_STR_1:
    print(f" {THEME['c2']}{s1[0]:<12}{THEME['rset']}\
{SOUP.find('span', {'class': s1[1]}).string}{s1[2]}")  # print current cond 1

CURR_COND_STR_2 = [
    ['Wind speed', 'num swip wind__speed__value', ' mph'],
    ['Humidity', 'num swip humidity__value', '%'],
    ['UV index', 'num uv__index__value', ''],
    ['Visibility', 'num swip visibility__value', ' mi'],
    ['Pressure', 'num swip pressure__value', ' mb']]  # curr conds strings 2

for cls2 in CURR_COND_STR_2:
    print(f" {THEME['c3']}{cls2[0]:<12}{THEME['rset']}\
{SOUP.find('span', {'class': cls2[1]}).string}{cls2[2]}")  # print curr cond 2

FORECAST_TODAY = SOUP.find(
    'span', {'class': 'currently__summary next swap'}).string.strip()  # forecast today
FORECAST_WEEK = SOUP.find('div', {'id': 'week'}).contents[1].contents[0].strip()  # forecast week
print(f" {THEME['c3']}Forecast today:{THEME['rset']} {FORECAST_TODAY}")  # print forecast today
print(f" {THEME['c3']}Forecast week:{THEME['rset']} {FORECAST_WEEK}")  # print forecast week
print(f"{THEME['c1']}―――――――――――――――――――――――――――――――――――――{THEME['rset']}")
print(f" {THEME['c1']}Forecast:{THEME['rset']}")  # weekly forecast; temps/conditions

for i in range(0, 8):
    min_temp = SOUP.find('a', {'data-day': str(i)}).contents[3].contents[1].string
    max_temp = SOUP.find('a', {'data-day': str(i)}).contents[3].contents[5].string
    weekday_str = (datetime.now() + timedelta(days=i)).strftime('%a')
    wthr_day = SOUP.find(
        'a', {'data-day': str(i)}).contents[1].find(
            'span', {'class': 'skycon'}).img['alt'].split(' ')[0].replace(
                '-', ' ')  # condition
    print(f" {THEME['c2']}{weekday_str:<5}{THEME['rset']}{THEME['c3']}{'L':<2}\
{THEME['rset']}{min_temp:<5}{THEME['c3']}{'H':<2}{THEME['rset']}{max_temp:<5}\
{wthr_day}")  # print temps/conditions

print(f"{THEME['c1']}―――――――――――――――――――――――――――――――――――――{THEME['rset']}")

# sunrise/sunset times
SUNRISE_TIME = SOUP.find('span', {'class':'sunrise swip'}).contents[3].string
SUNSET_TIME = SOUP.find('span', {'class':'sunset swap'}).contents[3].string
print(f" {THEME['c2']}Sunrise:{THEME['rset']} {SUNRISE_TIME}\
{THEME['c2']} | Sunset:{THEME['rset']} {SUNSET_TIME}")  # print sunrise/sunset

print('') # empty line
