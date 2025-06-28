from rest_framework import serializers
from .models import StaffBase, Manager, Intern, Address

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '__all__'
        read_only_fields = ('id', 'hire_date', 'created_at', 'updated_at')

class ManagerSerializer(StaffBaseSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class InternSerializer(StaffBaseSerializer):
    class Meta:
        model = Intern
        fields = '__all__'
        read_only_fields = ('mentor',)

class AddressSerializer(StaffBaseSerializer):
    class Meta:
        model = Address
        fields = '__all__'

