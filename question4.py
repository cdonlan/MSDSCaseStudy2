

import pandas as pd
import numpy as np
import operator as op
import datetime

# part 1
pd.set_option('display.width',3)

temp = pd.read_csv('TEMP.csv')
print(temp)
temp.info()
temp.max(axis=1)
temp["Monthly AverageTemp"]

pd.set_option('display.width',5)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 1000)



tempgrouped = temp.groupby('Country')

temp['Date'] = pd.to_datetime(temp['Date'])
monthly_average = tempgrouped["Monthly AverageTemp"].agg({'Max':np.max,'Min':np.min})
monthly_average['Difference'] = monthly_average['max'] - monthly_average['min']

# part 2
# united states
UStemp = temp.loc[(temp.Country == "United States")]
UStemp['Date'] = pd.to_datetime(UStemp['Date'])
date_object = datetime.datetime(1900,1,1)
UStemp = UStemp.loc[(UStemp.Date >= date_object)]
UStemp['Monthly AverageTemp F'] = ( UStemp['Monthly AverageTemp'] * 1.8) + 32

UStemp["Year"] = UStemp['Date'].dt.year
UStempgrouped = UStemp.groupby("Year")
UStemp_yearly_avg = UStempgrouped.agg(np.average)

twoyearave = []
for index, row in UStemp_yearly_avg.iterrows():
    if index+1 not in UStemp_yearly_avg.index:
        break
    yearplus = index + 1
    years = "%s-%s" % (index,yearplus)
    thisyear = row["Monthly AverageTemp F"]
    nextyear = UStemp_yearly_avg.loc[yearplus]["Monthly AverageTemp F"]
    diff = thisyear - nextyear
    twoyearave.append((years,format(diff,'.4f'))
    

city = pd.read_csv('CityTemp.csv')
city['Date'] = pd.to_datetime(city['Date'])
city = city.loc[(city.Date >= datetime.datetime(1900,1,1))]
city_grouped = city.groupby('City')
city_grouped_difference = city_grouped["Monthly AverageTemp"].agg({'Max':np.max,'Min':np.min})
city_grouped_difference['Difference'] = city_grouped_difference['Max'] - city_grouped_difference['Min']
