import pandas as pd

df = pd.read_csv(r"C:\Users\siddu\OneDrive\Documents\Desktop\Research_Paper_Expert_Chatbot\data\arxiv_cs.csv")

print("Original:", len(df))

df = df.sample(frac=1, random_state=42)

df = df.head(15000)

df.to_csv(r"C:\Users\siddu\OneDrive\Documents\Desktop\Research_Paper_Expert_Chatbot\data\arxiv_cs_small.csv", index=False)

print("Saved:", len(df))