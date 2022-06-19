from base import clean_stations, engine
from stations import stations, engine as station_engine

conn = engine.connect()

result = conn.execute(clean_stations.select())
stations_conn = station_engine.connect()
for row in result:
    ins = stations.insert().values(row)    
    stations_conn.execute(ins)

print(result)
