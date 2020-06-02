#!/usr/bin/env python3
import os
import sys


in_dir = sys.argv[1]
out_dir = sys.argv[2]

in_folders = os.listdir(in_dir)

for folder in in_folders:
	if os.path.isdir(os.path.join(in_dir,folder)):
		missing_gbk_list = []
		found_gbk_list = []
		files = os.listdir(os.path.join(in_dir,folder))
		prokka_ID = '.'.join(files[1].split('.')[:-1])
		gbk_path = os.path.join(in_dir,folder,prokka_ID+'.gbk')
		out_path = os.path.join(out_dir,folder)
		if os.path.exists(gbk_path):
			cmd = "antismash --output-dir " + out_path + " " + gbk_path
			sbatch_cmd = "sbatch -D . -c 4 --mem=12G --time=48:00:00 -J \"antismash\" -p project --wrap=\""+cmd+"\""
			found_gbk_list.append(gbk_path)
			print(sbatch_cmd)
		else:
			missing_gbk_list.append(gbk_path)

print(missing_gbk_list)