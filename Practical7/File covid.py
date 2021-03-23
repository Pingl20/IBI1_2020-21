import os
from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("C:\\Users\\Teresa Lu\\Desktop")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:10:2, :])

afgnst_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "Afghanistan":
        afgnst_booleans.append(True)
    else:
        afgnst_booleans.append(False)
afghanistan_total_cases = covid_data.loc[afgnst_booleans, "total_cases"]
print(afghanistan_total_cases)

print(np.median(world_new_cases))
print(np.nanmean(world_new_cases))

world_new_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "World":
        world_new_booleans.append(True)
    else:
        world_new_booleans.append(False)
world_new_cases = covid_data.loc[world_new_booleans, "new_cases"]
print(world_new_cases)

world_date_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "World":
        world_date_booleans.append(True)
    else:
        world_date_booleans.append(False)
world_date = covid_data.loc[world_date_booleans, "date"]
print(world_date)


score = world_new_cases
plt.boxplot(score,
            vert=True,
            showbox=True,
            meanline=True,
            showcaps=True,
            showfliers=True)
plt.show()

china_new_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "China":
        china_new_booleans.append(True)
    else:
        china_new_booleans.append(False)
china_new_cases = covid_data.loc[china_new_booleans, "new_cases"]
print(china_new_cases)


uk_new_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "United Kingdom":
        uk_new_booleans.append(True)
    else:
        uk_new_booleans.append(False)
uk_new_cases = covid_data.loc[uk_new_booleans, "new_cases"]
print(uk_new_cases)

plt.plot(world_date, china_new_cases, "bo")
plt.plot(world_date, uk_new_cases, "ro")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation = -90)

world_new_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "World":
        world_new_booleans.append(True)
    else:
        world_new_booleans.append(False)
world_new_deaths = covid_data.loc[world_new_booleans, "new_deaths"]
print(world_new_deaths)

plt.plot(world_date, world_new_cases, "b+")
plt.plot(world_date, world_new_deaths, "r+")
plt.xticks(world_date.iloc[0:len(world_date):4],rotation = -90)


andorra_new_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "Andorra":
        andorra_new_booleans.append(True)
    else:
        andorra_new_booleans.append(False)
andorra_new_cases = covid_data.loc[andorra_new_booleans, "new_cases"]


andorra_total_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "Andorra":
        andorra_total_booleans.append(True)
    else:
        andorra_total_booleans.append(False)
andorra_total_cases = covid_data.loc[andorra_total_booleans, "total_cases"]

andorra_date_booleans = []
for row in covid_data.iloc[0:, 1]:
    if row == "Andorra":
        andorra_date_booleans.append(True)
    else:
        andorra_date_booleans.append(False)
andorra_date = covid_data.loc[andorra_date_booleans, "date"]

plt.plot(andorra_date, andorra_total_cases, "bo")
plt.plot(andorra_date, andorra_new_cases, "ro")
plt.xticks(andorra_date.iloc[0:len(andorra_date):1],rotation=-90)