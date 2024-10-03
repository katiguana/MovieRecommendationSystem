import pandas as pd

movie_data=pd.read_csv('./tmdb_5000_movies.csv').dropna(axis=0)
print(movie_data.columns)


