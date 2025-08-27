import streamlit as st
import zipfile
import pandas as pd

st.title("Reddit Climate Change Topic Visualizer")
st.write("This app visualizes topics from Reddit posts about climate change over time.")

df_100k = pd.read_csv("data/df_100k.csv")
topic_info = pd.read_csv("data/topic_info.csv")
df_100k['Date'] = pd.to_datetime(df_100k['created_utc'], unit='s') # convert to datetime
df_vis = df_100k[df_100k['Topic'] != -1].copy()                    # filter out noise topic
df_vis['Month'] = df_vis['Date'].dt.to_period('M').dt.to_timestamp() # extract month
df_vis = df_vis.merge(
    topic_info[['Topic', 'Title']],
    on='Topic',
    how='left'                    
)
topic_over_time = df_vis.pivot_table(
    index='Month',
    columns='Title',
    values='full_text',  
    aggfunc='count',     # count posts per topic per month
    fill_value=0         # missing = 0 posts per topic in that month
)

all_topics = df_vis['Title'].tolist()
selected_topics = st.multiselect(
    "Select Topics to Display",
    options=all_topics,
    default=all_topics[:10]
)

st.area_chart(
    topic_over_time[selected_topics]
)

# TODO: FIX ORDER OF TOPICS, CONTROL ALLOWED SCROLLING BEHAVIOR, ADD MORE CHARTS (SUBREDDIT ETC)