from django.contrib import admin

# Register your models here.

from album.models import Team, Player
# Register your models here.

admin.site.register(Team)
admin.site.register(Player)
