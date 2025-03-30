import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# Import the data
census_data_metro = pd.read_csv("census_data_metro.csv")
white_alone = census_data_metro["white_alone_17"]
black_alone = census_data_metro["black_alone_17"]
asian_alone = census_data_metro["asian_alone_17"]
hispanic_alone = census_data_metro["hispanic_or_latino_17"]
median_income = census_data_metro["median_income_17"]

# Clean the data for each race
white_median = pd.DataFrame({
    'white_alone': white_alone,
    'white_median': median_income
})
clean_white_median = white_median.dropna()

black_median = pd.DataFrame({
    'black_alone': black_alone,
    'black_median': median_income
})
clean_black_median = black_median.dropna()

asian_median = pd.DataFrame({
    'asian_alone': asian_alone,
    'asian_median': median_income
})
clean_asian_median = asian_median.dropna()

hispanic_median = pd.DataFrame({
    'hispanic_alone': hispanic_alone,
    'hispanic_median': median_income
})
clean_hispanic_median = hispanic_median.dropna()

# make the lines of best fit
mw, bw = np.polyfit(clean_white_median["white_alone"], clean_white_median["white_median"], 1)
mb, bb = np.polyfit(clean_black_median["black_alone"], clean_black_median["black_median"], 1)
ma, ba = np.polyfit(clean_asian_median["asian_alone"], clean_asian_median["asian_median"], 1)
mh, bh = np.polyfit(clean_hispanic_median["hispanic_alone"], clean_hispanic_median["hispanic_median"], 1)

line_of_fit_white = mw * clean_white_median["white_alone"] + bw
line_of_fit_black = mb * clean_black_median["black_alone"] + bb
line_of_fit_asian = ma * clean_asian_median["asian_alone"] + ba
line_of_fit_hispanic = mh * clean_hispanic_median["hispanic_alone"] + bh

# plot data
plt.plot(clean_white_median["white_alone"], line_of_fit_white, color='red', label='White')
plt.plot(clean_black_median["black_alone"], line_of_fit_black, color='blue', label='Black')
plt.plot(clean_asian_median["asian_alone"], line_of_fit_asian, color='orange', label='Asian')
plt.plot(clean_hispanic_median["hispanic_alone"], line_of_fit_hispanic, color='green', label='Hispanic')

# truncate the x limit
plt.xlim(0, 8000)
plt.ylim(0, 250000)

plt.xlabel('Population')
plt.ylabel('Median Income')
plt.title('Median Income by Racial Populations in Metropolitan Areas')
plt.legend()
plt.grid()
plt.figtext(0.5, -0.05, "White and Asian people in metropolitan areas have more individuals with higher median incomes than Hispanic and Black people", wrap=True, horizontalalignment='center', fontsize=10)

plt.show()
