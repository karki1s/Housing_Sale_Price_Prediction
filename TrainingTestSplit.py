###################################
# Author: Suman Karki
# This program will split the file in to test and training sets.
####################################
import random
import io
try:
   file_handler =  open('reg.txt','r')
   lines = file_handler.readlines()
   file_handler.close()
except:
   print 'Error: could not open the file'
   exit()


def write_in_file(name,header,list_to_write):
   print name
   try:
      file_handle = open(name,'w')
      file_handle.write(str(header))
      file_handle.write('\n')
      for record in list_to_write:
         file_handle.write(record)
         file_handle.write('\n')
      file_handle.close()
   except:
      print 'Error: could not open a file to write a list in it'
      exit()



header = [ ]
trainlst =[ ]
testlst = [ ]
count = 0
for line in lines:
   if count ==0:
      header.append(line.strip('\n'))
      count+=1
   else:
      trainlst.append(line.strip('\n'))
      count+=1

for i in range(0,int((20*count)/100)):
   anum = random.randint(0,len(trainlst)-1)
   testlst.append(trainlst.pop(anum))

print '*'*20;
print testlst
print len(testlst)
print '*'*20;
print len(trainlst)
print trainlst
print header
print count
write_in_file('trainlst.txt',header[0],trainlst)
write_in_file('test.txt',header[0],testlst)
print 'done'
