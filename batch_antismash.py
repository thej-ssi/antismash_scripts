#!/usr/bin/env python3
import os
import sys


in_dir = sys.argv[1]
out_dir = sys.argv[2]

files = os.listdir(in_dir)


if not os.path.exists(out_dir):
	os.makedirs(out_dir)

missing_gbk_list = []
found_gbk_list = []
for file in files:
	if file.endswith('.gbk') or file.endswith('.gbff'):
		if file.endswith('.gbk'):
			gbk_path = os.path.join(in_dir,file)
			out_path = os.path.join(out_dir,file[:-4])
		elif file.endswith('.gbff'):
			gbk_path = os.path.join(in_dir,file)
			out_path = os.path.join(out_dir,file[:-5])
		if os.path.exists(gbk_path) and not os.path.exists(out_path):
			cmd = "antismash --output-dir " + out_path + " " + gbk_path
			sbatch_cmd = "sbatch -D . -c 4 --mem=12G --time=48:00:00 -J \"antismash\" -p project --wrap=\""+cmd+"\""
			found_gbk_list.append(gbk_path)
			print(sbatch_cmd)
			os.system(sbatch_cmd)
		else:
			missing_gbk_list.append(gbk_path)


print("Submitted antismash jobs for "+str(len(found_gbk_list))+" genbank files\n")
print(str(len(missing_gbk_list))+" folders without gbk files where identified in input folder\n")
if len(missing_gbk_list) > 0:
	print('\t'.join(missing_gbk_list))
