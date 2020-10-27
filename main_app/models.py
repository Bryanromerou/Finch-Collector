from django.db import models

# class Reptile:
#     def __init__(self, name , species , breed, color, age = 0):
#         self.name = name
#         self.species = species
#         self.breed = breed
#         self.color = color
#         self.age = age
#         self.img = ""
class Reptile(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

# reptiles = [
#     Reptile("Peter Parker", "Turtle" ,"Sulacda", "Brown", 1),
#     Reptile("Ramona Flowers", "Turtle" ,"Sulacda", "Black", 1),
#     Reptile("Biden", "Chameleons" ,"Veiled", "All", 1),
#     Reptile("Daisy", "Snake" ,"Emerald Tree Boa", "Green", 1),
# ]