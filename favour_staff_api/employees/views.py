from rest_framework import viewsets
from .models import employees 
from .serializers import EmployeeSerializer
from django.http import HttpResponse
from django.urls import reverse


def home_view(request):
    admin_url = reverse('admin:index')
    api_url = '/api/'
    html = f"""
    <h1>Welcome to the Staff Management API</h1>
    <ul>
        <li><a href="{admin_url}">Go to Admin</a></li>
        <li><a href="{api_url}">Go to API</a></li>
    </ul>
    """
    return HttpResponse(html)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = employees.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

