import pandas as pd
from matplotlib import pyplot as plt

# data = pd.read_csv("Calgary.csv")
# data = pd.read_csv("ClarknetAug28.csv") # too small, only 7 days
# data = pd.read_csv("ClarknetSep4.csv") # too small, only 7 days
data = pd.read_csv("NASAAug95.csv") # ! 可能存在问题
# data = pd.read_csv("NASAJul95.csv")
# data = pd.read_csv("Saskhttp.csv")
plt.plot(data["values"])
plt.show()