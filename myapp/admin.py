from django.contrib import admin
from .models import Publication, Article, Reporter, Place, PrintingPress, User
# Register your models here.

admin.site.register(Publication)
admin.site.register(Article)
admin.site.register(Reporter)
admin.site.register(User)
admin.site.register(Place)
admin.site.register(PrintingPress)