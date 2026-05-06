import pandas as pd
import os
def load_data(filepath):
    df=pd.read_csv(filepath,parse_dates=['date'])
    for c in df.select_dtypes(include='object').columns:
        df[c]=df[c].str.strip().str.lower()
    df['month']=df['date'].dt.month_name()
    month_order = [
    "January","February","March","April","May","June",
    "July","August","September","october","November","December"]
    df['month']=pd.Categorical(df['month'],categories=month_order,ordered=True)
    df=df.sort_values('month')
    df['day'] = df['date'].dt.day
    df['month_num'] = df['date'].dt.month
    return df
