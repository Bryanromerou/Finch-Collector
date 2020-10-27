from django.db import models

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

class Reptile(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

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


