#!/usr/bin/env python3
import os
import sys
import shutil

antismash_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
	os.makedirs(output_folder)

IDs = os.listdir(antismash_folder)

for ID in IDs:
	path = os.path.join(antismash_folder,ID)
	files = os.listdir(path)
	for file in files:
		if file.endswith('.gbk') and file.find('region') != -1:
			src = os.path.join(path,file)
			dst = os.path.join(output_folder,ID+'__'+file)
			shutil.copy2(src,dst)