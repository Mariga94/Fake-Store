from models import storage
from models.product import Product

tv_stand = "7b57e6a8-8310-4e94-a394-140459f41df2"

stand1 = Product()
stand1.name = "Brown Tv stand"
stand1.description = "Brown Tv stand"
stand1.category_id = tv_stand
stand1.price = 400.00
stand1.image = "https://img.freepik.com/free-photo/wall-mockup-with-cabinet-tv-white-color-wall-background-3d-rendering_41470-4113.jpg?size=626&ext=jpg&uid=R32916755&ga=GA1.2.1443394923.1670036113&semt=sph",
stand1.save()

stand2 = Product()
stand2.name = "Light Brown Tv Stand"
stand2.description = "Light Brown Tv Stand"
stand2.category_id = tv_stand
stand2.image ="https://img.freepik.com/free-photo/modern-wooden-commode-tv-mockup-empty-room-with-green-wall-3d-rendering_41470-4337.jpg?size=626&ext=jpg&uid=R32916755&ga=GA1.2.1443394923.1670036113&semt=sph"
stand2.price = 350.00
stand2.save()
