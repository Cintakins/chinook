from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from localhost "chinook" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for artist table
artist_table = Table(
    "Artist", meta, 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# variable for "table" 
album_table  = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GengreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Making the connection
with db.connect() as connection:

    # query1 - select all artists from the artist table
    # select_query = artist_table.select()

    # query2 - select only the name from artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # query3 - only select queen from artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - select artists from artistId 51
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - select only albums with artistId 51
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # query 6 - select all tracks where composer is queen from track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)

    for result in results:
        print(result)