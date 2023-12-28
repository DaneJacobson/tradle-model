import pandas as pd

file_path = './data/trade_i_baci_a_92.tsv'
chunk_size = 10000
chunks_2021 = []

for chunk in pd.read_csv(file_path, delimiter='\t', chunksize=chunk_size):
    chunks_2021.append(chunk[chunk['year'] == 2021])

data_2021 = pd.concat(chunks_2021)
data_2021.reset_index()
data_2021.to_csv('./data/hs92-2021.csv', index=False)