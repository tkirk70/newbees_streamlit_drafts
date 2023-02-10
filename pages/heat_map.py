# Contents of ~/my_app/pages/page_2.py
import pandas as pd
import streamlit as st

# format precision for floats
pd.set_option('display.float_format','{:.2f}'.format)

st.markdown("# Heat Maps under construction 🔥")
st.markdown("## Weekly Newbees Scoring - 2021")
st.sidebar.markdown("# Heat Maps 🔥")

# figure out how to make this df without excel.

df = pd.read_excel('season_2021.xlsx', sheet_name='combined_2021')

teams = df.columns.to_list()

weeks = df.Week.to_list()

df.set_index(['Week'], inplace=True)

# Python program to generate a heatmap
# which displays the value in each cell
# corresponding to the given dataframe

# import required libraries

# displaying dataframe as an heatmap
# with diverging colourmap as virdis
df_heat = df.style.background_gradient(cmap='viridis')\
    .set_properties(**{'font-size': '11px'}).format(precision=2)

st.dataframe(df_heat, use_container_width=True)

st.markdown("# Seaborn Heat Maps under construction 🔥")
st.markdown("## Weekly Newbees Scoring - 2021")

import matplotlib.pyplot as plt
from pandas import DataFrame
import seaborn as sns

df = pd.read_excel('season_2021.xlsx')
df = df.set_index('Week')

fig, ax = plt.subplots(figsize=(19,11))
sns.set()
sns.heatmap(df, cmap='viridis', annot=True, fmt='.1f', linewidth=.7) #.set(title="Newbee's 2021 Weekly Scores")
# plt.xticks(rotation=45)
# sns.color_palette("viridis", as_cmap=True)
ax.xaxis.tick_top()
ax.set_title("Newbee's 2021 Weekly Scores", fontsize=17, pad=40)
plt.show()

# How to show this in streamlit?
st.pyplot(fig)
