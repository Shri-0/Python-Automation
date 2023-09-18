import pandas as pd
import csv

# this gets basic data from a wikipedia table. Will get the viwership for each season of the simpsons
'''
simpsons = pd.read_html(
    'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

#print(len(simpsons))
print(simpsons[1])
'''

# Can read and change column names
'''
data = pd.read_csv('https://www.football-data.co.uk/mmz4281/2324/E0.csv')
#df = pd.DataFrame(data)
#print(data)
#print(df)

data.rename(columns={'PCAHA':'P', 'MaxCAHH': 'Max'}, inplace=True)

print(data)
'''
