#!/usr/bin/env python3
import sys
import os
import shutil


folder = sys.argv[1]
out_folder = sys.argv[2]

if not os.path.exists(out_folder):
	os.makedirs(out_folder)

files = os.listdir(folder)

for f in files:
	path = os.path.join(folder,f)
	files2 = os.listdir(path)
	for f2 in files2:
		if f2[-4:] == '.gbf':
			src = os.path.join(path,f2)
			dst = os.path.join(out_folder,f)
			dst = dst+'.gbk'
			print(src+'\t'+dst)
			shutil.copy2(src,dst)
