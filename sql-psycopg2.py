import psycopg2

# connect to chinook
connection = psycopg2.connect(database="chinook")

# build a curser object for the database
cursor = connection.cursor()

# query 1 - select all records from the artist table
# cursor.execute('SELECT * FROM "Artist"')

# query 2 - select only name collumn from artist table
# cursor.execute('SELECT "Name" FROM "Artist"')

# query 3 - select only Queen from artist table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# query4 - select artist id 51 from artist 
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# query 5 - select select albums with artistId 51 on the album
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

#  test query for dresden dolls
cursor.execute('SELECT * FROM "Arstist" WHERE "Name" = %s', ["The Dresden Dolls"])

# query 6 - select all tracks where composer is Queen
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# fetch results (multiple)
results = cursor.fetchall()

# fetch the result (single)
# results = curser.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)