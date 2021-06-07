from hood.models import Mtaa
from django.contrib import admin
from .models import Mtaa, Business, Post, Essential

# Register your models here.

admin.site.register(Mtaa)
admin.site.register(Post)
admin.site.register(Essential)
admin.site.register(Business)