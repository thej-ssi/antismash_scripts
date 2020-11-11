#!/usr/bin/env python3
import os
import sys

antismash_folder = sys.argv[1]


IDs = os.listdir(antismash_folder)

BGCs = []
BGC_dict = {}

BGC_to_fam = {}

#domain_dir = os.path.join(antismash_folder,'cache/domains')
#files = os.listdir(domain_dir)



for ID in IDs:
	BGC_dict[ID] = []
	path = os.path.join(antismash_folder,ID)
	files = os.listdir(path)
	for file in files:
		if file.endswith('.gbk') and file.find('region') != -1:
			if file not in BGCs:
				BGCs.append(file)
			BGC_dict[ID].append(file)


print('ID'+'\t'+'\t'.join(BGCs))

for ID in IDs:
	printlist = [ID]
	for BGC in BGCs:		
		if BGC in BGC_dict[ID]:
			printlist.append('1')
		else:
			printlist.append('0')
	print('\t'.join(printlist))