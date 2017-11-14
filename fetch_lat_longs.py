#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import os
import urllib
import urllib2

def fetch_addresses():
  countries = set()
  for data_file in os.listdir('data'):
    with open('data/' + data_file, 'r') as f:
      row = 0
      for l in f.xreadlines():
        if row == 0:
          row += 1
          continue
        split = l.strip().split(',')
        countries.add(split[0].strip())
        row += 1

  # print "number of unique countries"
  # print len(countries)
  # countries_list = list(countries)
  # countries_list.sort()
  # print countries_list
  # exit()

  GOOGLE_MAPS_LOOKUP_ADDRESS = 'https://maps.googleapis.com/maps/api/geocode/json?address='

  country_to_location = {}
  for country in countries:
    url_to_fetch = GOOGLE_MAPS_LOOKUP_ADDRESS + urllib.quote_plus(country) + '&key=AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8'
    print 'Fetching ', url_to_fetch
    response = urllib2.urlopen(url_to_fetch)
    data = json.load(response)
    print len(data['results'])
    location = data['results'][0]['geometry']['location']
    country_to_location[country] = location

  with open('lat_lngs.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['Country', 'Lat', 'Long'])
    for c, l in country_to_location.iteritems():
      writer.writerow([c, l['lat'], l['lng']])

if __name__ == '__main__':
  fetch_addresses()
