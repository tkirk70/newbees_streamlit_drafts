# Import dependencies
import pandas as pd
import streamlit as st 

# Try to increase width of layout
st.set_page_config(layout="wide")

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
st.subheader('Use the dropdowns on the left to sort through different teams or years.')

# Diplay the default dataframe.
st.dataframe(df, use_container_width=True)

options = df['year'].drop_duplicates()
selected_options = st.sidebar.selectbox('Which year do you want?',options)
st.write(selected_options)
filtered_df = df[df['year'] == selected_options]

# team_options = df['newbees_team'].unique().tolist()
# selected_teams = st.sidebar.selectbox('Which team do you want?',team_options)
# filtered_df2 = filtered_df[filtered_df["newbees_team"].isin(selected_teams)]

st.dataframe(filtered_df)
# st.dataframe(filtered_df2)




st.write('Where did you go wrong?')
