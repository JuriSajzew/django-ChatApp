from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat', 'created_ad', 'author')
    list_display = ('created_ad', 'author', 'text', 'receiver')
    search_fields = ('text',)

# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)
