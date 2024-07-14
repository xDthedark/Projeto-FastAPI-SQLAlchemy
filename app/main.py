from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List
from fastapi_pagination import Page, add_pagination, paginate
from fastapi_pagination.limit_offset import LimitOffsetPage
from . import models, schemas
from .database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/produtos/", response_model=schemas.Produto)
def create_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    db_produto = models.Produto(**produto.dict())
    try:
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=303,
            detail=f"Já existe um produto cadastrado com o nome: {produto.nome}"
        )
    return db_produto

@app.get("/produtos/", response_model=LimitOffsetPage[schemas.Produto])
def read_produtos(nome: str = None, db: Session = Depends(get_db)):
    query = db.query(models.Produto)
    if nome:
        query = query.filter(models.Produto.nome == nome)
    return paginate(query.all())

@app.get("/produtos/{produto_id}", response_model=schemas.Produto)
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    db_produto = db.query(models.Produto).filter(models.Produto.id == produto_id).first()
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_produto

add_pagination(app)
