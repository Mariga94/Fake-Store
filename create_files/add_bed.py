from models import storage
from models.product import Product

bed_id = "7e46d691-909e-4bc3-b94d-32d72b0a668d"

bed1=Product()
bed1.name = "Half poster bed"
bed1.description = "Half poster bed queen size" 
bed1.category_id = bed_id
bed1.price = 400.00
bed1.image = "https://images.ctfassets.net/q5lwz1whkyct/1omlem4bYSkC08QFuMU5PV/7d9fed73a245df2a82c581b7392ca3a0/17-half-poster-bed.jpg"
bed1.save()

bed2=Product()
bed2.name = "Four poster bed"
bed2.description = "Four posted bed king size" 
bed2.category_id = bed_id
bed2.price = 430.00
bed2.image = "https://images.ctfassets.net/q5lwz1whkyct/11WcbGuzdOm4Gv9uoMNpGv/8e7e075cb88ee7365da1ae0a247217fc/14-four-poster-bed.jpg"
bed2.save()

bed3=Product()
bed3.name = "Waterbed"
bed3.description = "Water bed" 
bed3.category_id = bed_id
bed3.price = 200.00
bed3.image = "https://images.ctfassets.net/q5lwz1whkyct/4KT5ofz84aB8Q3Prl8xTY0/386876f02dec4a0844410ee7511c2903/09-waterbed.jpg"
bed3.save()

bed4=Product()
bed4.name = "Futon Bed"
bed4.description = "Futon bed" 
bed4.category_id = bed_id
bed4.price = 300.00
bed4.image = "https://images.ctfassets.net/q5lwz1whkyct/6CGc8zcu3lKH34aEtYKh33/7126436e385a89fb284c32b312524cd9/08-futon.jpg"
bed4.save()

bed5=Product()
bed5.name = "Day bed"
bed5.description = "Day bed" 
bed5.category_id = bed_id
bed5.price = 350.00
bed5.image = "https://images.ctfassets.net/q5lwz1whkyct/6uBaY2REe6y2r6E7cnYtiE/6e23b9654942a41c8c38bd0cc87b4263/07-daybed.jpg"
bed5.save()

bed6=Product()
bed6.name = "King bed"
bed6.description = "King Bed" 
bed6.category_id = bed_id
bed6.price = 400.00
bed6.image = "https://ibb.co/HTbcrnr"
bed6.save()

bed7=Product()
bed7.name = "Queen Bed"
bed7.description = "Queen Bed" 
bed7.category_id = bed_id
bed7.price = 500.00
bed7.image = "https://ibb.co/ccwjdhD"
bed7.save()

