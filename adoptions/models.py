from django.db import models

class Pet(models.Model):
    """Lists pets and their attributes"""
    SEX_CHOICES = [('M',  'Male'), ('F', 'Female'), ('T', 'Transgender')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    submission_date = models.DateTimeField()
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        """returns the name of the vaccine"""
        return self.name
