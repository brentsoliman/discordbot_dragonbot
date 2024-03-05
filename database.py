from sqlalchemy import create_engine,update
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from statistics import mean
from uuid import uuid4
import creds



from sqlalchemy import ForeignKey, Column, String, Integer, CHAR, TIMESTAMP,Float,func,text,cast, Numeric
import datetime

import psycopg2

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column("id",Integer,primary_key=True)
    discord_id = Column("discord_id", String)
    first_name = Column("first_name",String)
    
    def __init__(self, discord_id,first_name):
        self.discord_id = discord_id
        self.first_name = first_name
        
        
class Mile(Base):
    __tablename__ = "miles"
    
    id = Column("id",Integer,primary_key=True)
    discord_id = Column("discord_id", String)
    distance = Column("distance",Float)
    created_at = Column("created_at",TIMESTAMP,default=datetime.date.today())
    
    def __init__(self,discord_id, distance,created_at):
        self.discord_id = discord_id
        self.distance = distance
        self.created_at = created_at
        
engine = create_engine(f'postgresql+psycopg2://postgres:{creds.password}@localhost:3331/postgres')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)

session = Session()
def user_entry(discord_id,first_name):
    query_data = session.query(User).filter(User.discord_id == str(discord_id)).first()
    
    if not query_data:
        print("If none: "+ str(query_data))
        session.add(User(discord_id,first_name))
        session.commit()    
        return True
    else:
        print("Already in the db:" + str(query_data))
        print(query_data)

        return False
    
def distance_entry(discord_id,distance,created_at):
    session.add(Mile(discord_id,distance,created_at))
    session.commit()
    
def getFirstName(discord_id):
    query_data = session.query(User).filter(User.discord_id == str(discord_id)).first()
    
    if not query_data:
        return query_data
    else:
        return query_data.first_name
    
def getListRanking():
# Define subquery
    weekly_miles_subquery = session.query(Mile.discord_id, func.round(cast(func.sum(Mile.distance), Numeric),2).label('total_distance')) \
        .filter(
            text("EXTRACT(WEEK FROM created_at) = EXTRACT(WEEK FROM CURRENT_DATE) AND EXTRACT(YEAR FROM created_at) = EXTRACT(YEAR FROM CURRENT_DATE)")
        ) \
        .group_by(Mile.discord_id) \
        .order_by(func.sum(Mile.distance)) \
        .subquery()

    # Use the subquery in the outer query
    result = session.query(User.first_name, weekly_miles_subquery.c.total_distance) \
        .join(weekly_miles_subquery, User.discord_id == weekly_miles_subquery.c.discord_id).distinct() \
        .distinct() \
        .order_by(weekly_miles_subquery.c.total_distance.desc()) \
        .all()
    return result

def getListRankingAllTime():
    subquery = session.query(Mile.discord_id,func.round(cast(func.sum(Mile.distance), Numeric),2).label("total_distance")) \
    .group_by(Mile.discord_id) \
    .subquery()

    data = session.query(User.first_name, subquery.c.total_distance) \
    .join(User, User.discord_id == subquery.c.discord_id) \
    .distinct() \
    .order_by(subquery.c.total_distance.desc()).all()
    return data

def getMostRecentUpload():
    mileData = session.query(Mile).order_by(Mile.created_at.desc()).first()
    timeDataString = mileData.created_at.strftime("(%B-%d-%y %I:%M %p)")
    
    userData = session.query(User).filter(User.discord_id == mileData.discord_id).first()
    return f"{timeDataString} {userData.first_name}: +{mileData.distance} miles"
    