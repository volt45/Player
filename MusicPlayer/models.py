from django.db import models


class Album(models.Model):
    Name = models.CharField(max_length=250)
    ImageAlbum = models.ImageField()
    DateReleased = models.DateField()

    def __str__(self):
        return self.Name


class Music(models.Model):
    Url = models.URLField()
    Name = models.CharField(max_length=250)
    Autor = models.CharField(max_length=250)
    Duration = models.IntegerField()
    DateReleased = models.DateField()
    Album = models.ManyToManyField(Album, default=None, blank=True)

    def __str__(self):
        return self.Name


class User(models.Model):
    FirstName = models.CharField(max_length=150)
    LastName = models.CharField(max_length=150)
    Login = models.CharField(max_length=250)
    Password = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.EmailField()
    DateBirth = models.DateField()
