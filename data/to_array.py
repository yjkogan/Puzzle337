#!/usr/bin/env python

def to_array(in_file, out_file):
  arr = []
  with open(in_file, 'r') as f:
    for l in f.xreadlines():
      split = l.strip().split(',')
      arr.append(split)
  
  with open(out_file, 'w+') as o:
    o.write(str(arr))

if __name__ == '__main__':
  to_array('survivor.csv', 'survivor_arr.txt')
