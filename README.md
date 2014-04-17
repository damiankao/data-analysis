data-analysis
=============

### Description

Some scripts I've used for data analysis. Mostly in Python/Javascript/R

`hierCluster` - Python script to perform hierarchical clustering with scipy and visualize with javascript (D3.js). Here is a demo: http://blog.nextgenetics.net/demo/entry0044/

`SVD` - Python script to perform singular value decomposition and partial reconstruction to smooth data. Here are 7 line graphs (http://i.imgur.com/uZmVFzT.jpg). Bottom-most graph is the full reconstruction. Each graph above are partial reconstructions, smoothing the data.

`kMeans` - Python script to perform k-means clustering. Also a function to calculate average silhouette of each cluster. The gap.R script calculates and graphs the gap statistic for each k-value.