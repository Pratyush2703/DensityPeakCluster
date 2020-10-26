#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# data reference : R. A. Fisher (1936). "The use of multiple measurements in taxonomic problems"

from distance_builder import *
from distance import *
from sklearn import manifold
import matplotlib.pyplot as plt
import math

import numpy as np

if __name__ == '__main__':
    builder = DistanceBuilder()
    builder.load_points(r'../data/data_others/aggregation.txt')  # Step 1
    load = 1   # This variable R modifies grid size
    limit = 20  # Density variable for cutoff or screening ratio <APLHA>
    xdata = builder.vectors[:, 0]
    ydata = builder.vectors[:, 1]
    grouping = []
    ydata_max = int(np.max(ydata)) + 1
    xdata_max = int(np.max(xdata)) + 1
    ydata_min = int(np.min(ydata)) + 1
    xdata_min = int(np.min(xdata)) + 1
    n = 5  # Value greater than i (i=2)
    print xdata_min
    print ydata_min
    print xdata_max
    print ydata_max

    load = int(load*(math.sqrt(((xdata_max-xdata_min) *
                                (ydata_max-ydata_min))/(n*n))))  # Step 2
    print load

    xdata_max += load
    ydata_max += load  # Buffering for visualisation

    set = (xdata_max)*(ydata_max)/(load*load)
    count = [0]*set

    for element in range(len(xdata)):  # Step 3
       # print element
        group = 0
        group += int(xdata[element]/load)
        group += int((ydata[element]/load))*(xdata_max/load)
        # print group
        grouping.append(group)
        count[group] += 1
    print count
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
        if (count[grouping[_]] < limit):  # Step 4
            xdata[_] = 0
            ydata[_] = 0

    plt.plot(xdata, ydata, linestyle='', marker='.', color='b')
    plt.show()

    finalvectors = np.dstack((xdata, ydata))
    finalvectors = finalvectors[0]
    # finalvectors = finalvectors[finalvectors != [0, 0]]
    # finalvectors = np.delete(finalvectors, [0, 0], 0)
    # print finalvectors
    # print (builder.vectors)
    builder.load_vectors(finalvectors)
    builder.build_distance_file_for_cluster(
        SqrtDistance(), r'../data/data_others/output_distance.dat')  # Step 5
    # 788
