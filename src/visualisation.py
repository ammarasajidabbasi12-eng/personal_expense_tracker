import matplotlib.pyplot as plt
from analysis import*
import seaborn as sns
#pie chart
def plot_total_spendings_per_category(df,ax):
   total=total_spending_per_category(df)
   if isinstance(total,pd.DataFrame):
      total=total.set_index('category')['amount']
   total.plot(kind='pie',ax=ax ,autopct='%1.1f%%')
   ax.set_title('total spending per category')
   ax.set_xlabel('equal')
#bar_chart
def plot_total_spending_by_month(df,ax):
   monthly=total_spendings_per_month(df)
   monthly=monthly[monthly>0]
   monthly.plot(kind='line',marker='o' ,ax=ax)
   ax.set_title("spending trends over month")
   ax.set_xlabel('month')
   ax.set_ylabel('amount')
   ax.tick_params(axis='x', rotation=45)

def plot_amount_distribution(df,ax):
   df['amount'].plot(kind='hist',bins=7,ax=ax)
   ax.set_title("amount distribution")
   ax.set_xlabel('amount')
   ax.set_ylabel('frequency')

def plot_correlation(df,ax):
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr,annot=True,cmap='coolwarm',ax=ax)
    ax.set_title("correlation heatmap")