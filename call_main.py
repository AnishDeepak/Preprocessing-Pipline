from main_csv import Preprocess
import pandas as pd

df=pd.read_csv('house_price.csv')
p=Preprocess(df)
p.df_basic_info()
p.impute_missing_values()