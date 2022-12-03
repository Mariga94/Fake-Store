#!/usr/bin/python3
# from models import storage
from models.product_category import ProductCategory

# all_objs = storage.all()
# print("-- Reloaded objects --")
# for obj_id in all_objs.keys():
#     obj = all_objs[obj_id]
#     print(obj)
#Create sofa category
sofas = ProductCategory()
sofas.name = "Sofas"
sofas.description = "Our Sofas are designed and made of high quality material"
sofas.save()

beds = ProductCategory()
beds.name = "Beds"
beds.description = "Our bed are made of high quality mahogany wood or red-wood oak"
beds.save()

#Create
office = ProductCategory()
office.name = "Tv Stands"
office.description = "Our Furniture are made of high quality red-oak and mahogamy desks"
office.save()