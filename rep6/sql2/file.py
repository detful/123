import csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Float, String, ForeignKey, Date
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

metadata = MetaData()

stations = Table('stations', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('station_name', String),
                 Column('latitude', Float),
                 Column('longitude', Float),
                 Column('elevation', Float))

measurements = Table('measurements', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('station_id', Integer, ForeignKey('stations.id')),
                     Column('date', Date),
                     Column('precip', Float),
                     Column('temp_max', Float),
                     Column('temp_min', Float))

engine = create_engine('sqlite:///weather_data.db', echo=True)
metadata.create_all(engine)

def load_csv_data(engine, table, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        data_to_insert = []
        for row in csv_reader:
            if 'date' in row and row['date']:
                try:
                    row['date'] = datetime.strptime(row['date'], '%Y-%m-%d').date()
                except ValueError:
                    row['date'] = None  
            data_to_insert.append(row)
        
        conn = engine.connect()
        trans = conn.begin()
        try:
            conn.execute(table.insert(), data_to_insert)
            trans.commit()
        except SQLAlchemyError as e:
            print(f"Error occurred: {e}")
            trans.rollback()
        finally:
            conn.close()

if __name__ == '__main__':
    try:
        load_csv_data(engine, stations, 'clean_stations.csv')
        load_csv_data(engine, measurements, 'clean_measure.csv')
        print("Data successfully loaded.")
    except Exception as e:
        print(f"An error occurred: {e}")

    with engine.connect() as connection:
        result = connection.execute("SELECT * FROM stations LIMIT 5").fetchall()
        print(result)
