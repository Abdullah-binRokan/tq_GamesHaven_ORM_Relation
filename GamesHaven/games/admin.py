from django.contrib import admin
from .models import Game, Review

# Register your models here.
# define custome admin configuration for Game model
class GameAdmin(admin.ModelAdmin):
    # specify the fields to display in the list veiw of the admin interface
    list_display = ("title", "publisher", "rating")
    list_filter = ("rating",)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "game", "rating")
    list_filter = ("game", "rating")

# register the models with the custom GameAdmin & ReviewAdmin configuration.
admin.site.register(Game, GameAdmin)
admin.site.register(Review, ReviewAdmin)