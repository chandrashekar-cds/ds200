# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:28:27 2019

@author: Chandrashekar
"""

#scatter plot
import pandas as pd
#Reading data frm the automobile #data sets using pandas read method

import matplotlib.pyplot as plt
df = pd.read_csv('sbm_blockwise_selected_districts.csv')
df.head()
block = df['DistrictName'] #fetching blockname values r
ihhl = df['IHHLTotal'] #fetching number of Individual household latrines for each block
plt.scatter(block, ihhl, edgecolors='r')
plt.xlabel('DistrictName')
plt.ylabel('number')
plt.title('number of Individual household latrines for each block for the district')
plt.show()

#box plot
df = pd.read_csv('sbm_blockwise_selected_districts.csv')

slice = df.iloc[:,[0, 3]]
blockid = df['BlockID']
#gives individual boxplot with all step names
bp = slice.boxplot(by='DistrictName')
#axes = plt.gca()
#axes.set_ylim([0,800])
plt.show()

#bar plot
df = pd.read_csv('sbm_blockwise_belagavi.csv')
df.set_index('BlockID')[['IHHLTotal']].plot.bar()

plt.title('number of Individual household latrines for each block for the district Belagavi')
plt.ylabel('Number of latrines')
plt.show()