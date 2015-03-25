#! /usr/bin/env python3
# coding: utf-8
import ast
import datetime
import urllib.request

'''
In forecast_history.txt: first list is minimal day temperature, second is maximum.
First value in lists is the date's value, others are the forecast for next days.
'''

URL = 'http://www.weather24.com/7days/r/Minsk-BY0MI0001.html'
today = datetime.datetime.now().strftime('%Y-%m-%d')

# get page
page = urllib.request.urlopen(URL)
content = page.read().decode(encoding='UTF-8')
lines = content.split('\n')

# extract info
t_min_raw_str = lines[2237].strip()
t_max_raw_str = lines[2238].strip()
t_min_raw = ast.literal_eval(t_min_raw_str[12:-1])
t_max_raw = ast.literal_eval(t_max_raw_str[12:-1])
t_min = [it[1] for it in t_min_raw]
t_max = [it[1] for it in t_max_raw]

# save info
save_line = '{}: {},\n            {}\n'.format(today, t_min, t_max)
with open('forecast_history.txt', 'a') as f:
    f.write(save_line)
