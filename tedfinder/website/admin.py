from django.contrib import admin
from website.models import *

@admin.register(Document)
class PostingRelation(admin.ModelAdmin):
    search_fields = ('user__first__name', 'user__last_name', 'user__username', 'title', 'date',)
