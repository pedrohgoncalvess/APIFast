from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(url='postgresql://postgre:fodao002@mkt-gam.co5etbvgqbcw.us-east-1.rds.amazonaws.com/postgre')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)

