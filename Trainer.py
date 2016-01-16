# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 13:19:28 2016

@author: mohit
"""

#f = open("/home/mohit/Documents/bingHackathon/bingHackathon/BingHackathonTrainingData.txt")


data=np.loadtxt("/home/mohit/Documents/bingHackathon/bingHackathon/BingHackathonTrainingData.txt",delimiter='\t',dtype=str)
data=data[:,:6]
clf.fit(data[:,1:], categories)