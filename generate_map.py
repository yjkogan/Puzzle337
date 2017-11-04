#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from string import Template

template_file = './template.html'

def to_array(in_file, out_file, order, index, apikey):
  arr = []
  with open(in_file, 'r') as f:
    row = 0
    for l in f.xreadlines():
      split = l.strip().split(',')
      if row == 0:
        arr.append(split)
        row += 1
        continue
      else:
        try:
          data_point = [split[0], int(split[1])]
          if len(split) == 3:
            data_point.append(split[2])
          arr.append(data_point)
        except ValueError:
          continue
  

  with open(template_file, 'r') as t:
    src = Template(t.read())
    with open(out_file, 'w+') as o:
      o.write(src.substitute({
        'apikey': apikey,
        'dataarray': str(arr),
        'index': index,
        'order': order,
      }))

if __name__ == '__main__':
  # Answer: Argentina (+54)
  to_array('data/billionaires.csv', './puzzle/1.html', 'KazakhstanMonaco', 1, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8')
  # Answer: Ethiopia (+251)
  to_array('data/reactors.csv', './puzzle/2.html', 'BrazilSwitzerlandArmenia', 2, 'AIzaSyD7L4w39LZ22obci_jIoZ5iT-DoccCtrw8')
  # Answer: Iceland (+354)
  to_array('data/survivor.csv', './puzzle/3.html', 'PanamaFijiPhilippines', 1, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk')
  # Answer: Indonesia (+62)
  to_array('data/un.csv', './puzzle/4.html', 'Cambodia', 2, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4') # Needs own key
  # Answer: Morocco (+212)
  to_array('data/oscars.csv', './puzzle/5.html', 'IranFrance', 3, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk') # Needs own key
  # Answer: New Zealand (+64)
  to_array('data/worlds50best.csv', './puzzle/6.html', 'SpainItaly', 7, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI')
  # Answer: Nicaragua (+505)
  to_array('data/mountains.csv', './puzzle/7.html', 'ChinaBhutan', 4, 'AIzaSyDke9m-rn4eIK-v39ah-RliNTfp-Zw0UGg')
  # Answer: Denmark (+45)
  to_array('data/letters.csv', './puzzle/8.html', 'UnitedKingdom', 3, 'AIzaSyA5pwIIpyL6u9kuOVs0i_KXitv65toze5c')
  # Answer: Pakistan (+92)
  to_array('data/timezones.csv', './puzzle/9.html', 'UnitedKingdomEcuador', 8, 'AIzaSyD2kUuTMcnK0Vh41G-MMpTDIzV4sk9oTCo')
  # Answer: Republic of the Congo (+242)
  to_array('data/worldcup.csv', './puzzle/10.html', 'ArgentinaItalyUruguay', 9, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4')
  # Answer: Sri Lanka (+94)
  to_array('data/flag_stars.csv', './puzzle/11.html', 'TuvaluNewZealand', 3, 'AIzaSyAqBmcAT2lia1AEt_6VvvOqydE8rQ8rlpc')
  # Answer: Switzerland (+41)
  to_array('data/female_leaders.csv', './puzzle/12.html', 'PeruRwanda', 2, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8') # Needs own key
  # Answer: The Netherlands (+31)
  to_array('data/olympics.csv', './puzzle/13.html', 'UnitedKingdomBrazil', 1, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI') # Needs own key
