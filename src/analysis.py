import pandas as pd
#tell me overall spendings
def calculate_total_spending(df):
    total=df['amount'].sum()
    return total
#tell me average spending
def total_average(df):
    avg=df['amount'].mean()
    return avg
#tell me categorywise spendings
def total_spending_per_category(df):
    category_total=df.groupby(['category'],as_index=False)['amount'].sum()
    return category_total
def highest_spending(df):
    highest_spend=total_spending_per_category(df).idxmax()
    return highest_spend
def top_two_spendings(df,n):
    top_two=total_spending_per_category(df).sort_values(by='amount',ascending=False).head(n)
    return top_two
def total_spendings_per_month(df):
    total_per_month=df.groupby('month')['amount'].sum()
    return total_per_month
def top_spending_by_month(df):
    return total_spendings_per_month(df).idxmax()
def calculate_correlation(df):
    corr=df[['amount']].corr()
    return corr