Data originally from https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset?resource=download

This project concerns all Reddit posts containing the words "climate" and "change" up until September 2022. It allows you to visualize the distribution of topics over time, as well as the distribution of subreddits in which a certain topic was posted about.

### Setup
This app requires Streamlit, pandas, and Altair, which you can download with 
```bash
pip install streamlit pandas altair
```

You will also have to download the Reddit post data and topic data, which are too large to attach to the GitHub repository. You can download them here (https://drive.google.com/drive/folders/19WSP47EL7DWYMSirMdq1erYLIT-tX0Ev?usp=sharing) and move them to the repository manually. A Python script that automates this is in progress. Ensure that the name of the data folder remains "data" after downloading.

You can then run the app with
```bash
streamlit run app.py
```

Also in progress is a demo video if you want to see how the project works without downloading the files.

### Process (which you can see in the Jupyter Notebook):
1. Dealing with original dataset. Keeping only relevant columns, combining titles and datasets, later on using only a sample of 100k posts out of the original 600k+ for faster computation.
2. Generating sentence embeddings of each post's title + text.
3. 
    -  First attempt at clustering for topic modelling. Tried to use silhouette scores to determine best k value for k-means clustering, but values were all extremely close to 0. Perhaps silhouette score was a poor metric for textual data? Or for textual data under the same macro-topic?
    - Second attempt. Tried using the elbow method to find the best k-value, but there was not a clear elbow point.
    - Third attempt; "let's get an algorithm to find k for me". Tried HDBSCAN (from BERTopic) which was successful except for the very large amount of noise. Looking at some of the topics it generated shows that clusters are mostly headlines rather than subjects or opinions. I could possibly get non-headline-based topic clusters with fuzzy deduplication, but "whatever". Decided to instead switch focus to visualizing the climate change related events/headlines that the clustering algorithm returned rather than sentiment/opinion, which was the original intent.
4. Using OpenAI's gpt-5-mini model to generate titles for each topic using the key words representing each topic.
5. Creating app and interactive visualization in Streamlit.
