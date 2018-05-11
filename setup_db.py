import sqlite3
import pandas as pd
import json as json

con = sqlite3.connect("db.sqlite3")

movies = pd.read_csv("movies_final.csv")

movies.to_sql("server_movies",con, if_exists='replace', index=False)

credits = pd.read_csv("final_credits.csv")

credits.to_sql("server_credits", con, if_exists='replace', index=False)