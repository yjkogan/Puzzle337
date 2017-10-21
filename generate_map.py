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
          split = [split[0], int(split[1])]
          arr.append(split)
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
  # Answer: Ethiopia (+251)
  to_array('data/astronauts.csv', './puzzle/1.html', 'Germany, US', 2, 'AIzaSyD7L4w39LZ22obci_jIoZ5iT-DoccCtrw8')
  # Answer: Iceland (+354)
  to_array('data/survivor.csv', './puzzle/2.html', 'Panama, Fiji, Philippines', 1, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk')
  # Answer: Indonesia (+62)
  to_array('data/un.csv', './puzzle/3.html', 'Cambodia', 2, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4') # Needs own key
  # Answer: Italy (+39)
  to_array('data/olympics.csv', './puzzle/4.html', 'United Kingdom, Brazil', 1, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI') # Needs own key
  # Answer: Morocco (+212)
  to_array('data/oscars.csv', './puzzle/5.html', 'Iran, France', 3, 'AIzaSyA0oD5trz09rmpopMLmHfyn-mtTbh3dsqk') # Needs own key
  # Answer: New Zealand (+64)
  to_array('data/worlds50best.csv', './puzzle/6.html', 'Spain, Italy', 7, 'AIzaSyDzevghJT_Wy7hwZzy5IB5bKfUBe6k14yI')
  # Answer: Nicaragua (+505)
  to_array('data/mountains.csv', './puzzle/7.html', 'China, Bhutan', 4, 'AIzaSyDke9m-rn4eIK-v39ah-RliNTfp-Zw0UGg')
  # Answer: Norway (+47)
  to_array('data/letters.csv', './puzzle/8.html', 'Mali, Bolivia', 1, 'AIzaSyA5pwIIpyL6u9kuOVs0i_KXitv65toze5c')
  # Answer: Pakistan (+92)
  to_array('data/timezones.csv', './puzzle/9.html', 'Australia, Ecuador', 8, 'AIzaSyD2kUuTMcnK0Vh41G-MMpTDIzV4sk9oTCo')
  # Answer: Paraguay (+595)
  to_array('data/nobels.csv', './puzzle/10.html', 'Argentina, China, Ukraine', 2, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8')
  # Answer: Republic of the Congo (+242)
  to_array('data/worldcup.csv', './puzzle/11.html', 'Argentina, Italy, Uruguay', 9, 'AIzaSyDGWjCK3Q6MLTfnMinDULYkSUXTn5D8GR4')
  # Answer: South Korea (+82)
  to_array('data/languages.csv', './puzzle/12.html', 'Norway, Canada', 9, 'AIzaSyCDB45ZVFNENiV2bUO92tzHO095stqd7F8') # Needs own key
  # Answer: Sri Lanka (+94)
  to_array('data/flag_stars.csv', './puzzle/13.html', 'Tuvalu, New Zealand', 3, 'AIzaSyAqBmcAT2lia1AEt_6VvvOqydE8rQ8rlpc')
