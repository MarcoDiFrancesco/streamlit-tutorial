# %%
import pandas as pd
import streamlit as st
import plotly.express as px
from random import randint
from time import sleep

# Write text in different sizes
# ...

# Download Data
# link = f"http://data.insideairbnb.com/united-states/ny/new-york-city/2022-06-03/visualisations/listings.csv"
# df = pd.read_csv(link)

# Cache Data
# @st.cache
# def download_csv():
#     df = pd.read_csv(link)
#     # sleep(3)
#     return df
# df = download_csv()


# Show table
# st.header("Show table")
# st.table(df.head(10))

# Show dataframe size
# st.header("Show dataframe size")
# st.markdown(f"Dataframe contains {len(df)} row")

# Price min and max values
# min_val = 0
# max_val = 10000
# st.markdown(f"Max {max_val} Min {min_val}")

# Slider: one value
# st.header("Sliders")
# slider_val = st.slider("Select price range", min_val, max_val)
# st.markdown(f"Slider value: {slider_val}")

# Slider: range
# min_sel, max_sel = st.slider("Select price range", value=(min_val, max_val))
# st.markdown(f"Slider value: {min_sel} and {max_sel}")

# Filter data
# df1 = df[(df.price > min_sel) & (df.price < max_sel)]

# Table and rows count
# st.table(df1.head())
# st.markdown(f"Dataframe contains {len(df1)} row")

# Map
# st.header("Map")
# st.map(df1[["latitude", "longitude"]])

# Property price distribution: slider
# min, max = st.sidebar.slider(
#     "Price range",
#     int(df.price.min()),
#     1000,
#     (0, 600),
# )

# Property price distribution: filter dataframe
# df2 = df[(df.price > min) & (df.price < max)]

# Property price distribution: histogram
# st.header("Property price distribution")
# f = px.histogram(df2, x="price", nbins=15, title="Price distribution")
# f.update_xaxes(title="Price")
# f.update_yaxes(title="No. of listings")
# st.plotly_chart(f)

# Filter by Neighborhood
# st.header("Filter by Neighborhood")
# neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
# df3 = df[df.neighbourhood_group == neighborhood]
# st.map(df3[["latitude", "longitude"]])

# Cats and dogs
# st.header("Cats and dogs")
# pics = {
#     "Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
#     "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
#     "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg",
# }
# pic = st.selectbox("Picture choices", list(pics.keys()), 0)
# st.image(pics[pic], use_column_width=True, caption=pics[pic])

# Party time
# st.markdown("## Party time!")
# st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
# btn = st.button("Chborhood")
# neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
# df3 = df[df.neighbourhood_group == neighborhood]
# st.map(df3[["latitude", "elebrate!")
# if btn:
#     st.balloons()
