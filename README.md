Data originally from https://www.kaggle.com/datasets/pavellexyr/the-reddit-climate-change-dataset?resource=download

This app requires Streamlit, pandas, and Altair, which you can download with 
```bash
pip install streamlit pandas altair
```

You will also have to download the Reddit post data and topic data, which are too large to attach to the GitHub repository. You can download them here and move them to the repository manually. A Python script that automates this is in progress. Ensure that the name of the data folder remains "data" after downloading.

You can then run the app with
```bash
streamlit run app.py
```

Also in progress is a demo video if you want to see how the project works without downloading the files.

### Process (which you can see in the Jupyter Notebook):
1. Dealing with original dataset. Keeping only relevant columns, combining titles and datasets, later on taking a sample of 100k posts out of the original 600k+ for faster computation.