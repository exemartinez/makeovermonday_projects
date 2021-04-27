
# %%
# Imports

RANDOM_SEED = 12345
from numpy.random import seed
seed(RANDOM_SEED)

import matplotlib.pyplot as plt
import pandas as pd

import os
import numpy as np
import time

# %%
df = pd.read_csv('/home/osboxes/Documents/makeovermonday/data/makeovermonday-2021w17/data/regional_price_parities_by_state.csv', index_col=0)  

# %%
df.describe()
# %%
df.boxplot()
# %%
all_states_df = df.loc[df.geoname != "United States"]

# %%
all_items_df = all_states_df.loc[all_states_df.description == "All items"]
all_items_df = all_items_df.drop(labels=["linecode"], axis=1)
# %%
all_items_df.describe()

# %%
all_items_df.boxplot()

# %%
array = all_items_df.to_numpy()

# %%
array.shape
# %%
(all_items_df.mean()).mean()

# %%

plt.lineh()