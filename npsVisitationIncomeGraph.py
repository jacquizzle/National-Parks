import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
natl_park_total_data = pd.read_csv('Totalvisits.csv')
natl_park_visitors = natl_park_total_data[['Year','RecreationVisitors']]
us_median_income = pd.read_csv('usincome.csv')
us_median_income['DATE'] = pd.to_datetime(us_median_income['DATE'])
us_median_income['DATE'] = pd.DatetimeIndex(us_median_income['DATE']).year
us_median_income['DATE'] = pd.to_numeric(us_median_income['DATE'])
us_median_income = us_median_income.rename(columns={'DATE': 'Year', 'MEHOINUSA672N': 'US Median Income'})
us_gas = pd.read_csv('usgas.csv')
us_gas = us_gas.rename(columns={'U.S. All Grades All Formulations Retail Gasoline Prices Dollars per Gallon': 'Avg Gas Price'})
economic_factors = pd.merge(us_median_income, us_gas, how='inner', on='Year')
nps_with_econ = pd.merge(natl_park_visitors, economic_factors, how='inner', on='Year')
nps_income = sns.lmplot("US Median Income", "RecreationVisitors", data=nps_with_econ)
nps_income.set(xlim =(56500,70000))
plt.tight_layout()
plt.show()

