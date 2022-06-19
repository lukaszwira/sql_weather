from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine

engine = create_engine('sqlite:///weather.db', echo=True)

meta = MetaData()

clean_stations = Table(
   'clean_stations', meta,
   Column('station', String),
   Column('latitude', Integer), 
   Column('longitude', Integer),
   Column('elevation', Integer),
   Column('name', String),
   Column('country', String),
   Column('state', String)
)

clean_measure = Table(
   'clean_measure', meta,
   Column('station', String),
   Column('date', String),
   Column('precip', String),
   Column('tobs', String)
)

meta.create_all(engine)
print(engine.table_names())
