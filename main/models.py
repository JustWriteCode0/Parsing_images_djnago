from django.db import models


class Url(models.Model):
    UsedURL = models.URLField(max_length=150)

    def __str__(self):
        return self.UsedURL

