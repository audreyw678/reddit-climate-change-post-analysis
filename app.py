import streamlit as st
import pandas as pd
import altair as alt

def removeLeadingQuotations(title):
    """Remove leading quotation marks from a title string."""
    return title.strip('"').strip("'")

st.title("Reddit Climate Change Topic Visualizer")
st.write("This app visualizes topics from Reddit posts about climate change over time. You can also see the distribution of subreddits where a certain topic(s) was posted.")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

df_100k = load_data("data/df_100k.csv")
topic_info = load_data("data/topic_info.csv")

st.header("Prevalence of topics over time")

df_100k['Date'] = pd.to_datetime(df_100k['created_utc'], unit='s') # convert to datetime
topic_info['Title'] = topic_info['Title'].apply(removeLeadingQuotations) # clean titles
df_vis = df_100k[df_100k['Topic'] != -1].copy()                    # filter out noise topic
df_vis['Month'] = df_vis['Date'].dt.to_period('M').dt.to_timestamp() # extract month
df_vis = df_vis.merge(
    topic_info[['Topic', 'Title']],
    on='Topic',
    how='left'                    
)
all_topics = topic_info['Title'].unique().tolist()[1:]

selected_topics = st.multiselect("Select topics to include",
    options=all_topics,
    default=all_topics, key='multiselect1'
)

topic_over_time = df_vis.pivot_table(
    index='Month',
    columns='Title',
    values='full_text',  
    aggfunc='count',     # count posts per topic per month
    fill_value=0         # missing = 0 posts per topic in that month
).reindex(all_topics, axis=1)

st.area_chart(
    topic_over_time[selected_topics]
)

st.divider()
st.header("Subreddit distribution of topics")

selected_topics2 = st.multiselect("Select topics to include",
    options=all_topics,
    default=all_topics, key='multiselect2')

filtered_df = df_vis[df_vis['Title'].isin(selected_topics2)]
subreddit_dist = filtered_df['subreddit.name'].dropna().value_counts().head(30).reset_index()
subreddit_dist.columns = ['subreddit name', 'posts']
subreddit_dist['subreddit name'] = subreddit_dist['subreddit name'].apply(lambda x: 'r/' + x)
subreddit_dist = subreddit_dist.sort_values('posts', ascending=False)

chart = alt.Chart(subreddit_dist).mark_bar().encode(x=alt.X("subreddit name", sort=None), y="posts")
st.altair_chart(chart, use_container_width=True)