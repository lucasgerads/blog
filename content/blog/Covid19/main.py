# -*- coding: utf-8 -*-

import requests, csv
from io import StringIO
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import numpy as np
import math as m



csv_url1='https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y/export?format=csv&gid=0'
csv_url2='https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y/export?format=csv&gid=1537942838'

res1 = requests.get(url=csv_url1)
res2 = requests.get(url=csv_url2)


f = StringIO(res1.content.decode("utf-8"))
reader = csv.reader(f, delimiter=',')

next(reader)    # skip header
data = []
for row in reader:
    print(row)
    date_time = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
    cases = int(row[1])
    cases_city = int(row[2])
    deaths = int(row[3])
    data.append([date_time,cases,cases_city,deaths] )

print(data)




# date: "2020-03-27T22:40:32.169Z"
date = datetime.now()
dateFormatted = date.strftime("%Y-%m-%dT%H:%M:%S.000Z")
print(dateFormatted)

header = "--- \n title: Covid19 in Aachen (Stadt und Städteregion) \n date: \"" +  dateFormatted + "\" \n--- " 

introduction = "The city of Aachen publishes (more or less) daily updates about Covid19. It's in the form of a daily press release, so I decided to collect this data to make it more usable for further processing." 


plotPic = "Below is development of cases in the Städteregion Aachen and the city of Aachen\n"
plotPic = plotPic + "![Cases of Covid19](cases.png)" 
plotPic = plotPic + "and the current death toll\n"
plotPic = plotPic + "![Deaths from Covid19](deaths.png)" 


tableHeader = "| Date       	| Cases (Städteregion) 	| Cases (Stadt Aachen) 	| Death Toll (Städteregion) |\n"
tableHeader = tableHeader + "|-------------------	|---------------------	|----------------------	|--------------------------	| "

tableContent = ""

for row in data:
    tableContent = tableContent + "|" + row[0].strftime('%b %d, 2020') + "|" + str(row[1]) + "|"+ str(row[2]) + "|"+ str(row[3]) + "|\n"


source = "Source: [Stadt Aachen](http://www.aachen.de/DE/stadt_buerger/notfall_informationen/corona/aktuelles/pressemitteilungen/index.html)"

d = np.array(data)

print(d)

x = d[:,0]
cases = d[:,1]
cases_aachen =  d[:,2]

deaths = d[:,3]


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(x, cases)
plt.plot(x, cases_aachen)
plt.gcf().autofmt_xdate()
plt.ylabel('Cases')
plt.savefig('cases.png')

plt.clf()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(x, deaths)
plt.gcf().autofmt_xdate()
plt.ylabel('death toll')
plt.savefig('deaths.png')

plt.clf()

f2 = StringIO(res2.content.decode("utf-8"))
reader = csv.reader(f2, delimiter=',')

next(reader)    # skip header
data = []
for row in reader:
    date_time = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
    year = int(row[1])
    gender = row[2]
    data.append([date_time,year, gender] )


d2 = np.array(data)


averageYear = np.median(d2[:,1])
print(d2[:,1])

unique, counts = np.unique(d2[:,1], return_counts=True)

print(unique)
print(counts)

plt.bar(unique, counts)
plt.xlabel('Year of Birth', fontsize=12)
plt.yticks(np.arange(0, max(counts) + 1, step=1))
plt.savefig('year.png')


plotPic = plotPic + "and the year of birth of the deceased. Their average (median) year of birth was " + str(m.floor(averageYear)) + ". Which corresponds to an average age of " + str(2020 - m.floor(averageYear)) + ".\n" 
plotPic = plotPic + "![Year of Birth](year.png)" 



googleurl = "I keep the data in a google [spread sheet](https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y)"

text = header + "\n" + introduction + "\n\n" + plotPic + "\n\n" + googleurl  +  "\n\n\n" + source
print(text)


file = open("index.md", "w") 
file.write(text) 
file.close() 

