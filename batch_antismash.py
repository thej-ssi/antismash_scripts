#!/usr/bin/env python3
import os
import sys


in_dir = sys.argv[1]
out_dir = sys.argv[2]

in_folders = os.listdir(in_dir)


if not os.path.exists(out_dir):
	os.makedirs(out_dir)

missing_gbk_list = []
found_gbk_list = []
for folder in in_folders:
	if os.path.isdir(os.path.join(in_dir,folder)):
		files = os.listdir(os.path.join(in_dir,folder))
		prokka_ID = '.'.join(files[1].split('.')[:-1])
		gbk_path = os.path.join(in_dir,folder,prokka_ID+'.gbf')
		out_path = os.path.join(out_dir,folder)
		if os.path.exists(gbk_path):
			cmd = "antismash --output-dir " + out_path + " " + gbk_path
			sbatch_cmd = "sbatch -D . -c 4 --mem=12G --time=48:00:00 -J \"antismash\" -p daytime --wrap=\""+cmd+"\""
			found_gbk_list.append(gbk_path)
			print(sbatch_cmd)
			os.system(sbatch_cmd)
		else:
			missing_gbk_list.append(gbk_path)


print("Submitted antismash jobs for "+str(len(found_gbk_list))+" genbank files\n")
print(str(len(missing_gbk_list))+" folders without gbk files where identified in input folder\n")
if len(missing_gbk_list) > 0:
	print('\t'.join(missing_gbk_list))
