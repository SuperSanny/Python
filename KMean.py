import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.datasets import make_blobs

#generate dataset

dataset = make_blobs(n_samples=200, centers=4, n_features=2, cluster_std=1.6, random_state=50)
print(dataset)
points = dataset[0]

#import kmeans

from sklearn.cluster import KMeans

#create kmeans objects
kmeans = KMeans(n_clusters=4)

#fit the kmeans objects to the dataset

kmeans.fit(points)

#plot the dataset

plt.scatter(dataset[0][:, 0], dataset[0][:,1])
plt.show()

#print out the clusters

clusters = kmeans.cluster_centers_
print(clusters)

#plot the clusters

y_km = kmeans.fit_predict(points)
plt.scatter(points[y_km == 0, 0], points[y_km == 0, 1], s = 50, color = 'red')
plt.scatter(points[y_km == 1, 0], points[y_km == 1, 1], s = 50, color = 'green')
plt.scatter(points[y_km == 2, 0], points[y_km == 2, 1], s = 50, color = 'yellow')
plt.scatter(points[y_km == 3, 0], points[y_km == 3, 1], s = 50, color = 'cyan')
plt.show()

#position the centroids of the clusters
plt.scatter(clusters[0][0], clusters[0][1], marker='*', s= 200, color = 'black')
plt.scatter(clusters[1][0], clusters[1][1], marker='*', s= 200, color = 'black')
plt.scatter(clusters[2][0], clusters[2][1], marker='*', s= 200, color = 'black')
plt.scatter(clusters[3][0], clusters[3][1], marker='*', s= 200, color = 'black')
plt.show()