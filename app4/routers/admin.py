# routers/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from pydantic import BaseModel
from typing import Optional, Union

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models
class SiteBase(BaseModel):
    name: str
    url: str
    filename: str

class SiteCreate(SiteBase):
    pass

class SiteUpdate(SiteBase):
    pass


@router.delete("/sites/{site_id}")
def delete_site(site_id: int, db: Session = Depends(get_db)):
    site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if not site:
        return {'status_code': 400, 'detail': "Site not found"}

    db.delete(site)
    db.commit()
    return {'status_code': 200, 'detail': 'Site update'}

@router.put("/sites/{site_id}")
def update_site(site_id: int, site: SiteUpdate, db: Session = Depends(get_db)):
    db_site = db.query(models.Site).filter(models.Site.id == site_id).first()
    if not db_site:
        return {'status_code': 400, 'detail': "Site not found"}

    for key, value in site.dict().items():
        setattr(db_site, key, value)

    db.commit()
    db.refresh(db_site)
    return {'status_code': 200, 'detail': 'Site update'}


# CRUD operations for Sites
@router.post("/sites/")
def create_site(site: SiteCreate, db: Session = Depends(get_db)):
    if site.dict()['url'] == '':
        return {'status_code': 400, 'detail': "Url must be empty"}
    if site.dict()['name'] == '':
        return {'status_code': 400, 'detail': "Name must be empty"}
    if site.dict()['filename'] == '':
        site.dict()['filename'] = f'{site.dict()["name"]}.xml'
    db_site = models.Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return {'status_code': 200, 'detail': 'Site created'}


@router.get("/sites/")
def read_sites(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Site).offset(skip).limit(limit).all()


@router.get("/site/{site_id}")
def read_site(site_id: int, db: Session = Depends(get_db)):
    try:
        site = db.query(models.Site).filter(models.Site.id == site_id).first()
        print(site.id)
        categories = db.query(models.Category).filter(models.Category.site_id == site_id).all()
        print('1')
        for category in categories:

            category.products = db.query(models.Product).filter(models.Product.category_id == category.id).all()
            print('2')
            category.descriptions = db.query(models.Description).filter(models.Description.category_id == category.id).all()
            print('3')
            try:
                print('4')
                category.parent = db.query(models.Category).filter(models.Category.id == category.parent_id).first()
                print('5')

            except:
                category.parent = {'name': '-'}
                print('6')
        context = {'status_code': 200, "site": site, "categories": categories}
        db.close()
        return context
    except:
        return {'status_code': 400, 'detail': "Site not found"}

# Аналогичные CRUD операции для остальных моделей (Category, Product, Description, TimeMark)
# Реализация аналогична вышеописанной для Sites

class CategoryBase(BaseModel):
    name: str
    parent_id: Union[int, None]
    site_id: int

class CategoryCreate(CategoryBase):
    pass

@router.post("/categories/")
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    print(category.dict())
    if category.dict()['name'] == '':
        return {'status_code': 400, 'detail': "Url must be empty"}
    if category.dict()['parent_id']:
        parent = db.query(models.Category).filter(models.Category.id == category.dict()['parent_id']).first()
        print(parent)
        if not parent:
            return {'status_code': 400, 'detail': "Parent category not found"}
    if category.dict()['site_id']:
        site = db.query(models.Site).filter(models.Site.id == category.dict()['site_id']).first()
        if not site:
            return {'status_code': 400, 'detail': "Site not found"}
    else:
        return {'status_code': 400, 'detail': "Site must be specified"}
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return {'status_code': 200, 'detail': 'Category created'}

@router.get("/categories/")
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Category).offset(skip).limit(limit).all()


class ProductBase(BaseModel):
    name: str
    category_id: int

@router.post("/products/")
def create_product(product: ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/products/")
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Product).offset(skip).limit(limit).all()


class DescriptionBase(BaseModel):
    text: str
    category_id: int

@router.post("/descriptions/")
def create_description(description: DescriptionBase, db: Session = Depends(get_db)):
    db_description = models.Description(**description.dict())
    db.add(db_description)
    db.commit()
    db.refresh(db_description)
    return db_description

@router.get("/descriptions/")
def read_descriptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Description).offset(skip).limit(limit).all()


class TimeMarkBase(BaseModel):
    day_of_week: int
    hour: int
    minute: int
    site_id: int

@router.post("/timemarks/")
def create_timemark(timemark: TimeMarkBase, db: Session = Depends(get_db)):
    db_timemark = models.TimeMark(**timemark.dict())
    db.add(db_timemark)
    db.commit()
    db.refresh(db_timemark)
    return db_timemark

@router.get("/timemarks/")
def read_timemarks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.TimeMark).offset(skip).limit(limit).all()

