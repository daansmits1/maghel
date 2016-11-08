# -*- coding: utf-8 -*-

import pandas as pd 

columns = ["id", "title", "year", "ratings", "votes", "length", "genres"]
data = pd.read_csv('imdb_top_10000.txt', sep='\t', names=columns, index_col=0)

data['formatted_title'] = data['title'].str[:-7]
data['formatted_length'] = data['length'].str[:-6].astype('int')

# print(data.head)
print(data.formatted_length)


data.to_csv('imdb_top_10000_cleaned.csv', header=True, sep=',')