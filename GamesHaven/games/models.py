from django.db import models

# Create your models here.

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


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)