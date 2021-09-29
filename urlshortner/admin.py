from django.contrib import admin
from urlshortner.models import Url
# Register your models here.

class UrlAdmin(admin.ModelAdmin):
    list_display = ('original_name', 'short_name', 'count_open', 'created')

admin.site.register(Url, UrlAdmin)