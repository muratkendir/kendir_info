from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    duty = models.CharField(max_length=255, default="surveyor")
    mission = models.CharField(max_length=255, blank = True)
    year = models.DateField(help_text = "The year I quit/finished work.", blank = True, default="2024-01-01")
    location = models.CharField(max_length=255, blank = True)

    def __str__(self):
        key_string = self.duty + '-' + self.year.strftime('%Y')
        return key_string

    def only_year(self):
        return self.year.strftime('%Y')

    class Meta:
       ordering = ["-year"]
