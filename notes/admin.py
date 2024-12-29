from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.
from .models import Note, Tag, List, Relationship

admin.site.register(Note, MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Relationship)
admin.site.register(List)