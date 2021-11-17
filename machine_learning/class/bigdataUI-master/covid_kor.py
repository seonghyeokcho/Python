import matplotlib.pyplot as plt
import datetime as dt
import operator
import csv
with open('owid-covid-data1.csv', 'rt') as f: 
  filtereddata = [row for row in csv.reader(f)] 

sorteddata = sorted(filtereddata, key=operator.itemgetter(1))

KOR = [row for row in sorteddata if row[0] == "KOR"]

c_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in KOR] 
c_y = [row[3] for row in KOR] 

nc_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in KOR] 
nc_y = [row[4] for row in KOR] 

d_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in KOR] 
d_y = [row[5] for row in KOR]

nd_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in KOR] 
nd_y = [row[6] for row in KOR]

plt.plot(c_x,c_y, color='blue')
plt.plot(nc_x,nc_y, color='skyblue')
plt.plot(d_x,d_y, color='red')
plt.plot(nd_x,nd_y, color='hotpink')

plt.show()