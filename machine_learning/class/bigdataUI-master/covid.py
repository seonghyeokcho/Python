import matplotlib.pyplot as plt
import datetime as dt
import operator
import csv
with open('owid-covid-data1.csv', 'rt') as f: 
  filtereddata = [row for row in csv.reader(f)] 

sorteddata = sorted(filtereddata, key=operator.itemgetter(1))

KORdeath = [row for row in sorteddata if row[0] == "KOR"]
CHNdeath = [row for row in sorteddata if row[0] == "CHN"]
JAPdeath = [row for row in sorteddata if row[0] == "JPN"]
RUSdeath = [row for row in sorteddata if row[0] == "RUS"]

k_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in KORdeath] 
k_y = [row[5] for row in KORdeath] 

c_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for 
       row in CHNdeath] 
c_y = [row[5] for row in CHNdeath] 

j_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in JAPdeath] 
j_y = [row[5] for row in JAPdeath]

r_x = [dt.datetime.strptime(row[2], '%Y.%m.%d').date() for
       row in RUSdeath] 
r_y = [row[5] for row in RUSdeath]

plt.plot(k_x,k_y, color='red')
plt.plot(c_x,c_y, color='orange') 
plt.plot(j_x,j_y, color='blue')
plt.plot(r_x,r_y, color='green')
plt.show()
