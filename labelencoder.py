#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:53:36 2019

@author: manpreetsaluja
"""

from sklearn.preprocessing import LabelEncoder

labelencoder=LabelEncoder()
input=['b','a','c','e','d']
labelencoder.fit(input)

for i,item in enumerate(labelencoder.classes_):
    print(item,'-->',i)