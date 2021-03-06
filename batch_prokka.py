#!/usr/bin/env python3

import os
import sys

in_dir = sys.argv[1]
out_dir = sys.argv[2]

files = os.listdir(in_dir)

for file in files:
	path = os.path.join(in_dir,file)
	out_path = os.path.join(out_dir,file)
	if not os.path.exists(out_path):
		cmd = "sbatch -D . -c 4 --mem=12G --time=48:00:00 -J \"spl_prokka\" -p project --wrap=\"prokka "+path+" --outdir "+out_path+" --compliant --force\""
		os.system(cmd)
	#print(cmd)
	
