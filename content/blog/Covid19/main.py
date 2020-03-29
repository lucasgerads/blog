# -*- coding: utf-8 -*-

import requests, csv
from io import StringIO
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import numpy as np
import math as m

# pulling data form spreasheet 
csv_url1='https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y/export?format=csv&gid=0'
csv_url2='https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y/export?format=csv&gid=1537942838'

res1 = requests.get(url=csv_url1)
res2 = requests.get(url=csv_url2)

f = StringIO(res1.content.decode("utf-8"))
reader = csv.reader(f, delimiter=',')

next(reader)    # skip header
data = []
for row in reader:
    date_time = datetime.strptime(row[0], '%Y-%m-%dT%H:%M:%S')
    cases = int(row[1])
    cases_city = int(row[2])
    deaths = int(row[3])
    data.append([date_time,cases,cases_city,deaths] )


date = datetime.now()
dateFormatted = date.strftime("%Y-%m-%dT%H:%M:%S.000Z")

header = "--- \n title: Covid19 in Aachen (Stadt und Städteregion) \n date: \"" +  dateFormatted + "\" \n--- " 

introduction = "The city of Aachen publishes (more or less) daily updates about Covid19. It's in the form of a daily press release, so I decided to collect this data to make it more usable for further processing ([google spread sheet](https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y))." 

plotPic = "Below is the development of cases in the Städteregion Aachen and the city of Aachen: \n"
plotPic = plotPic + "![Cases of Covid19](cases.png)" 
plotPic = plotPic + "And the current death toll: \n"
plotPic = plotPic + "![Deaths from Covid19](deaths.png)" 
source = "Source: [Stadt Aachen](http://www.aachen.de/DE/stadt_buerger/notfall_informationen/corona/aktuelles/pressemitteilungen/index.html)"

d = np.array(data)

x = d[:,0]
cases = d[:,1]
cases_aachen =  d[:,2]
deaths = d[:,3]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(x, cases, "-b", label="Städteregion")
plt.plot(x, cases_aachen, "-r", label="Stadt Aachen")
plt.gcf().autofmt_xdate()
plt.legend(loc="upper left")
plt.ylabel('Cases')
plt.savefig('cases.png')
plt.clf()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
plt.plot(x, deaths, "-g")
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

unique, counts = np.unique(d2[:,1], return_counts=True)

plt.bar(unique, counts)
plt.xlabel('Year of Birth', fontsize=12)
plt.yticks(np.arange(0, max(counts) + 1, step=1))
plt.savefig('year.png')
plt.clf()

unique, counts = np.unique(d2[:,2], return_counts=True)
totalDeaths = np.sum(counts)
percentages = np.rint(counts  * 100 / totalDeaths)


plt.bar(unique, counts)
plt.xlabel('Gender', fontsize=12)
plt.yticks(np.arange(0, max(counts) + 3, step=1))
for i, (c, p)  in enumerate(zip(counts, percentages)):
    plt.gca().text(i-0.05, c + 0.5, str(p) + " %", color='black', fontweight='bold')
plt.savefig('gender.png')
plt.clf()

plotPic = plotPic + "And the year of birth of the deceased. Their average (median) year of birth was " + str(m.floor(averageYear)) + ". Which corresponds to an average age of " + str(2020 - m.floor(averageYear)) + ".\n" 
plotPic = plotPic + "![Year of Birth](year.png)" 

plotPic = plotPic + "And the gender distribution of the deceased. " + str(percentages[1]) + " % of victms were male.\n" 
plotPic = plotPic + "![Gender](gender.png)" 

description = "## How this site is generated \n This site is automatically generated when data is added to the [spread sheet](https://docs.google.com/spreadsheets/d/1Th4GSgmTpX4GtcebVDzIfRuCOu2cSOc2WJCORHcCw-Y). You can find the corresponding python script inside my [github repository](https://github.com/lucasgerads/blog/blob/master/content/blog/Covid19/main.py)."

text = header + "\n" + introduction + "\n\n" + plotPic + "\n\n" + description +  "\n\n\n ##Source\n" + source

file = open("index.md", "w") 
file.write(text) 
file.close() 