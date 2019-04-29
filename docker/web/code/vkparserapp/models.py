from django.db import models



class User(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    # составной индекс
    class Meta:
        index_together = ["first_name", "last_name"]




