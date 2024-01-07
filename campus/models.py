from django.db import models

# Create your models here.

class Report(models.Model):
    title = models.CharField(max_length=1000, blank=True)
    report = models.TextField(blank=True)
    report_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class AdminReport(models.Model):
    title = models.CharField(max_length=1000, blank=True)
    report = models.TextField(blank=True)
    report_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    fullname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    dov = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.fullname

class Vehicle(models.Model):
    veh_model = models.CharField(max_length=100, blank=True)
    number = models.CharField(max_length=100, blank=True)
    veh_color = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.veh_model