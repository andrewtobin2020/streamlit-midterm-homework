import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

data = pd.read_csv("nfl_mdf.csv")
st.title ("NFL Games Streamlit App")
scatter = alt.Chart(data, title = "Wind vs Total Score since 2000").mark_point().encode(
    x = 'wind',
    y='total'
)
st.altair_chart(scatter, use_container_width=True)

scatter2 = alt.Chart(data, title = "Temperature vs Total Score since 2000").mark_point().encode(
    x = 'temp',
    y='total'
)
st.altair_chart(scatter2, use_container_width=True)

teams = data["home_team"].sort_values().unique()
team = st.selectbox('Pick your favorite team',teams) 
st.text_area(f'Why is {team} your favorite team?')

team2 = st.selectbox('Pick your least favorite team',teams) 
st.text_area(f'Why is {team2} your least favorite team?')

st.text_area('If you are playing fantasy football, how is your team doing? (This is a safe space)')
