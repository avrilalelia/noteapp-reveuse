from django.contrib import admin
from .models import Note, Content

admin.site.site_header = "Note App"
admin.site.site_title = "Note App"
admin.site.index_title = "Welcome to Note Web App"


class contentInLine(admin.TabularInline):
    model = Content
    extra = 3


class NoteAdmin(admin.ModelAdmin):
    fieldsets = [("Title", {'fields': ['note_title']}),
                 ]
    inlines = [contentInLine]


admin.site.register(Note, NoteAdmin)
