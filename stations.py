from sqlalchemy import Table, Column, Integer, String, create_engine, MetaData


engine = create_engine('sqlite:///stations.db')

meta = MetaData()

stations = Table(
   'stations', meta,
   Column('station', String),
   Column('latitude', Integer), 
   Column('longitude', Integer),
   Column('elevation', Integer),
   Column('name', String),
   Column('country', String),
   Column('state', String)
)
meta.create_all(engine)
print(engine.table_names())
