import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    data = pd.read_csv("epa-sea-level.csv")
    
    # Scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label='Original Data')
    
    # Line of best fit for all data
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_all = range(1880, 2051)
    plt.plot(x_all, slope_all * pd.Series(x_all) + intercept_all, 'r', label='Best Fit (All Data)')
    
    # Line of best fit for data from 2000 onwards
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(
        recent_data['Year'], recent_data['CSIRO Adjusted Sea Level']
    )
    x_recent = range(2000, 2051)
    plt.plot(x_recent, slope_recent * pd.Series(x_recent) + intercept_recent, 'g', label='Best Fit (2000 Onwards)')
    
    # Add title, labels, and legend
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    
    # Save plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()  # Ensure there are no non-breaking spaces here
