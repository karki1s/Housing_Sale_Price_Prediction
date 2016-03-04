##########################################################
# Author: Suman Karki
# This program will take the output file from the FilterData.py and
# Analyse the datasets , plot the graphs and create the linear regression model
#####################################################

#some of the module needed to do the job
# sklearn for generating the model from out dataset
# numpy for  converting our list to array  for our model and graphs
# matplotlib for ploting the various graphs

from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
import pprint

def make_graph_szp(splst,estlst,predlst):
        sold_price = plt.plot(splst,'o',label = 'Sold Price')
        zestimate = plt.plot(estlst,'o',label = 'Zestimate')
        prediction = plt.plot(predlst,'o',label = 'prediction')
        legend = plt.legend(loc = 'upper left')
        lx = plt.xlabel('Houses')
        ly = plt.ylabel('Amount')
        ltitle = plt.title(" Sold Price, Zestimate, and Prediction")
        plt.savefig("make_graph_szp",ext='png',close=True)
        plt.show()

def make_graph_for_try_a(splst,estlst,predlst):
        print splst
        print np.shape(splst)
        print len(splst)
        print type(splst)
        x = np.array(range(1,len(splst)+1))
        print np.shape(x)
        a = plt.plot(x,splst,'o')
        b = plt.plot(x,estlst,'o')
        c = plt.plot(x,predlst,'o')
        plt.show()
        print x

def make_graph_for_try_b(splst,estlst,predlst):
        lists=[]
        for i in range(0,len(splst)):
               lists.append([splst[i],estlst[i],predlst[i]])
        print lists
        x = 0;
        for d in range(1,len(splst)):
                plt.plot(lists[0],lists[1],lists[2],'o')
        plt.show()
        print 'done'



def make_graph_sp(splst,predlst):
        plt.scatter(splst,predlst,c ='orange',marker='o')
        plt.xlabel('Sold Price')
        plt.ylabel('Prediction')
        plt.title('Sold Price Vs Prediction')
        plt.savefig("make_graph_sp",ext='png',close=True)
        plt.show()


#open the reg.txt file which is created after we run the
#FilterData.py. reg.txt file has all the data we need to create the model
try:
        data_file = open('reg.txt')
        lines = data_file.readlines()
        data_file.close()
except:
        print 'Error: couldnot open the file'
        exit()

# Here for the convenient we will change relabel our attribute
# For our dependent we will call y and for our
# independent attributes we will call x1, x2....x5 and the zest is the Zillow.com estimate
zest = []
y = []
x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

# we will not include the header
cr=0
for line in lines:
        if cr ==0:
                cr+=1
        else:
                line = line.replace("\n",' ')
                vals = line.split(",")
                zest.append(float(vals[0]))
                y.append(float(vals[1]))
                x1.append(float(vals[2]))
                x2.append(float(vals[3]))
                x3.append(float(vals[4]))
                x4.append(float(vals[5]))
                x5.append(float(vals[6]))
                cr+=1
print 'Number of records : ', cr-1

#converting all the attribute to numpy.dnarray
zest = np.array(zest)
y = np.array(y)
x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
x4 = np.array(x4)
x5 = np.array(x5)

# We have all the data now we will built regression model using the sklearn
#ones = np.ones(x1.shape)
#print ones
#np.vstack will take all the attribute combine all x1,x2,......x2 vertically and transpose
#which is great each row will be the record

X = np.vstack([x1,x2,x3,x4,x5]).T
regr = linear_model.LinearRegression()
handle = regr.fit(X,y)
print handle.coef_
print handle.intercept_
#result = regr.decision_function(X)
#make_graph_szp(y,zest,result)
#print(type(result))
#print result
#make_graph_sp(y,result)
#make_graph_for_try_a(y,zest,result)
#make_graph_for_try_b(y,zest,result)

file_handle = open('reg.txt','r')
lines = file_handle.readlines()
file_handle.close()
lst = []
count = 0
z_estmate =[]
s_oldprice =[]
p_value =[]
for line in lines:
   if count ==0:
      count+=1
   else:
      alist =[]
      alist = line.strip('\n').split(',')
      alist = [float(i) for i in alist]
      print alist
      z_estmate.append(alist.pop(0))
      s_oldprice.append(alist.pop(0))
      p_value.append(handle.predict(alist))
      print alist
      count+=1

print 'Zestmate Sold Price Predicted value'
print '*'*20
file_out = open('result_out','w')
file_out.write('Zestmate, Sold Price, Predicted Value')
file_out.write('\n')
for i in range(0,len(z_estmate)):
       print z_estmate[i],',',s_oldprice[i],' , ', p_value[i]
       alist = [z_estmate[i],s_oldprice[i], p_value[i]]
       print 'printing a list..............'
       print alist
       file_out.write((','.join(str(i) for i in alist)))
       file_out.write('\n')


make_graph_szp(s_oldprice,z_estmate,p_value)
print 'Sold Price: ',sum(s_oldprice )
print 'Zestmate Price: ',sum(z_estmate)
print 'Predicted Value: ',sum(p_value)
print 'Absolute value of Sold Price-Zestmate Price: ',abs(sum(s_oldprice )-sum(z_estmate))
print 'Absolute value of Sold Price-Predicted Value:' ,abs(sum(s_oldprice)-sum(p_value))
coefficent = handle.coef_
intercept = handle.intercept_
print coefficent
print intercept
equation = 'House Price (Y) = '+str(intercept) + '+('+str(coefficent[0]) +'age) + (' +str(coefficent[1])+'beds) + ('+str(coefficent[2])+'baths) + ('+str(coefficent[3])+'housesize) + ('+str(coefficent[4])+'lotsize)'
print equation
file_out.write(equation)
file_out.close()
regr = RandomForestRegressor()
regr.fit(X,y)
print regr.predict(X)
