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
        parser = ET.XMLParser(strip_cdata=False, encoding="utf-8")
        tree = ET.parse(source=f, parser=parser)

        f.close()
    return tree


def update_file(tree):
    i=0
    root = tree.getroot()
    for shop in root.iter():
        for element in shop.iter():
            if element.tag == 'categories':
                print(len(element))
                while len(element) > 0:
                    element.remove(element[0])
                    i += 1
                    print(i)


    return tree


def save_file(file_name, tree):
    pass


def main():
    file_name = 'dealer.xml'
    save_name = 'dealer_update.xml'
    tree = open_file(file_name)
    tree = update_file(tree)
    tree.write(save_name, encoding='utf-8')
    # save_file(file_name, tree)


if __name__ == '__main__':
    main()

