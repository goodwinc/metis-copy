#!/usr/bin/env python

# make executable with `chmod +x map.py`
# run map on an input file with `cat input.txt | ./map.py `

import sys

for line in sys.stdin:
    tweet_dict = eval(line)
    
#     print(tweet_dict.keys())
    print(tweet_dict["user"]["screen_name"])
