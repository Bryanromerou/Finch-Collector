from django.db import models
from django.contrib.auth.models import User

MEALS = (
    ("B", "Breakfast"),
    ("L", "Lunch"),
    ("D", "Dinner"),
)
LOCATIONS = (
    ("F", "Farm"),
    ("H", "House"),
    ("A", "Appartment"),
    ("M", "Mobile Home"),
    ("L", "Homeless"),
)

# ------------------------------------------Toy Model
class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# -----------------------------------------Reptile Model
class Reptile(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()
    toys = models.ManyToManyField(Toy)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# -----------------------------------------Feeding Model
class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length = 1,
        choices = MEALS,
        default = MEALS[0][0]
    )

    reptile = models.ForeignKey(Reptile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'


class Species(models.Model):
    name = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)


class Home(models.Model):
    address = models.CharField(max_length = 100)
    location = models.CharField(
        max_length = 1,
        choices = LOCATIONS,
        default = LOCATIONS[0][0]
    )
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    zipcode = models.CharField(max_length = 100)
    occupants = models.IntegerField()

    reptile = models.OneToOneField(
        Reptile,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    def __str__(self):
        return f'{self.get_location_display()} on {self.address}'

