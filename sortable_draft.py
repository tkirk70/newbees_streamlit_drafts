# Import dependencies
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib
from matplotlib import pyplot as plt

# Try to increase width of layout
st.set_page_config(layout="wide")

# Create imgage variable for league logo
components.html(
    """
    
    <img class="NavSecondary__Logo__Img imageLoaded " src="https://g.espncdn.com/lm-static/ffl/images/ffl-shield-shield.svg" alt="Fantasy Football Home">
    
    
    """,
    width=159
)
# Load df from excel
df = pd.read_excel('combined_newbees_draft.xlsx')
# # Filter by year
# years = df['year'].drop_duplicates()
# make_choice = st.sidebar.selectbox('Select your year:', years)
# filtered_df = df[df.loc['year'].is_in(make_choice)]
# st.dataframe(filtered_df)

# Get rid of index
# df.reset_index(drop=True, inplace=True)

# Create header and subheader
st.title('Sortable Newbees Drafts: 2013-2020')
st.subheader(
    'Use the dropdowns on the left to sort through different teams or years.')

# Diplay the default dataframe.
# st.dataframe(df, use_container_width=True)

# Add radio button to choose between All or Individual
st.sidebar.radio('Choose your own fantasy',
                 ("All Newbees", "Individual Team"))

options = df['year'].drop_duplicates()
options2 = df['round'].drop_duplicates()
selected_options = st.sidebar.selectbox(
    'Which year do you want relive?', options)
selected_options2 = st.sidebar.selectbox('Which round do you want?', options2)
st.write('Year: ', selected_options, 'Round: ', selected_options2)
filtered_df = df[(df['year'] == selected_options) &
                 (df['round'] == selected_options2)]

# team_options = df['newbees_team'].unique().tolist()
# selected_teams = st.sidebar.selectbox('Which team do you want?',team_options)
# filtered_df2 = filtered_df[filtered_df["newbees_team"].isin(selected_teams)]

st.dataframe(filtered_df)
# st.dataframe(filtered_df2)


st.write('Where did you go wrong?')

components.iframe(
    "https://g.espncdn.com/lm-static/ffl/images/ffl-shield-shield.svg")

# st.markdown("# Heat Maps under construction ????")
# st.sidebar.markdown("# Heat Maps ????")

# # figure out how to make this df without excel.

# df = pd.read_excel('season_2021.xlsx', sheet_name='combined_2021')

# teams = df.columns.to_list()

# weeks = df.Week.to_list()

# df.set_index(['Week'], inplace=True)

# # Python program to generate a heatmap
# # which displays the value in each cell
# # corresponding to the given dataframe

# # import required libraries

# # displaying dataframe as an heatmap
# # with diverging colourmap as virdis
# df_heat = df.style.background_gradient(cmap='viridis')\
#     .set_properties(**{'font-size': '11px'})

# st.dataframe(df_heat)
