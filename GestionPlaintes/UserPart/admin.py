from django.contrib import admin
from .models import Subject, Problem, Keyword


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('id','nom', 'date', 'email', 'etat', 'subject', 'importance')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Problem, ProblemAdmin)
