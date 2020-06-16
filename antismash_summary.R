library(gplots)
d = read.table("/Volumes/data/MPV/THEJ/antismash_testing/GCF_presence_absence.tsv",header=TRUE,row.names = 1)
dim(d)
colSums(d)
rowSums(d)


heatmap.2(as.matrix(d), trace = "none")
