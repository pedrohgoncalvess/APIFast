from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from environments import environmentsVariables as env

engine = create_engine(url=f"postgresql://{env('user')}:{env('password')}@{env('host_name')}/postgre")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine,expire_on_commit=False)

