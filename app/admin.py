from django.contrib import admin
from .models import UserProfile, Post, Ressource, User


admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Ressource)