import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd
import numpy as np
from scipy import stats

# Import the data
gentrification = pd.read_csv("./data/gentrification.csv")
white_change = gentrification["pct_white_alone_change"]
black_change = gentrification["pct_black_alone_change"]
asian_change = gentrification["pct_asian_alone_change"]
hispanic_change = gentrification["pct_hispanic_or_latino_change"]
metro_area = gentrification["metro_area"]


# Clean the data for each race
df = pd.DataFrame({
    'white': white_change,
    'black': black_change,
    'asian': asian_change,
    'hispanic': hispanic_change,
    'metro_area': metro_area
})

clean_df = df.dropna()
aggregated_df = df.groupby('metro_area').agg({'white': 'mean', 'black': 'mean', 'asian': 'mean', 'hispanic': 'mean'}).reset_index()
aggregated_df['metro_area'] = aggregated_df['metro_area'].replace({'Atlanta-Sandy Springs-Alpharetta' : 'Atlanta', 
                                                  'Baltimore-Columbia-Towson': 'Baltimore', 
                                                  'New York-Newark-Jersey City': 'New York City', 
                                                  'San Francisco-Oakland-Berkeley': 'Oakland',
                                                  'Washington-Arlington-Alexandria': 'Washington, D.C'})

aggregated_df.set_index('metro_area').plot(kind='barh', figsize=(8, 5), color=['red', 'blue', 'orange', 'green'])

plt.ylabel('Metro Area', labelpad=10) 
plt.xlabel('Population Change (%)', labelpad=20)  
plt.ticklabel_format(style='plain', axis='x') 
plt.title('Change in Population by Race from 2000 to 2017 in Metropolitan Areas')
plt.legend()
plt.grid(axis='x', linestyle='--', alpha=0.7)  
plt.subplots_adjust(bottom=0.2) 
plt.figtext(0.5, 0.02, "Black people in these five metropolitan areas saw the greatest decrease in population after gentrification.", wrap=True, horizontalalignment='center', fontsize=10)

# save the figure as PNG
plt.savefig("white_hat.png", bbox_inches='tight', dpi=300) 

plt.show()
