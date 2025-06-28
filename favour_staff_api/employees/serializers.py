from rest_framework import serializers
from .models import Staff

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ('id', 'hire_date', 'created_at', 'updated_at', 'has_company_card')