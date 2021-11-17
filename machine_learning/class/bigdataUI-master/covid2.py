import matplotlib.pyplot as plt
import datetime as dt
import operator
import csv
with open('owid-covid-data1.csv', 'rt') as f: 
  filtereddata = [row for row in csv.reader(f)] 

sorteddata = sorted(filtereddata, key=operator.itemgetter(1))

KORcase = [row for row in sorteddata if row[0] == "KOR"]
CHNcase = [row for row in sorteddata if row[0] == "CHN"]
JAPcase = [row for row in sorteddata if row[0] == "JPN"]
RUScase = [row for row in sorteddata if row[0] == "RUS"]

k_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in KORcase] 
k_y = [row[3] for row in KORcase] 

c_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in CHNcase] 
c_y = [row[3] for row in CHNcase] 

j_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in JAPcase] 
j_y = [row[3] for row in JAPcase]

r_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in RUScase] 
r_y = [row[3] for row in RUScase]

plt.plot(k_x,k_y, color='red')
plt.plot(c_x,c_y, color='orange') 
plt.plot(j_x,j_y, color='blue')
plt.plot(r_x,r_y, color='green')
plt.show()
