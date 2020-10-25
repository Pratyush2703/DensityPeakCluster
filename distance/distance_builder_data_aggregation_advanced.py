#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# data reference : R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems"

from distance_builder import *
from distance import *
from sklearn import manifold
import matplotlib.pyplot as plt

import numpy as np

if __name__ == '__main__':
    builder = DistanceBuilder()
    builder.load_points(r'../data/data_others/aggregation.txt')

    xdata = builder.vectors[:, 0]
    ydata = builder.vectors[:, 1]
    grouping = []
    load = 5
    limit = 20
    ydata_max = 30
    xdata_max = 40
    set = (xdata_max)*(ydata_max)/(load*load)
    count = [0]*set

    for element in range(len(xdata)):
       # print element
        group = 0
        group += int(xdata[element]/load)
        group += int((ydata[element]/load))*(xdata_max/load)
        # print group
        grouping.append(group)
        count[group] += 1

    plt.plot(xdata, ydata, linestyle='', marker='.', color='r')
    plt.title("Data Set")

    # plt.plot(xdata, ydata, 'b')
    _, __, xcount, ycount = 0, 0, 0, 0
    while (_ <= ydata_max):
        plt.axhline(y=_)
        _ += load
        ycount += 1

    while (__ <= xdata_max):
        plt.axvline(x=__)
        __ += load
        xcount += 1

    plt.grid(b=False)
    # plt.show()

    vector2 = builder.vectors
    vector3 = builder.vectors
    for _ in range(len(xdata)):
        if (count[grouping[_]] < limit):
            xdata[_] = 0
            ydata[_] = 0

    plt.plot(xdata, ydata, linestyle='', marker='.', color='b')
   # plt.show()

    finalvectors = np.dstack((xdata, ydata))
    finalvectors = finalvectors[0]
    # finalvectors = finalvectors[finalvectors != [0, 0]]
    #finalvectors = np.delete(finalvectors, [0, 0], 0)
    print finalvectors
    # print (builder.vectors)
    builder.load_vectors(finalvectors)
    builder.build_distance_file_for_cluster(
        SqrtDistance(), r'../data/data_others/aggregation_distance.dat')
    # 788
