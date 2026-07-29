import pandas as pd

def load_arxiv_data():
    df = pd.read_csv("data/arxiv_cs_small.csv")

    df = df.dropna()

    df = df[["title", "summary"]]

    return df