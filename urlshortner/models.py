from django.db import models
from urlshortner.utils import create_random_string
from django.core.validators import URLValidator


class Url(models.Model):
    short_name = models.CharField(max_length=10, unique=True, blank=True)
    original_name = models.URLField(validators=[URLValidator])
    created = models.DateTimeField(auto_now_add=True)
    count_open = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.original_name}'

    def save(self, *args, **kwargs):
        if not self.short_name:
            self.create_short_url()
        super().save(*args, **kwargs)

    def create_short_url(self):
        self.short_name = create_random_string(10)
        if Url.objects.filter(short_name=self.short_name).exists():
            self.create_short_url()
        


