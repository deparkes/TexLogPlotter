# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:19:11 2015

@author: Duncan Parkes

Requirements:
- matplotlib
- pandas
- Output from texlog

Todo: 
- Make into a more robust commandline interface e.g. with argparser and options
for outputs

Thesis data plotter
"""

import matplotlib.pyplot as plt
from matplotlib.dates import strpdate2num
import os
import pandas as pd
from datetime import datetime

plt.rcdefaults()


plt.style.use('ggplot')
plt.style.use('bmh')

LoggingDir = "C:\\Users\\ppxdep\\Documents\\Work\\thesis\\Logging"

os.chdir(LoggingDir)

def bytedate2num(fmt):
    def converter(b):
        return strpdate2num(fmt)(b.decode('ascii'))
    return converter

date_converter = bytedate2num("%Y-%m-%d %H:%M")

#fig = plt.figure()
#
#ax1 = fig.add_subplot(1,1,1, axisbg="white")
legend_entries = []


figure1 = plt.figure(1,figsize=(4, 3), dpi=100) 
figure2 = plt.figure(2,figsize=(4, 3), dpi=100)

#ax1 = figure1.add_subplot(111) 
#ax2 = figure2.add_subplot(111)

for root, dirs, files in os.walk(LoggingDir):
    for logfile in files:
        if logfile.endswith('.txt') and not logfile.endswith('matter.txt'):

            with open(logfile,"rb") as f:
                  data = pd.read_csv(f)
                  data.Date = data.Date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d %H:%M"))
                  data.index = data.Date
                  legend_entries.append(logfile)
                  print logfile
                  data
                      
#                date[i], words[i] = data[1]
                
            if not "Total" in logfile:
                plt.figure(2)
                ax2 = figure2.add_axes(data.icol(3).plot(linewidth=1))
                
            else:
                plt.figure(1)
                ax1 = figure1.add_axes(data.icol(2).plot(linewidth=1))
                      

#t1 = np.arange(0.0, 5.0, 0.1)
#t2 = np.arange(0.0, 5.0, 0.02)
#
#
#
#plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#
#plt.subplot(212)
#plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()

ax1.set_title("Total Words")
#ax.xaxis.set_major_locator(DayLocator(1))
ax1.set_ylabel("Words")

ax2.set_title("Thesis Words")
#ax.xaxis.set_major_locator(DayLocator(1))
ax2.legend(legend_entries,loc=2,bbox_to_anchor=(1, 1.04))
ax2.set_ylabel("Words")

#plt.show()

save_image_as = "thesis_plot.png"

figure2.set_size_inches(4,3)
figure2.savefig(save_image_as,dpi=600,bbox_inches='tight')

save_image_as = "total_words.png"

figure1.set_size_inches(4,3)
figure1.savefig(save_image_as,dpi=600,bbox_inches='tight')