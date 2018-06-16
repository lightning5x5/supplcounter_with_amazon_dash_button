#!/usr/bin/env python3

import os
import time
import datetime
import csv


today = datetime.datetime.now().strftime('%Y/%m/%d')
path_csv = '/your/path/here/suppl_log.csv'

# 読み込み用
read_f = open(path_csv, 'r')
lines = read_f.readlines()
data_tail = lines[len(lines) - 1]

# 書き込み用
write_f = open(path_csv, 'a')
writer = csv.writer(write_f, lineterminator='\n')

if data_tail == (today + '\n'):
    # M/Bから警告音を3回鳴らす
    for _ in range(3):
        os.system('beep -l 800')
        time.sleep(0.5)
else:
    writer.writerow([today])

read_f.close()
write_f.close()
