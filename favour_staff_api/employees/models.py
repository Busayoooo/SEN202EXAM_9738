from django.db import models

class StaffBase(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def get_role(self):
        return "Staff"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)
    team_size = models.PositiveIntegerField(default=0)

    def get_role(self):
        return "Manager"

    def __str__(self):
        return f"{self.department} {self.has_company_card} {self.team_size} {self.first_name} {self.last_name} (Manager)"
    
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='interns')
    internship_end_date = models.DateField()

    def get_role(self):
        return "Intern"

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Intern)"
    
class Address(models.Model):
    employee = models.ForeignKey(StaffBase, on_delete=models.CASCADE, related_name='addresses')
    street1_address = models.CharField(max_length=255)
    street2_address = models.CharField(max_length=255, blank=True)
    house_number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street1_address}, {self.house_number}, {self.city}"
