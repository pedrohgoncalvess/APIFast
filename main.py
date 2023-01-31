from fastapi import FastAPI, Body, Depends
from database import Base,SessionLocal,engine
from sqlalchemy.orm import Session
import schemas
import models
from schemas import Item

Base.metadata.create_all(engine)

def getSession():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

bigam = FastAPI()

@bigam.get("/")
def getItems(session: Session = Depends(getSession)):
    items = session.query(models.Item).all()
    return items

@bigam.get("/{id}")
def getItem(id:int,session: Session = Depends(getSession)):
    item = session.query(models.Item).get(id)
    return item

@bigam.post("/")
def addItem(item:schemas.Item, session: Session = Depends(getSession)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@bigam.put("/{id}")
def updateItem(id:int,item:schemas.Item, session: Session = Depends(getSession)):
    itemobj = session.query(models.Item).get(id)
    itemobj.task = item.task
    session.commit()
    return itemobj


@bigam.delete("/{id}")
def updateItem(id:int, session: Session = Depends(getSession)):
    itemobj = session.query(models.Item).get(id)
    session.delete(itemobj)
    session.commit()
    return "Task has been deleted."

#@app.post("/")
#def addItemBody(body = Body()):
#    newId = len(fakeDataBase.keys())+1
#    fakeDataBase[newId] = {'task':body['task']}
#    return fakeDataBase