import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv("petrol_consumption.csv")

print(dataset.columns)

x = dataset.Average_income
print(x)

print(dataset.Petrol_Consumption.describe())

