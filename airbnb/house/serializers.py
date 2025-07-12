from rest_framework import serializers
from .models import User, Property, Image, Booking, Review, Amenity
from django.conf import settings
import joblib
import os

model_path = os.path.join(settings.BASE_DIR, 'model_airbnb.pkl')
vec_path = os.path.join(settings.BASE_DIR, 'vec_airbnb')
model_predict = joblib.load(model_path)
vec = joblib.load(vec_path)

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class BookingSerializer(serializers.ModelSerializer):
    guest = serializers.ReadOnlyField(source='guest.id')

    class Meta:
        model = Booking
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    check_comment = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_check_comment(self, obj):
        return model_predict.predict(vec.transform([obj.comment]))


class PropertySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    images = ImageSerializer(many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    reviews = ReviewSerializer(read_only=True, many=True)

    class Meta:
        model = Property
        fields = '__all__'