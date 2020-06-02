#!/usr/bin/env python3
import os
import sys


in_dir = sys.argv[1]
out_dir = sys.argv[2]

in_folders = os.listdir(in_dir)

for folder in in_folders:
	if os.path.isdir(os.path.join(in_dir,folder)):
		files = os.listdir(os.path.join(in_dir,folder))
		prokka_ID = '.'.join(files[1].split('.')[:-1])
		gbk_path = os.path.join(in_dir,folder,prokka_ID+'.gbk')
		out_path = os.path.join(out_dir,folder)
		cmd = "antismash --output-dir " + out_path + " " + gbk_path
		if os.path.exists(gbk_path):
			print(cmd)
		else:
			print('err ' + cmd)