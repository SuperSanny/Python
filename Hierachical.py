#import libraries

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#create a blob of 200 data points

dataset = make_blobs(n_samples=200, centers=4, n_features=2, cluster_std=1.6, random_state=50)
print(dataset)
points = dataset[0]

#import hierarchy

import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#create a dendrogram

dendrogram = sch.dendrogram(sch.linkage(points, method='ward'))
plt.show()

#plot the dataset

plt.scatter(dataset[0][:,0], dataset[0][:,1])
plt.show()

#perform clustering

hc = AgglomerativeClustering(n_clusters=4, affinity='euclidean',linkage='ward')

#plot the cluseters

y_hc = hc.fit_predict(points)
plt.scatter(points[y_hc == 0,0], points[y_hc == 0, 1], s = 100, c = 'green')
plt.scatter(points[y_hc == 1,0], points[y_hc == 1, 1], s = 100, c = 'red')
plt.scatter(points[y_hc == 2,0], points[y_hc == 2, 1], s = 100, c = 'yellow')
plt.scatter(points[y_hc == 3,0], points[y_hc == 3, 1], s = 100, c = 'violet')
plt.show()

