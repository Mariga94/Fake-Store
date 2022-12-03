from models import storage
from models.product import Product
sofa_id = "c20ea509-2f1d-42d3-a9ba-ea901abdd012"

sofa1 = Product()
sofa1.name= "Green Fabric sofa"
sofa1.image = "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8c29mYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
sofa1.description = "Green 3 seater fabric sofa made from high quality material"
sofa1.category_id = sofa_id
sofa1.price = 200.00
sofa1.save()

sofa2 = Product()
sofa2.name= "Beig leather sofa"
sofa2.image =  "https://images.unsplash.com/photo-1540574163026-643ea20ade25?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8c29mYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
sofa2.description= "Beige brown 3 seater leather sofa"
sofa2.category_id = sofa_id
sofa2.price = 350.00
sofa2.save()

sofa3 = Product()
sofa3.name= "Blue fabric loveseat"
sofa3.image = "https://images.unsplash.com/photo-1484101403633-562f891dc89a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8c29mYXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60"
sofa3.description= "Blue fabric loveseat made from high quality material",
sofa3.category_id = sofa_id
sofa3.price = 250.00
sofa3.save()

sofa4 = Product()
sofa4.name= "Beige leather sofa"
sofa4.image = "https://images.unsplash.com/photo-1512212621149-107ffe572d2f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fHNvZmF8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60"
sofa4.description= "Beige leather sofa",
sofa4.category_id = sofa_id
sofa4.price = 165.00
sofa4.save()

sofa5 = Product()
sofa5.name = "3 Seater Grey padded Chair"
sofa5.description = "3 Seater Grey padded Chair"
sofa5.category_id = sofa_id
sofa5.image = "https://images.unsplash.com/photo-1573866926487-a1865558a9cf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fHNvZmF8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
sofa5.price = 400.00
sofa5.save()

sofa6 = Product()
sofa6.name = "Brown leather chesterfield sofa"
sofa6.description = "Brown leather chesterfield sofa",
sofa6.image = "https://images.unsplash.com/photo-1573866926487-a1865558a9cf?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTZ8fHNvZmF8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60",
sofa6.category_id = sofa_id
sofa6.price = 400.00
sofa6.save()