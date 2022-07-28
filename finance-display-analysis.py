import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas_datareader
import datetime
import pandas_datareader.data as web
from pandas.plotting import scatter_matrix

start=datetime.datetime(2012,1,1)
end=datetime.datetime(2017,1,1)
tesla=web.DataReader("TSLA","yahoo",start,end)
ford=web.DataReader("F","yahoo",start,end)
gm=web.DataReader("GM","yahoo",start,end)
plt.subplot(3,1,1)
tesla["Open"].plot(label="Tesla",title="Open Price",figsize=(16,8))
ford["Open"].plot(label="Ford")
gm["Open"].plot(label="GM")
plt.legend()
plt.tight_layout()

plt.subplot(3,1,2)
tesla["Volume"].plot(label="Tesla",title="Volume Traded",figsize=(16,8))
ford["Volume"].plot(label="Ford")
gm["Volume"].plot(label="GM")
plt.legend()
plt.tight_layout()

tesla["Total Traded"]=tesla["Open"]*tesla["Volume"]
ford["Total Traded"]=ford["Open"]*ford["Volume"]
gm["Total Traded"]=gm["Open"]*gm["Volume"]

plt.subplot(3,1,3)
tesla["Total Traded"].plot(figsize=(16,8),label="Tesla",title="Total Traded")
ford["Total Traded"].plot(label="Ford")
gm["Total Traded"].plot(label="GM")
plt.legend()
plt.tight_layout()

gm["MA50"]=gm["Open"].rolling(50).mean()
gm["MA200"]=gm["Open"].rolling(200).mean()
gm[["Open","MA50","MA200"]].plot(label="gm",figsize=(16,8),title="Bollinger Band Analysis")
plt.legend()

car_compiled = pd.concat([tesla["Open"],ford["Open"],gm["Open"]],axis=1)
car_compiled.columns = ["Tesla Open","Ford Open","GM Open"]
scatter_matrix(car_compiled,figsize=(8,8),hist_kwds={"bins":50})

plt.show()

