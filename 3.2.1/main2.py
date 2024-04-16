# a321_temps_analysis.py
# This program uses the pandas module to load a 2-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot a graph and a bar chart
import matplotlib.pyplot as plt
import pandas as pd

# Load in the data with read_csv()
# TODO #1: change the file name to your data file name
co2_data = pd.read_csv("co2_data.csv", header=0)   # identify the header row

# TODO #2: Use matplotlib to make a line graph
plt.plot(co2_data['decimal_year'], co2_data['Average'], color='gray')
plt.ylabel('Average value')
plt.xlabel('decimal_year')
plt.title('Change in Temperatures')

# TODO #3: Plot LOWESS in a line graph
# plt.plot(co2_data['decimal_year'], co2_data['#Days'], color='blue')
plt.show()

# TODO #4: Use matplotlib to make a bar chart
plt.bar(co2_data['decimal_year'], co2_data['Average'], align='center', color='green')
plt.ylabel('Average value')
plt.xlabel('decimal_year')
plt.title('Change in Temperatures')
plt.show()

# TODO #5: Calculate min, max, and avg anomaly and the corresponding min/max years
min_average = co2_data['Average'][0]
max_average = co2_data['Average'][0]
min_year = co2_data['decimal_year'][0]
max_year = co2_data['decimal_year'][0]
sum_average = 0
avg_average = 0
# find the min, max and calculate the sum
for i in range(len(co2_data['Average'])):
    if (co2_data['Average'][i] < min_average):
        min_anomaly = co2_data['Average'][i]
        min_year = co2_data['decimal_year'][i]
    if (co2_data['Average'][i] > max_average):
        max_anomaly = co2_data['Average'][i]
        max_year = co2_data['decimal_year'][i]
    sum_average += co2_data['Average'][i]
# calculate average
avg_anomaly = sum_average/len(co2_data['Average'])
# print the statistical values
print("The maximum average is:", max_average, "which occured in", max_year)
print("The minimum average is:", min_average, "which occured in", min_year)
print("The average average is:", avg_average)