#! /usr/bin/env python
# Time-stamp: <2021-03-25 13:42:24 christophe@pallier.org>

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

L=sys.argv[1:]
data = pd.concat(pd.read_csv(exp, comment='#', na_values='None') for exp in L)
#print(sys.argv[1:])


L=['red','blue','random']
for col in L:
	print(data[data.block==col])
	print( col + "block" ,data[data.block==col].describe() )
	

fig = plt.figure()

ax1 = fig.add_subplot(131)
ax1.stem(data.time)
ax1.title.set_text('RT ~ Trial')

ax2 = fig.add_subplot(132)
ax2.boxplot(data.time[~np.isnan(data.time)])
ax2.title.set_text('Distrib. of RT')


#ax3 = fig.add_subplot(133)
#ax3.scatter(data.wait, data.time)
#ax3.title.set_text('RT ~ Wait time')

plt.show()
