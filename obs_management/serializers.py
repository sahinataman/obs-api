from .models import Management
from rest_framework import serializers

class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management 
        fields = ('url', 'user', 'degree', 'm_type','phone','fax','address','gender','department')
