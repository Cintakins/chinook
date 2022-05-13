from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing instructions from the chinook database
db = create_engine("postgresql:///chinook")

base = declarative_base()

# create class based model for programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

# create a new instance of sessionmake and point to our engine
Session = sessionmaker(db)

session = Session()

# creating database using declarative_base subclass
base.metadata.create_all(db)

# creating records on the pragrammer table
ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovalace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)
alun_turing = Programmer(
    first_name = "Alun",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL language"
)

margeret_hamilton = Programmer(
    first_name = "Margeret",
    last_name = "Hamilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "Britich",
    famous_for = "World Wide Web"
)
# add each instance of programmers to session
# session.add(ada_lovelace)
# session.add(alun_turing)
# session.add(grace_hopper)
# session.add(bill_gates)
# session.add(margeret_hamilton)
# session.add(tim_berners_lee)

# commit session to the database
session.commit()

# query database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )