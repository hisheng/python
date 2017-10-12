import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rn



data_set = pd.read_csv("HR_comma_sep.csv",",")
print(data_set.info())
print(data_set.head())