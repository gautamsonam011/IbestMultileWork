from fastapi import FastAPI,Depends
from db import engine,SessionLocal
from model import Books, Base
from sqlalchemy.orm import Session
from pydantic import BaseModel
Base.metadata.create_all(bind = engine)
app = FastAPI()

  
def get_db():
    db = SessionLocal()
    try:    
        yield db 
    finally:
        db.close()
   
class BookSchema(BaseModel):
    name:str
    author:str
    publisher:str
    class Config:
        orm_mode =True
    
        
# @app.get("/books",response_model=[BookSchema])
@app.post("/books")
def get_books(request: BookSchema, db:Session = Depends(get_db)):
    query = {"name": request.name,"author": request.author,"publisher": request.publisher}
    b = Books(**query)
    db.add(b)
    db.commit()
    return b

@app.get("/books")
def get_books(db:Session = Depends(get_db)):
    data = db.query(Books).all()
    return data

@app.get("/books{id}")
def get_book(id:int, db:Session = Depends(get_db)):
    a = db.query(Books).filter(Books.id == id).first()
    return a

@app.put('/books/{id}', response_model=Books)
def update_book(id:int,        db: Session = Depends(get_db)):
   b1 = db.query(Books).filter(Books.id == id).first()
   b1.id=Books.id
   b1.author=Books.author
   b1.publisher=Books.publisher
   db.commit()
   return db.query(Books).filter(Books.id == id).first()

# @app.put('/books')
# def update_book(id:int,db: Session = Depends(get_db)):
#    b1 = db.query(Books).filter(Books.id == id).first()
# #    b1.id=Books.id
#    b1.name=Books.name
#    b1.publisher=Books.publisher
#    db.commit()
#    return db.query(Books).filter(Books.id == id).first()

@app.delete('/books')
def del_book(id:int, db: Session = Depends(get_db)):
   try:
      db.query(Books).filter(Books.id == id).delete()
      db.commit()
   except Exception as e:
      raise Exception(e)
   return {"delete status": "success"}




# @app.get('/')
# def hey():
#     return {'message':'Hello'}

# @app.get('/')
# async def root():
#     return {'message':'Hello World'}
