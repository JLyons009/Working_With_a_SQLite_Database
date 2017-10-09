import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')

land_q = 'SELECT SUM(area_land) FROM facts'
area_land = pd.read_sql_query(land_q, conn)

water_q = 'SELECT SUM(area_water) FROM facts'
area_water = pd.read_sql_query(water_q, conn)

conn.close()

land = int(area_land['SUM(area_land)'])
water = int(area_water['SUM(area_water)'])
ratio = land/water
print("Land: {0}\nWater: {1}\nRatio: {2}".format(land, water, ratio))