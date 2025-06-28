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
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

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
