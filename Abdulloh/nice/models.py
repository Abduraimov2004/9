from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  # Store the icon class name

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(upload_to='team/')

