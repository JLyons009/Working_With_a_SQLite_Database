import sqlite3
import pandas as pd
import math

conn = sqlite3.connect('factbook.db')

query = 'SELECT * FROM facts'
facts = pd.read_sql_query(query, conn)
conn.close()

facts.dropna(axis=0)

def pop_final(row):
    return row['population'] * math.exp((row['population_growth']/100)*35)

facts['final_population'] = facts.apply(pop_final, axis=1)

print(facts[['name', 'population', 'population_growth', 'final_population']].head(10))