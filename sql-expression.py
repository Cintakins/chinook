from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Making the connection
with db.connect() as connection: