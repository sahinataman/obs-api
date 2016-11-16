from .models import Faculty
from rest_framework import serializers

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty  
        fields = ('url', 'faculty_name', 'faculty_code', 'faculty_address','faculty_tel','faculty_fax')
