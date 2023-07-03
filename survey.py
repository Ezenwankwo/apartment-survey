"""
Analysis of survey result
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud


st.title("Survey Analysis")
st.sidebar.header('Select what to display')

# display data
st.subheader("Data table")
df = pd.read_csv("survey.csv")
# filtering data 
age_selected = st.sidebar.multiselect("Age", df["What is your age?"].value_counts().index)
gender_selected = st.sidebar.multiselect("Gender", df["What is your gender?"].value_counts().index)
location_selected = st.sidebar.multiselect("Location", df["What is your current location?"].value_counts().index)
renter_selected = st.sidebar.multiselect("Renter", df["Have you rented an apartment in Nigeria in the past 5 years?"].value_counts().index)
if any(age_selected):
    df = df[df["What is your age?"].isin(age_selected)]
if any(gender_selected):
    df = df[df["What is your gender?"].isin(gender_selected)]
if any(location_selected):
    df = df[df["What is your current location?"].isin(location_selected)]
if any(renter_selected):
    df = df[df["Have you rented an apartment in Nigeria in the past 5 years?"].isin(renter_selected)]
st.write(df)


# What is your age?
st.subheader("What is your age?")
age = df["What is your age?"].value_counts()
fig = px.pie(values=age, names=age.index)
st.plotly_chart(fig)

# What is your gender?
st.subheader("What is your gender?")
gender = df["What is your gender?"].value_counts()
fig = px.pie(values=gender, names=gender.index)
st.plotly_chart(fig)

# What is your current location?
st.subheader("What is your current location?")
location = df["What is your current location?"].value_counts()
fig = px.pie(values=location, names=location.index)
st.plotly_chart(fig)

# Have you rented an apartment in Nigeria in the past 5 years?
st.subheader("Have you rented an apartment in Nigeria in the past 5 years?")
rented = df["Have you rented an apartment in Nigeria in the past 5 years?"].value_counts()
fig = px.pie(values=rented, names=rented.index)
st.plotly_chart(fig)

# How did you find your previous rental apartment? (Select all that apply)
st.subheader("How did you find your previous rental apartment? (Select all that apply)")
previous_rental = df["How did you find your previous rental apartment? (Select all that apply)"].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=previous_rental.index,
    y=previous_rental.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# On a scale of 1 to 5, how satisfied were you with your previous rental experience?
st.subheader("On a scale of 1 to 5, how satisfied were you with your previous rental experience?")
satisfaction = df["On a scale of 1 to 5, how satisfied were you with your previous rental experience?"].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=satisfaction.index,
    y=satisfaction.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Limited options for suitable apartments
st.subheader("Limited options for suitable apartments")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [Limited options for suitable apartments]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Lack of transparency in terms of pricing and property information
st.subheader("Lack of transparency in terms of pricing and property information")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [Lack of transparency in terms of pricing and property information]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# High agent fees or charges
st.subheader("High agent fees or charges")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [High agent fees or charges]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Difficulty in finding apartments in preferred locations
st.subheader("Difficulty in finding apartments in preferred locations")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [Difficulty in finding apartments in preferred locations]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Time-consuming process of searching for apartments
st.subheader("Time-consuming process of searching for apartments")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [Time-consuming process of searching for apartments]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Inadequate information about the neighbourhood or facilities
st.subheader("Inadequate information about the neighbourhood or facilities")
limited_options = df['Please rate the following challenges or pain points you have experienced when searching for or renting an apartment in Nigeria on a scale of 1 to 5, with 1 being "Not a challenge" and 5 being "Major challenge": [Inadequate information about the neighbourhood or facilities]'].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=limited_options.index,
    y=limited_options.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Which method do you prefer for searching and finding rental apartments?
st.subheader("Which method do you prefer for searching and finding rental apartments?")
method = df["Which method do you prefer for searching and finding rental apartments?"].value_counts()
fig = px.pie(values=method, names=method.index)
st.plotly_chart(fig)

# What features or information do you find most valuable when searching for rental apartments? (Select all that apply)
st.subheader("What features or information do you find most valuable when searching for rental apartments? (Select all that apply)")
preference = df["What features or information do you find most valuable when searching for rental apartments? (Select all that apply)"].value_counts()
fig = go.Figure()
fig.add_trace(go.Bar(
    x=preference.index,
    y=preference.values,
    marker_color='#1f77b4',
))
st.plotly_chart(fig)

# Would you be open to connecting with other renters who have soon-to-be-vacant apartments in your desired location?
st.subheader("Would you be open to connecting with other renters who have soon-to-be-vacant apartments in your desired location?")
connect_to_renters = df["Would you be open to connecting with other renters who have soon-to-be-vacant apartments in your desired location?"].value_counts()
fig = px.pie(values=connect_to_renters, names=connect_to_renters.index)
st.plotly_chart(fig)

# How likely would you be to list your own soon-to-be-vacant apartment for other renters to explore?
st.subheader("How likely would you be to list your own soon-to-be-vacant apartment for other renters to explore?")
vacant = df["How likely would you be to list your own soon-to-be-vacant apartment for other renters to explore?"].value_counts()
fig = px.pie(values=vacant, names=vacant.index)
st.plotly_chart(fig)

# In your opinion, what improvements or changes would you like to see in the apartment rental process in Nigeria?
st.subheader("In your opinion, what improvements or changes would you like to see in the apartment rental process in Nigeria?")
st.set_option('deprecation.showPyplotGlobalUse', False)
text_data =  df['In your opinion, what improvements or changes would you like to see in the apartment rental process in Nigeria? Please share any suggestions or ideas you have.'].str.cat(sep=' ')
w = WordCloud().generate(text_data)
plt.imshow(w)
plt.axis('off')
st.pyplot()
