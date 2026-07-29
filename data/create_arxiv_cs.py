import pandas as pd

input_file = r"C:\Users\siddu\OneDrive\Documents\Desktop\Research_Paper_Expert_Chatbot\data\arxiv-metadata-oai-snapshot.json"
output_file = r"C:\Users\siddu\OneDrive\Documents\Desktop\Research_Paper_Expert_Chatbot\data\arxiv_cs.csv"

chunksize = 10000
first_chunk = True
total = 0

print("Reading dataset...")

for chunk in pd.read_json(input_file, lines=True, chunksize=chunksize):

    cs = chunk[chunk["categories"].str.contains("cs.", na=False)]

    cs = cs[["title", "abstract"]]

    cs = cs.rename(columns={"abstract": "summary"})

    cs.to_csv(
        output_file,
        mode="w" if first_chunk else "a",
        header=first_chunk,
        index=False
    )

    total += len(cs)
    first_chunk = False

    print(f"Saved {total} Computer Science papers...")

print("\nDone!")
print("Total CS Papers:", total)