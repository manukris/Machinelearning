import pandas as pd

filepath = "Melbourne_housing_extra_data.csv"
data = pd.read_csv(filepath)
print(data.columns)

y = data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = data[melbourne_features]

print(X.head())