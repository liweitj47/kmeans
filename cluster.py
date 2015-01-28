#!/usr/bin/python
from __future__ import division

class Point:
    def __init__(self,key, vector):
        self.key = key 
        self.dim = len(vector) 
        self.vector = vector 
        self.norm = 0
        self.cal_norm()
        self.cluster = None

    def cal_norm(self):
        for i in range(self.dim):
            self.norm += self.vector[i] ** 2


    def distance(self, other):
        dot_product = 0
        for i in range(self.dim):
            dot_product = self.vector[i] * other.vector[i]
        return dot_product /(self.norm * other.norm)

    def set_cluster(self, clusters):
        min_dist = 10000
        min_index = 0
        for i in range(len(clusters)):
            dist = self.distance(clusters[i].centroid)
            if dist < min_dist:
                min_dist = dist
                min_index = i
        self.cluster = min_index


class Cluster:
    def __init__(self, centroid):
        self.points = []
        self.centroid = centroid

    def set_centroid(self):
        dim = self.points[0].dim
        new_centroid = [0 for i in range(dim)]
        for point in self.points:
            for j in range(dim):
                new_centroid[j] += point.vector[j]
        new_centroid = [num/len(self.points) for num in new_centroid]
        self.centroid = Point(None, new_centroid)
        self.points = []

import sys
import re
import random

if __name__ == '__main__':
    fname = open(sys.argv[1]).readlines()
    p_space = re.compile('[\\s]+')
    K = int(sys.argv[2])
    points = []
    for i in range(0,len(fname),2):
        key = fname[i].strip().decode('utf8')
        vector = [float(num) for num in re.split(p_space, fname[i+1].strip())]
        points.append(Point(key, vector))
    dim = points[0].dim
    clusters = [Cluster(Point(None,[random.uniform(-1,1) for i in range(dim)])) for j in range(K)]
    while True:
        same_cluster = 0
        for i in range(len(points)):
            old_cluster = points[i].cluster
            points[i].set_cluster(clusters)) 
            if old_cluster == points[i].cluster:
                same_cluster += 1
            clusters[points[i].cluster].points.append(points[i])
        for c in clusters:
            c.set_centroids()
        if same_cluster == len(points):
            break
