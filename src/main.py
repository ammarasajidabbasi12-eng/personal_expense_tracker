import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
from analysis import*
from visualisation import *
from loader import *
def main():
    base_dir=os.path.dirname(__file__)
    filepath=os.path.join(os.path.join(base_dir,'..','data','personal_expense_tracker.csv'))
    df=load_data(filepath)
    print(df)
    print(calculate_total_spending(df))
    print(total_average(df))
    total_spending_per_category(df)
    highest_spending(df)
    top_two_spendings(df,2)
    total_spendings_per_month(df)
    top_spending_by_month(df)
    calculate_correlation(df)
    fig,axes =plt.subplots(2,2,figsize=(14,10))
    plot_amount_distribution(df,axes[0,0])
    plot_correlation(df,axes[0,1])
    plot_total_spending_by_month(df,axes[1,0])
    plot_total_spendings_per_category(df,axes[1,1])
    plt.tight_layout()
    base_dir = Path(__file__).resolve().parent
    output_dir = base_dir.parent / "data" / "output"

    output_dir.mkdir(parents=True, exist_ok=True)

    plt.savefig(output_dir / "dashboard.png", dpi=300, bbox_inches='tight') 
    plt.show()
if __name__=='__main__':
    main()