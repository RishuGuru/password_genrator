from rest_framework import serializers
from genrator.models import Contact

class contactserializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields ='__all__'


