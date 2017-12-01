# libraries
import numpy as np
import quandl
import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# reading the data
data  = web.DataReader('IBM','google')
data.head(10)

data = quandl.get("WIKI/GOOGL")
data.head()

# plotting
plt.figure(figsize=(10,4))
plt.grid(True)
plt.plot(data['Open'],"ro")
plt.show()


sns.distplot(data['Open'],bins=100,color="green")
plt.show()

sns.distplot(data['Open'].pct_change().dropna(),bins=100,color="green")

# simulation function
def stock_simulator(starting_price,periods,mean,std):
    X_axis = []
    Y_axis = []
    
    current_period = 1
    previous_price = starting_price
    
    while current_period <= periods:
        
        drift = float(mean)/periods
        shock = np.random.normal(drift,float(std)/np.sqrt(periods))
        
        X_axis.append(current_period)
        Y_axis.append(current_price)
        
        current_price = previous_price + previous_price*(drift + shock)
    
    plt.plot(X_axis,Y_axis)


# simulation itself
simulations=0
while simulations < 100:
    stock_simulator(starting_price,periods,mean,std)
    simulations = simulations + 1

plt.ylabel('Price')
plt.xlabel('Days')
plt.title('Monte Carlo Simulation for Google's stock price)
plt.show()
