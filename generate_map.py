#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import plotly
import plotly.plotly as py
import pandas as pd
from string import Template

plotly.tools.set_credentials_file(username='yjkogan-harvard', api_key='7LpTZktpFhracINiPiEk')

country_to_lat_long = {}
results = []

def plot_map(in_file, out_file, order, index, api_key):
  max_count = -1
  min_count = 1000000000000
  counts = []
  lats = []
  lngs = []
  texts = []

  with open(in_file, 'r') as f:
    row = 0
    for l in f.xreadlines():
      if row == 0:
        row += 1
        continue
      split = l.strip().split(',')
      country_name = split[0].strip()
      try:
        country_count = int(split[1].strip())
      except ValueError:
        continue

      max_count = max(max_count, country_count)
      min_count = min(min_count, country_count)
      counts.append(country_count)
      lats.append(float(country_to_lat_long[country_name]['Lat']))
      lngs.append(float(country_to_lat_long[country_name]['Long']))
      texts.append(country_name + '<br />Count: ' + str(country_count))

      country = dict(
          type = 'scattergeo',
          hoverinfo = 'text',
          locationmode = 'country names',
          lon = lngs,
          lat = lats,
          text = texts,
          marker = dict(
              color = "#00a80d",
              sizemin = 5,
              size = list(map(lambda c: (c / (max_count * 1.0)) * 50, counts)),
              sizemode = 'diameter',
              line = dict(width=0.5, color='rgb(40,40,40)'),
          ),
          name = '{0} - {1}'.format(min_count, max_count)
          )

  layout = dict(
    margin = dict(
      l = 0,
      r = 0,
      t = 50,
      b = 70,
      pad = 0,
    ),
    title = '{0} ({1}) <br /> Range: {2}-{3}'.format(order, index, min_count, max_count),
    showlegend = False,
    geo = dict(
        lataxis = dict(
          range = [-5, 90],
        ),
        landcolor = '#F9FFEE',
        oceancolor = '#EAF7FE',
        scope='world',
        showcountries = True,
        showocean = True,
        showland = True,
        showframe = False,
        projection=dict(type = 'mercator')
    ),
  )

  fig = dict( data=[country], layout=layout )
  out_file_name = out_file.replace('./', '').replace('/', '')
  results.append(py.plot( fig, validate=False, filename=out_file_name ))

if __name__ == '__main__':
  lat_lng_file = 'lat_lngs.csv'
  with open(lat_lng_file, 'r') as f:
    csvReader = csv.DictReader(f)
    for c in csvReader:
      country_to_lat_long[c['Country']] = c

  # Answer: Argentina (+54)
  plot_map('data/billionaires.csv', './puzzle/1.html', 'KazakhstanMonaco', 1, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8')
  # Answer: Denmark (+45)
  plot_map('data/letters.csv', './puzzle/2.html', 'UnitedKingdom', 3, 'AIzaSyA5pwIIpyL6u9kuOVs0i_KXitv65toze5c')
  # Answer: Ethiopia (+251)
  plot_map('data/reactors.csv', './puzzle/3.html', 'BrazilSwitzerlandArmenia', 2, 'AIzaSyD7L4w39LZ22obci_jIoZ5iT-DoccCtrw8')
  # Answer: Iceland (+354)
  plot_map('data/survivor.csv', './puzzle/4.html', 'PanamaFijiPhilippines', 1, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk')
  # Answer: Indonesia (+62)
  plot_map('data/un.csv', './puzzle/5.html', 'Cambodia', 2, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4') # Needs own key
  # Answer: Morocco (+212)
  plot_map('data/oscars.csv', './puzzle/6.html', 'IranFrance', 3, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk') # Needs own key
  # Answer: Netherlands (+31)
  plot_map('data/olympics.csv', './puzzle/7.html', 'UnitedKingdomBrazil', 3, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI') # Needs own key
  # Answer: New Zealand (+64)
  plot_map('data/worlds50best.csv', './puzzle/8.html', 'SpainItaly', 7, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI')
  # Answer: Nicaragua (+505)
  plot_map('data/mountains.csv', './puzzle/9.html', 'ChinaBhutan', 4, 'AIzaSyDke9m-rn4eIK-v39ah-RliNTfp-Zw0UGg')
  # Answer: Pakistan (+92)
  plot_map('data/timezones.csv', './puzzle/10.html', 'UnitedKingdomEcuador', 8, 'AIzaSyD2kUuTMcnK0Vh41G-MMpTDIzV4sk9oTCo')
  # Answer: Republic of the Congo (+242)
  plot_map('data/worldcup.csv', './puzzle/11.html', 'ArgentinaItalyUruguay', 9, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4')
  # Answer: Sri Lanka (+94)
  plot_map('data/flag_stars.csv', './puzzle/12.html', 'TuvaluNewZealand', 3, 'AIzaSyAqBmcAT2lia1AEt_6VvvOqydE8rQ8rlpc')
  # Answer: Switzerland (+41)
  plot_map('data/female_leaders.csv', './puzzle/13.html', 'PeruRwanda', 6, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8') # Needs own key

  template_file = 'plotly_template.html'
  with open(template_file, 'r') as t:
    src = Template(t.read())
    with open('index.html', 'w+') as o:
      substitution_dict = {}
      for i in range(len(results)):
        substitution_dict['puzzle' + str(i + 1)] = results[i] + '.embed'
      print substitution_dict
      o.write(src.substitute(substitution_dict))
