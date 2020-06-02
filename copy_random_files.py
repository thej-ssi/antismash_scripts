#!/usr/bin/env python3

import os
import sys
import shutil
from random import sample


in_dir = sys.argv[1]
out_dir = sys.argv[2]
x = int(sys.argv[3])


files = os.listdir(in_dir)

try:
	cp_list = sample(files,x)
	for file in cp_list:
		src = os.path.join(in_dir,file)
		dst = os.path.join(out_dir,file)
		shutil.copy2(src,dst)
except:
	"error, x larger than number of files"
