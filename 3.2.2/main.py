# a322_electricity_trends.py
# This program uses the pandas module to load a 3-dimensional data sheet into a pandas DataFrame object
# Then it will use the matplotlib module to plot comparative line graphs 

import matplotlib.pyplot as plt
import pandas as pd

# choose countries of interest
Africa_countries = ['Egypt','Morocco', 'Sudan', 'Niger', 'Ethiopia', 'South Africa']
Europe_countries = ['Austria', 'Croatia', 'Hungary', 'Romania', 'Slovakia', 'Slovenia']
Asian_countries = ['China', 'Japan', 'Philippines', 'South Korea', 'Thailand', 'South Asia']
American_countries = ['United States', 'Argentina', 'Barbados', 'Brazil', 'Canada', 'Mexico']


# Load in the data with read_csv()
df = pd.read_csv("elec_access_data.csv", header=0)    # header=0 means there is a header in row 0

# get a list unique countries
unique_countries = df['Entity'].unique()

# Plot the data on a line graph
for c in unique_countries:
  if c in Africa_countries:
    
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == c]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == c]['Access']

    plt.plot(years, sum_elec, label=c, linestyle=":")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()



for a in Europe_countries:
  if a in Europe_countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == a]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == a]['Access']

    plt.plot(years, sum_elec, label=a, linestyle="-.")


plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()


for b in unique_countries:
  if b in Asian_countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == b]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == b]['Access']

    plt.plot(years, sum_elec, label=b, linestyle="--")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()

for d in unique_countries:
  if d in American_countries:
    # match country to one of our we want to look at and get a list of years
    years = df[df['Entity'] == d]['Year']

    # match country to one of our we want to look at and get a list of electriciy values
    sum_elec = df[df['Entity'] == d]['Access']

    plt.plot(years, sum_elec, label=d, linestyle="-")

plt.ylabel('Percentage of Country Population')
plt.xlabel('Year')
plt.title('Percent of Population with Access to Electricity')
plt.legend()
plt.show()
