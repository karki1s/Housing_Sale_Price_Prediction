#########################################################
# Author: Suman Karki
# Reads the file called raw_data.csv and cleans and does the missing value
# mutation, unit conversion and generate the out put as clean file.
# changes
#########################################################

import csv
import pprint
import matplotlib.pyplot as plt

'''
It will take the list  and if the value is missing it will put the 0 and
later it is taken care when doing the data mutation
'''
def get_data(row_num):
    lst = []
    for i in all_record:
        if i [row_num]==' ':
            lst.append(0)
        else:
            lst.append(i[row_num])
    print lst
    return lst

'''
Takes value as list and goes through each value and delete the unnessary
information.
'''
def process_further(data):
    lst = []
    for i in data:
        if type(i)==int:
            lst.append(i)
        else:
            a = i.split(' ')
            if(len(a)>=2):
                lst.append(a[0])
            else:
                lst.append(i)
    return lst

'''
Takes the sold on data list and built date list and return the list of age of
the house when sold.
'''
def get_age_when_sold(sold_on,built):
    lst = []
    if len(sold_on)==len(built):
        for i in range(0,len(sold_on)):
            if sold_on[i] == ' ' or int(built[i])==0:
                lst.append(0)
            else:
                lst.append(float( '20'+(sold_on[i])[-2:])-float(built[i]))
    else:
        print "Error: Not Possible to compute"
    return lst

'''
It will take the list and calculate the average and does the missing
value mutation
'''
def data_mut_w_mean(data_lst):
    lst =[]
    c=data_lst.count(0)
    mut = sum(data_lst)/(len(data_lst)-c)
    for i in data_lst:
        if i ==0:
            lst.append(mut)
        else:
            lst.append(i)
    return lst

'''
Takes the string contented list and convert the int float content list.
'''
def change_strlst_intlst(strlst):
    lst =[]
    for i in strlst:
        try:
            lst.append(float(i))
        except:
            lst.append(0)
    return lst

'''
Takes the list of data which are in acer and convert to the sqft
'''
def convert_to_sqft(data_lst):
    lst = []
    for i in data_lst:
        if (i < 100):
            lst.append(i*43560)
        else:
            lst.append(i)
    return lst

'''
Some of the lot_size are smaller than area of house if that the case
it will make lot_size as area of house of house plus lot_size.
Need to make sure they do that.....
'''
def get_right_lot_size(area_of_house,lot_size):
    lst = []
    if len(area_of_house) == len(lot_size):
        for i in range(0,len(area_of_house)):
            if(area_of_house[i]>=lot_size[i]):
                lst.append(area_of_house[i]+lot_size[i])
            else:
                lst.append(lot_size[i])
    else:
        print " Error: size does not match"
    return lst

'''
Takes the integer content list and convert it to string content list
'''
def convert_intlst_to_strlst(data_lst):
    lst = []
    for i in data_lst:
        lst.append(str(i))
    return lst

'''
Save_in_file will take the attributes and write the information in the
file called reg.txt
'''
def save_in_file(x1,x2,x3,x4,x5,x6,x7):
    fileout = open('reg.txt','w')
    fileout.write(str('zest, soldprice, age, bedroom, bathroom,housesize, lotsize'))
    fileout.write('\n')
    for i in range(0,len(x1)):
        lst = [str(x1[i]),str(x2[i]),str(x3[i]),str(x4[i]),str(x5[i]),str(x6[i]),str(x7[i])]
        fileout.write(', '.join(lst))
        fileout.write('\n')
    fileout.close()


def make_graph_a(attr,name='Label'):
        grap = plt.plot(attr,'o',color='red')
        lx = plt.xlabel('Houses')
        ly = plt.ylabel(name)
        ltitle = plt.title(" House and "+name)
        plt.savefig(name,ext='png',close=True)
        plt.show()

def make_graph_b(attr,name='Label'):
        x = [i for i in range(0,len(attr))]
        grap = plt.bar(x,attr,1,color = 'green')
        lx = plt.xlabel('Houses')
        ly = plt.ylabel(name)
        ltitle = plt.title(" House and "+name)
        plt.savefig(name,ext='png',close=True)
        plt.show()

def make_graph_beds_baths(beds,baths):
    x = [i for i in range(0,len(beds))]
    plt.subplot(1,2,1)
    plt.plot(x,beds,'ro')
    plt.xlabel('house')
    plt.ylabel('bedroom')
    plt.title('House and Bedroom')
    plt.subplot(1,2,2)
    plt.plot(x,baths,'g*')
    plt.xlabel('house')
    plt.ylabel('bathroom')
    plt.title('House and Bathroom')
    plt.show()

all_record=[]
file = open('raw_data.csv','r')
reader = csv.reader(file)
print (reader)
row_num=0
record_w_missing=0
for row in reader:
    if row_num==0:
        header = row
    row = row[1:]
    print row
    missing_value=0
    for r in row:
        if r in [' ','']:
            missing_value+=1
    if missing_value<=2 and len(row)==9:
        record_w_missing+=1
        all_record.append(row)
    row_num+=1
file.close()
print(header)



sold_on = []
sold_price =[]
zestimate =[]
bedrooms =[]
bathrooms = []
area_of_house = []
lot_size = []
built = []
age_when_sold = []

sold_on = process_further(get_data(0))
sold_price = process_further(get_data(1))
zestimate = process_further(get_data(2))
bedrooms = process_further(get_data(3))
bathrooms = process_further(get_data(4))
area_of_house = process_further(get_data(5))
lot_size = process_further(get_data(6))
built = process_further(get_data(7))

age_when_sold =  data_mut_w_mean(change_strlst_intlst(get_age_when_sold(sold_on,built)))
bathrooms = data_mut_w_mean(change_strlst_intlst(bathrooms))
bedrooms = data_mut_w_mean(change_strlst_intlst(bedrooms))
area_of_house = data_mut_w_mean(change_strlst_intlst(area_of_house))
sold_price = data_mut_w_mean(change_strlst_intlst(sold_price))
zestimate = data_mut_w_mean(change_strlst_intlst(zestimate))
lot_size = get_right_lot_size(data_mut_w_mean(convert_to_sqft(change_strlst_intlst(lot_size))),area_of_house)
print len(age_when_sold),len(sold_price),len(area_of_house),len(lot_size),len(zestimate)
print '*'*30
print 'zestimate:'
print zestimate
print '*'*30
print 'sold_price:'
print sold_price
print '*'*30
print 'age_when_sold:'
print age_when_sold
print '*'*30
print 'bedrooms:'
print bedrooms
print '*'*30
print 'bathrooms:'
print bathrooms
print '*'*30
print 'area_of_house:'
print area_of_house
print '*'*30
print 'lot_size:'
print lot_size
print '*'*30
make_graph_b(zestimate,'zest')
make_graph_b(sold_price,'soldprice')
make_graph_b(age_when_sold,'age')
make_graph_a(bedrooms,'bedroom')
make_graph_a(bathrooms,'bathroom')
make_graph_b(area_of_house,'housesize')
make_graph_b(lot_size,'lotsize')
save_in_file(zestimate,sold_price,age_when_sold,bedrooms,bathrooms,area_of_house,lot_size)
make_graph_beds_baths(bedrooms,bathrooms)
print 'done'
