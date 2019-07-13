#!/usr/bin/python
#encoding:utf-8

import requests
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('setting.ini')
section = "settings"

url = config.get("settings", "url")
token = config.get(section, "token")
text = config.get(section, "text")
channel = config.get(section, "channel")
icon = config.get(section, "icon")

def main():
    params = {
      "token": token,
      "channel": channel,
       "icon_url": icon,
       "text": text
    }
    ret = requests.post(url, params)
    print ret.json()

# main
main()
