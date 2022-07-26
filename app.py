import pandas as pd
import streamlit as st
import plotly.express as px


#### Write text in different sizes
st.title("Streamlit") # h1
st.header("Data visualization") # h2
st.markdown("""# Markdown title
## Subtitle
### Somthing smaller
""")

#### Importing and caching
@st.cache
def get_data():
    return pd.read_csv(
        "http://data.insideairbnb.com/united-states/ny/new-york-city/2022-06-03/visualisations/listings.csv"
    )


df = get_data()

#### Write into the file
st.markdown(f"Dataframe contains {len(df)} rows")
st.dataframe(df.head(10))

#### 
st.header("Where are the properties located?")
st.subheader("On a map")

min_val = int(df["price"].min())
max_val = int(df["price"].max())
sel_min, sel_max = st.slider("Select price range", value=(min_val, max_val))
df_map = df.copy()
# df_map = df_map[(df_map.price >= sel_min) & (df_map.price <= sel_max)]
df_map = df_map.query("price >= @sel_min and price <= @sel_max")
st.map(df_map[["latitude", "longitude"]])
st.subheader("In a table")
st.markdown("Following are the top five most expensive properties.")
st.write(df_map.sort_values("price", ascending=False).head())

st.subheader("Selecting a subset of columns")
defaultcols = ["name", "host_name", "neighbourhood", "room_type", "price"]
cols = st.multiselect("Columns", df.columns.tolist(), default=defaultcols)
st.dataframe(df[cols].head(1000))

st.header("Average price by room type")
dfp = df[["room_type", "price"]].groupby("room_type").mean().sort_values("price")
st.table(dfp)

st.header("Which host has the most properties listed?")


st.table(
    df.groupby(["host_id", "host_name"])
    .count()
    .sort_values("id", ascending=False)
    .rename({"id": "count"}, axis=1)
    .reset_index()[["host_name", "count"]]
    .head(5)
)


st.header("What is the distribution of property price?")
st.write(
    """Select a custom price range from the side bar to update the histogram below displayed as a Plotly chart using
[`st.plotly_chart`](https://streamlit.io/docs/api.html#streamlit.plotly_chart)."""
)
values = st.sidebar.slider(
    "Price range",
    float(df.price.min()),
    float(df.price.clip(upper=1000.0).max()),
    (50.0, 300.0),
)
f = px.histogram(
    df.query(f"price.between{values}"), x="price", nbins=15, title="Price distribution"
)
f.update_xaxes(title="Price")
f.update_yaxes(title="No. of listings")
st.plotly_chart(f)

st.header("What is the distribution of availability in various neighborhoods?")
st.write("Using a radio button restricts selection to only one option at a time.")
st.write(
    "💡 Notice how we use a static table below instead of a data frame. \
Unlike a data frame, if content overflows out of the section margin, \
a static table does not automatically hide it inside a scrollable area. \
Instead, the overflowing content remains visible."
)
neighborhood = st.radio("Neighborhood", df.neighbourhood_group.unique())
show_exp = st.checkbox("Include expensive listings")
show_exp = " and price<200" if not show_exp else ""


@st.cache
def get_availability(show_exp, neighborhood):
    return (
        df.query(
            f"""neighbourhood_group==@neighborhood{show_exp}\
        and availability_365>0"""
        )
        .availability_365.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9, 0.99])
        .to_frame()
        .T
    )


st.table(get_availability(show_exp, neighborhood))
st.write(
    "At 169 days, Brooklyn has the lowest average availability. At 226, Staten Island has the highest average availability.\
    If we include expensive listings (price>=$200), the numbers are 171 and 230 respectively."
)
st.markdown(
    "_**Note:** There are 18431 records with `availability_365` 0 (zero), which I've ignored._"
)

df.query("availability_365>0").groupby(
    "neighbourhood_group"
).availability_365.mean().plot.bar(rot=0).set(
    title="Average availability by neighborhood group",
    xlabel="Neighborhood group",
    ylabel="Avg. availability (in no. of days)",
)
st.pyplot()

st.header("Properties by number of reviews")
st.write(
    "Enter a range of numbers in the sidebar to view properties whose review count falls in that range."
)
minimum = st.sidebar.number_input("Minimum", min_value=0)
maximum = st.sidebar.number_input("Maximum", min_value=0, value=5)
if minimum > maximum:
    st.error("Please enter a valid range")
else:
    df.query("@minimum<=number_of_reviews<=@maximum").sort_values(
        "number_of_reviews", ascending=False
    ).head(50)[
        [
            "name",
            "number_of_reviews",
            "neighbourhood",
            "host_name",
            "room_type",
            "price",
        ]
    ]

st.write(
    "486 is the highest number of reviews and two properties have it. Both are in the East Elmhurst \
    neighborhood and are private rooms with prices $65 and $45. \
    In general, listings with >400 reviews are priced below $100. \
    A few are between $100 and $200, and only one is priced above $200."
)
st.header("Images")
pics = {
    "Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
    "Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
    "Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg",
}
pic = st.selectbox("Picture choices", list(pics.keys()), 0)
st.image(pics[pic], use_column_width=True, caption=pics[pic])

st.markdown("## Party time!")
st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
btn = st.button("Celebrate!")
if btn:
    st.balloons()
