import xml.etree.ElementTree as ET
from fastapi import Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def open_file(file):
    with open(file, "r", encoding='utf-8') as f:
        parser = ET.XMLParser(encoding="utf-8")
        tree = ET.parse(source=f, parser=parser)
        root = tree.getroot()
        f.close()
    return root


def update_file(root):
    print(root)
    for shop in root:
        for element in shop:
            if element.tag == 'categories':
                for category in element:
                    print(category)





def main():
    file_name = 'dealer.xml'
    root = open_file(file_name)
    contexts = update_file(root)
    print(contexts)


if __name__ == '__main__':
    main()

