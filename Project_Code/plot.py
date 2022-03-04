#! /usr/bin/env python3
import pandas
import matplotlib.pyplot as plt
import numpy as np

weatherdata = pandas.read_csv('test.csv')

plt.plot(weatherdata.TEMP, weatherdata.CURRENT_TIME)


plt.show()
##print(weatherdata)

