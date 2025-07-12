from django.contrib import admin
from .models import User, Property, Image, Booking, Review, Amenity

admin.site.register(User)
admin.site.register(Property)
admin.site.register(Image)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Amenity)
