from django.db import models


# Create your models here.

class UserRatingStar(models.Model):
    rating = models.ForeignKey('star_rating.Rating', on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.rating:
            self.rating = star_ratings.Rating.objects.create()
        super(Post, self).save(*args, **kwargs)
