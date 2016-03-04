#########################################################
# Author: Suman Karki
########################################################

import numpy as np
import matplotlib.pyplot as plt

def make_graph_beds_baths(bedroom,bathroom,age,housesize,soldprice):
    x = [i for i in range(0,len(bedroom))]
    plt.figure(1,figsize=(13,6),facecolor='w',edgecolor='b')
    plt.subplot(231)
    plt.bar(x,bedroom,color='red',edgecolor='red')
    plt.xlabel('house')
    plt.ylabel('bedroom')
    plt.title('House and Bedroom')
    plt.subplot(232)
    plt.bar(x,bathroom,color='green',edgecolor='green')
    plt.xlabel('house')
    plt.ylabel('bathroom')
    plt.title('House and Bathroom')
    plt.subplot(233)
    plt.bar(x,age,color='blue',edgecolor ='blue')
    plt.xlabel('house')
    plt.ylabel('age')
    plt.title('House and Age')
    plt.subplot(234)
    plt.bar(x,housesize,color='red',edgecolor ='red')
    plt.xlabel('house')
    plt.ylabel('housesize x 1000')
    plt.title('House and House Size')
    plt.subplot(235)
    plt.bar(x,lotsize,color='green',edgecolor ='green')
    plt.xlabel('house')
    plt.ylabel('lotsize x 10000')
    plt.title('House and Lot Size')
    plt.subplot(236)
    plt.bar(x,soldprice,color='blue',edgecolor='blue')
    plt.xlabel('house')
    plt.ylabel('soldprice x 10000')
    plt.title('House and Sold Price')
    plt.tight_layout()
    plt.show()


#open the reg.txt file which is created after we run the
#FilterData.py. reg.txt file has all the data we need to create the model
try:
        datafile = open('reg.txt')
        lines = datafile.readlines()
        datafile.close()
except:
        print 'Error: couldnot open the file'
        exit()

zest,soldprice,age,bedroom,bathroom,housesize,lotsize = [],[],[],[],[],[],[]
cr=0
for line in lines:
        if cr ==0:
                cr+=1
        else:
                line = line.replace("\n",' ')
                vals = line.split(",")
                zest.append(float(vals[0]))
                soldprice.append(float(vals[1])/10000)
                age.append(float(vals[2]))
                bedroom.append(float(vals[3]))
                bathroom.append(float(vals[4]))
                housesize.append(float(vals[5])/1000)
                lotsize.append(float(vals[6])/10000)
                cr+=1
print 'Number of records : ', cr-1

#converting all the attribute to numpy.dnarray
zest = np.array(zest)
soldprice = np.array(soldprice)
age = np.array(age)
bedroom = np.array(bedroom)
bathroom = np.array(bathroom)
housesize = np.array(housesize)
lotsize = np.array(lotsize)

fig = plt.figure()
ax = fig.add_subplot(111)
#ax.boxplot([zest,soldprice,age,bedroom,bathroom,housesize,lotsize])
ax.boxplot([bedroom,bathroom])
ax.set_xticklabels(['bedroom','bathroom'])
fig.savefig('boxplotbedandbath.png', inches = 'tight')
print "one done"
fig = plt.figure()
ax = fig.add_subplot(111)
#ax.boxplot([zest,soldprice,age,bedroom,bathroom,housesize,lotsize])
ax.boxplot([zest,soldprice])
ax.set_xticklabels(['zest','soldprice'])
plt.show()
make_graph_beds_baths(bedroom,bathroom,age,housesize,soldprice)
