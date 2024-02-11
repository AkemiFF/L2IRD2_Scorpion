from django.contrib import admin
from .models import Subject, Problem, Keyword

admin.site.register(Problem)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(Keyword, KeywordAdmin)
