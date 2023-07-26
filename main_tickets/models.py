#DB creation
from django.db import models
from django.utils import timezone

#User table
class User(models.Model):
    #Just for testing
    #The next atributes are here to make the login possible
    #once finished the username and pwd are from another DB
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    type = models.IntegerField()
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


#Lacation table, Ticket(location <------- Location)    
class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

#Ticket Table
class Ticket(models.Model):
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    lvl_priority = models.IntegerField()
    date = models.DateField(default=timezone.now)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    detail = models.CharField(max_length=600)
    detail_feedback = models.CharField(max_length=600, default='null', editable=True)

    def __str__(self):
        return self.lvl_priority