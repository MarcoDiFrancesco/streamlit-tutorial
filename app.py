# %%
import pandas as pd
import streamlit as st
import plotly.express as px
from random import randint
from time import sleep

# Write text in different sizes
# ...

# Download Data
link = f"http://data.insideairbnb.com/united-states/ny/new-york-city/2022-06-03/visualisations/listings.csv"
df = pd.read_csv(link)

# Cache Data
# @st.cache
# def function():
#     df = pd.read_csv(link)
#     sleep(3)
#     return df
# df = function()
        

# Show table
st.table(df.head(10))

# Show dataframe size
st.markdown(f"Dataframe contains {len(df)} row")

# Price min and max values
min_val = int(df["price"].min())
max_val = int(df["price"].max())
st.markdown(f"Max {max_val} Min {min_val}")

# Slider: one value
slider_val = st.slider("Select price range", min_val, max_val)
st.markdown(f"Slider value: {slider_val}")

# Slider: range
min_sel, max_sel = st.slider("Select price range", value=(min_val, max_val))
st.markdown(f"Slider value: {min_sel} and {max_sel}")

# Filter data
df1 = df[(df.price > min_sel) & (df.price < max_sel)]

# Table and rows count
st.table(df1.head())
st.markdown(f"Dataframe contains {len(df1)} row")

# Map
st.map(df1[["latitude", "longitude"]])







# Distribution of property price
min, max = st.sidebar.slider(
    "Price range",
    int(df.price.min()),
    1000,
    (0, 600),
)

df2 = df[(df.price > min) & (df.price < max)]
f = px.histogram(
    df2, x="price", nbins=15, title="Price distribution"
)
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)

# Filter by Neighborhood
neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
