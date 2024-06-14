from django.db import models

# Create your models here.
class Booking(models.Model):
    #booking id is automatically created in models
    booking_name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.booking_name

class Menu(models.Model):
    #menu id is automatically created in models
    menu_item = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.menu_item}: {str(self.price)}'