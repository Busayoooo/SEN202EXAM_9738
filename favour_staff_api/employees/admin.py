from django.contrib import admin
from .models import StaffBase, Manager, Intern, Address

admin.site.register(Manager)
admin.site.register(Intern)
admin.site.register(Address)
