import curses
import math

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

import admin.admin_options
import connector

stdscr = curses.initscr()
def start():
    plotSalesChart()


def plotSalesChart():
    # connect to the database and retrieve the data
    conn = connector.connect_to_database()
    df = pd.read_sql_query("SELECT bookingDate, COUNT(*) as count FROM booking GROUP BY bookingDate", conn)

    # generate the chart using Seaborn
    sns.barplot(x='bookingDate', y='count', data=df)

    # customize the chart
    sns.set_style("whitegrid")
    plt.xlabel('Booking Date')
    plt.ylabel('Number of Bikes Booked')
    plt.title('Daily Bike Bookings')

    max_count = max(df['count'])
    plt.ylim(0, max_count)
    plt.yticks(range(0, max_count+1, 1))

    # display the chart
    plt.show()
    admin.admin_options.print_admin_options()
