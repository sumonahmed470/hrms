from django.db import models


# Create your models here.

class Position(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_of_joining = models.DateField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]
    )
    
    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')],
        default='Pending'
    )
    
    def __str__(self):
        return f"{self.employee} - {self.status}"                