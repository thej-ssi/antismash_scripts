#!/usr/bin/env python3

import os
import sys
import shutil
from random import sample


in_dir = sys.argv[1]
out_dir = sys.argv[2]
x = int(sys.argv[3])


files = os.listdir(in_dir)

cp_list = sample(files,x)

print(cp_list)
