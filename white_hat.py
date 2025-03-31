import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
from scipy import stats

# Import the data
census_data_metro = pd.read_csv("./data/census_data_metro.csv")
white_alone = census_data_metro["white_alone_17"]
black_alone = census_data_metro["black_alone_17"]
asian_alone = census_data_metro["asian_alone_17"]
hispanic_alone = census_data_metro["hispanic_or_latino_17"]
metro_area = census_data_metro["metro_area"]


'''
Atlanta-Sandy Springs-Alpharetta, GA (for Atlanta)
Baltimore-Columbia-Towson, MD (for Baltimore)
New York-Newark-Jersey City, NY-NJ-PA (for New York City)
San Francisco-Oakland-Berkeley, CA (for Oakland)
Washington-Arlington-Alexandria, DC-VA-MD-WV (for Washington, D.C.)'


'''
# Clean the data for each race
df = pd.DataFrame({
    'white': white_alone,
    'black': black_alone,
    'asian': asian_alone,
    'hispanic': hispanic_alone,
    'metro_area': metro_area
})

clean_df = df.dropna()
aggregated_df = df.groupby('metro_area').agg({'white': 'sum', 'black': 'sum', 'asian': 'sum', 'hispanic': 'sum'}).reset_index()
aggregated_df['metro_area'] = aggregated_df['metro_area'].replace({'Atlanta-Sandy Springs-Alpharetta' : 'Atlanta', 
                                                  'Baltimore-Columbia-Towson': 'Baltimore', 
                                                  'New York-Newark-Jersey City': 'New York City', 
                                                  'San Francisco-Oakland-Berkeley': 'Oakland',
                                                  'Washington-Arlington-Alexandria': 'Washington, D.C'})

aggregated_df.set_index('metro_area').plot(kind='bar', figsize=(8, 5), color=['red', 'blue', 'orange', 'green'])

plt.xlabel('Metro Area', labelpad=20)
plt.xticks(rotation=0)
plt.ylabel('Population', labelpad=20)
plt.ticklabel_format(style='plain', axis='y')  # Alternative method
plt.title('Racial Populations in Metropolitan Areas')
plt.legend()
plt.grid()
plt.figtext(0.5, -0.1, "White people are the race with the highest population in all 5 of these metropolitan areas.", wrap=True, horizontalalignment='center', fontsize=10)

# save the figure as PNG
# plt.savefig("white_hat.png") 

plt.show()
