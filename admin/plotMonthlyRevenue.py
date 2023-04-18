import math

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import connector

def start():
    plotMonthlyRevenue()


def plotMonthlyRevenue():
    # connect to the database and retrieve the data
    conn = connector.connect_to_database()
    df = pd.read_sql_query(
        "SELECT MONTH(bookingDate) AS month, SUM(paymentAmount) AS earnings FROM booking GROUP BY month",
        conn)

    # set the style and color palette
    sns.set_style('whitegrid')
    sns.set_palette('husl')

    # create the bar chart using Seaborn
    ax = sns.barplot(x='month', y='earnings', data=df)

    # customize the chart
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Earnings')
    ax.set_title('Monthly Earnings')

    # display the chart
    plt.show()
