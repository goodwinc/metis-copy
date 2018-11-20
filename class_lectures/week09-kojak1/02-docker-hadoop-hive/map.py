#!/usr/bin/env python
from __future__ import print_function
import sys

for line in sys.stdin:
    try:
        print(eval(line)['user']['screen_name'])
    except:
        pass
