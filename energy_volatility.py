import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import seaborn as sns


oil=yf.download('CL=F', start='2020-01-01', end="2024-12-12")
gas=yf.download('NG=F', start='2020-01-01', end="2024-12-12")
gold=yf.download('GC=F', start='2020-01-01', end="2024-12-12")

oil=oil.droplevel(1,axis=1)#flatten the MultiIndex on
gas=gas.droplevel(1,axis=1)
gold=gold.droplevel(1,axis=1)

#1-Explore the data

print("\n the columns of the data")
print(oil.columns)# one is enough cause basically all got the same layout

print("\n the number of rows and columns in each")
print("\noil:",oil.shape,
      "\ngas:",gas.shape,
      "\ngold:",gold.shape)


print("\n the overall information about the data")

print("\noil:",oil.describe(),
      "\ngas:",gas.describe(),
      "\ngold:",gold.describe())


print("\n missing vlaues in each data")
print("\n oil:",oil.isnull().sum(),
      "\ngold:",gold.isnull().sum(),
      "\ngas:",gas.isnull().sum())


#2-Cleaning the data

oil=oil['Close']# keeping only the Close column
gold=gold["Close"]
gas=gas['Close']


df=pd.concat([oil,gas,gold],axis=1) #axis=1 means join them side by side (columns) rather than stacking them on top of each other.
df.columns=['Oil','Gas','Gold']
df=df.dropna()


#3-analysing the data

df["Oil_Vol"]=df['Oil'].rolling(30).std() #calculate 30-day rolling standard deviation for each commodity
df["Gas_Vol"]=df['Gas'].rolling(30).std()
df["Gold_Vol"]=df['Gold'].rolling(30).std()


correlation=df[['Oil','Gas','Gold']].corr()#.corr() calculates the correlation between every pair of columns automatically and returns a table.
print(correlation)



#4-visuliazation 

fig, (ax1, ax2,ax3) = plt.subplots(3, 1, figsize=(12, 14))


#Price chart (all three commodities)
oil.plot(ax=ax1, label='Oil')
gas.plot(ax=ax1, label='Gas')
gold.plot(ax=ax1, label='Gold')
ax1.set_title('Oil vs Gold vs Gas')
ax1.set_ylabel('Price (USD)')
ax1.legend()


# Chart 3 - Volatility
df['Oil_Vol'].plot(ax=ax2, label='Oil_Volatility')
df['Gas_Vol'].plot(ax=ax2, label='Gas_Volatility')
df['Gold_Vol'].plot(ax=ax2, label='Gold_Volatility')
ax2.set_title('Volatility chart')
ax2.set_ylabel('Volatility (USD)')
ax2.set_xlabel('Date')
ax2.legend()


#heatmap you need seaborn library
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax3)

plt.tight_layout()
plt.show()