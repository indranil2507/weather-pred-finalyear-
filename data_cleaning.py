import pandas as pd
import numpy as np
data = pd.read_csv("dataset_ml.csv")

# drop (delete) the unnecessary columns in the data


data = data.replace('T', 0.0)
data = data.replace('-', 0.0)

# Save the data in a csv file
data.to_csv('dataset_ml.csv')