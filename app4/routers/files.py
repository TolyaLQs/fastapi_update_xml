# routers/files.py
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import shutil
import os
from lxml import etree as ET
from routers.admin import get_db
from sqlalchemy.orm import Session
from models import Site, Category, Product, Description
import itertools

router = APIRouter()

UPLOAD_DIR = "uploads"
OUTPUT_DIR = "output"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def update_file(tree, site, db):
    error_site = {'site_name': site.name,
                  'check_error': False,
                  'products_error': [],
                  }
    products_error = []
    root = tree.getroot()
    categories = db.query(Category).filter(Category.site_id == site.id).all()
    products_dict = {}
    for category in categories:
        products = db.query(Product).filter(Product.category_id == category.id).all()
        for product in products:
            products_dict[product.name] = category.id
    for shop in root:
        for element in shop:
            if element.tag == 'categories':
                while len(element) > 0:
                    element.remove(element[0])
                for category in categories:
                    if category.parent_id is None:
                        cat = ET.SubElement(element, 'category', id=str(category.id))
                        cat.text = category.name
                    else:
                        cat = ET.SubElement(element, 'category', id=str(category.id), parentId=str(category.parent_id))
                        cat.text = category.name
            #             ET.CDATA()
            if element.tag == 'offers':
                for offers in element:
                    offer_id = offers.attrib['id']
                    category_id = None
                    offer_error = False
                    offer_name = ''
                    for offer in offers:
                        if offer.tag == 'name':
                            offer_name = offer.text
                            for key, value in products_dict.items():
                                if key in offer.text:
                                    category_id = value
                        if offer.tag == 'categoryId':
                            if category_id is not None:
                                offer.text = str(category_id)
                            else:
                                offer.text = ''
                                offer_error = True
                        if offer.tag == 'description':
                            if offer.text is not None:
                                offer.text = ET.CDATA(offer.text)
                    if offer_name == '':
                        offer_error = True
                    context = {'offer_id': offer_id, 'offer_name': offer_name, 'offer_error': offer_error}
                    products_error.append(context)
    error_site['products_error'] = products_error
    if len(products_error) > 0:
        error_site['check_error'] = True

    return tree, error_site


def open_file(file_path):
    with open(file_path, "r", encoding='utf-8') as f:
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(source=f, parser=parser)
        f.close()
    return tree


@router.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            buffer.close()
        sites = db.query(Site).all()
        report_list = []
        if len(sites) == 0:
            return {'status_code': 400, 'detail': 'Site not found'}
        if len(sites) > 1:
            for site in sites:
                tree = open_file(file_path)
                otvet, error = update_file(tree, site, db)
                report_list.append(error)
                file_save_path = OUTPUT_DIR+'/'+site.filename
                otvet.write(file_save_path, encoding='utf-8')
        else:
            tree = open_file(file_path)
            otvet, error = update_file(tree, sites, db)
            report_list.append(error)
            file_save_path = OUTPUT_DIR + '/' + sites.filename
            otvet.write(file_save_path, encoding='utf-8')
        return {"filename": file.filename, "size": os.path.getsize(file_path), 'report': report_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


