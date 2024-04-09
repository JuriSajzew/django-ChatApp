from datetime import date
from django.conf import settings
from django.db import models



# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_ad = models.DateField(default=date.today)
    #chat = muss noch zugewiesen werden
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
        
    
    