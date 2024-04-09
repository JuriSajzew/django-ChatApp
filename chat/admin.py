from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('created_ad', 'author', 'text', 'receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)
