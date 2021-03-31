from django.contrib import admin

# Register your models here.
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'published')


admin.site.register(Tutorial, TutorialAdmin)