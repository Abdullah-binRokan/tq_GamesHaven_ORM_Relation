from django.db import models

# Create your models here.

# create category model -- many to many relationship
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):

    class RatingChoices(models.IntegerChoices):
        STAR1 = 1, "One Star"
        STAR2 = 2, "Two Stars"
        STAR3 = 3, "Three Stars"
        STAR4 = 4, "Four Stars"
        STAR5 = 5, "Five Stars"

    title = models.CharField(max_length=1024)
    description = models.TextField()
    publisher = models.CharField(max_length=256)
    rating = models.SmallIntegerField(choices=RatingChoices.choices)
    release_date = models.DateField()
    poster = models.ImageField(upload_to="images/", default="images/default.jpg")
    # link the Game with Category model -- many to many relationship
    categories = models.ManyToManyField(Category)

    # defines the string representation of an instance of a model using dunder function
    def __str__(self) -> str:
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    comment = models.TextField()
    rating = models.SmallIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # defines the string representation of an instance of a model using dunder function
    def __str__(self) -> str:
        return f"{self.name} on {self.game.title}"
