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
