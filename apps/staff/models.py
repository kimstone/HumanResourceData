from django.db import models


class Dependent(models.Model):
    RELATIONSHIP_CHOICES = [
        ('child', 'Child'),
        ('husband', 'Husband'),
        ('wife', 'Wife'),
    ]
    # id = models.AutoField()
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mission = models.CharField(max_length=500)
    relationship = models.CharField(max_length=70, choices=RELATIONSHIP_CHOICES, blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Department(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=200)
    mission = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length=200)
    min_salary = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    max_salary = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title