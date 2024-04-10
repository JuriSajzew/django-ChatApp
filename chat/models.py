from datetime import date
from django.conf import settings
from django.db import models



# Create your models here.
class Chat(models.Model):
    created_ad=models.DateField(default=date.today)

class Message(models.Model):
    text = models.CharField(max_length=500)
    created_ad = models.DateField(default=date.today)
    #chat = muss noch zugewiesen werden
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='chat_message_set', default=None, null=True, blank=True) 
                                                                                            #default=None=>Standartwert ist 0
                                                                                                #null=True=>Die Datenbank akzeptiert 0
                                                                                                    #blank=True=>erlaubt das das Feld leer bleiben soll
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_message_set')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver_message_set')
        
    
    