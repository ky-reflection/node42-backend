from rest_framework import serializers
from .models import CustomUser
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('uuid', 'username','date_joined' )