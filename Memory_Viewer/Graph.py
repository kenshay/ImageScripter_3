import matplotlib
import matplotlib.pyplot as plt
import time
from datetime import datetime
import matplotlib.dates as mdates
import numpy as np

x = []
y = [0,10,20,30,40,50,60,70,80,90,100]
script_x = []
script_y = []

for i in range(11):
    num = datetime.now()
    print(type(num))
    time.sleep(1)
    #num = matplotlib.dates.epoch2num(time.time())
    x.append(num)

for i in range(len(x)):
    script_x.append(i)
    script_y.append(0)
    print(i)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )


fig = plt.figure()
ax = fig.add_subplot(1,1,1)
plt.plot(x, y,color='r')
plt.plot(x,script_y,color='b')
#ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))   #to get a tick every 15 minutes
#ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))     #optional formatting
ax.xaxis.set_major_locator(mdates.SecondLocator(interval=1))   #to get a tick every 15 minutes
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))     #optional formatting


#fig_scripts = plt.figure()
#fig_scripts.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')





#print(x)
plt.yticks(np.arange(min(y), max(y)+1, 10.0))
plt.show()



'''
[datetime.datetime(2019, 1, 4, 9, 44, 58, 229000),
 datetime.datetime(2019, 1, 4, 9, 45, 8, 229000),
 datetime.datetime(2019, 1, 4, 9, 45, 18, 230000),
 datetime.datetime(2019, 1, 4, 9, 45, 28, 231000),
 datetime.datetime(2019, 1, 4, 9, 45, 38, 232000),
 datetime.datetime(2019, 1, 4, 9, 45, 48, 233000),
 datetime.datetime(2019, 1, 4, 9, 45, 58, 233000),
 datetime.datetime(2019, 1, 4, 9, 46, 8, 233000),
 datetime.datetime(2019, 1, 4, 9, 46, 18, 234000),
 datetime.datetime(2019, 1, 4, 9, 46, 28, 235000),
 datetime.datetime(2019, 1, 4, 9, 46, 38, 235000)]
'''


