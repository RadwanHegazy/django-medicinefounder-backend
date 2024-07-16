from rest_framework import serializers
from users.models import User
from ..models import Medicine

class MedicineSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Medicine
        fields = ('name','img',)

    def validate(self, attrs):
        attrs['user'] = self.context['user']
        return attrs
    
    def to_representation(self, instance:Medicine):
        data = super().to_representation(instance)
        data['user'] = {
            'pharmcy_name' : instance.user.pharmcy_name,
            'whatsapp' : instance.user.whats_app_number,
        }
        return data