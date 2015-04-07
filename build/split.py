#!/usr/bin/env python2.7

import glob
import json
import os
import re

def main():
    session_cells = {n: [] for n in range(1, 6+1)}
    f = open(os.path.dirname(__file__) + '/../All.ipynb')
    j = json.load(f)
    cells = j['cells']
    for cell in cells:
        source = u''.join(cell['source'])
        m = re.search(r'# +(\d+)\. ', source.strip())
        if not m:
            continue
        n = int(m.group(1))
        session_cells[n].append(cell)
    for n, cells in sorted(session_cells.items()):
        print 'Session {}: {} cells'.format(n, len(cells))

def convert(filename):
    f = open(filename)
    j = json.load(f)
    cells = j['cells']
    n = 0
    for cell in cells:
        if cell['cell_type'] != 'code':
            continue
        source = u''.join(cell['source'])
        if source.startswith('#'):
            n += 1
    print '{:6}   {}'.format(n, filename)
        #print cell

def main2():
    for filename in sorted(glob.glob('Solutions-*.ipynb')):
        convert(filename)

if __name__ == '__main__':
    main2()
