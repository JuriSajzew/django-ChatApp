from django.shortcuts import render
from .models import Chat, Message

# Create your views here.
def index(request):
    if request.method == "POST":
        print("Received data " + request.POST['textmessage']) # mit dem request.POST wird die Nachricht aus dem Input Feld aus dem HTML Teil rausgegeben
        Message.objects.create(text=request.POST['textmessage'], chat=None, author=request.user, receiver=request.user)
    
    return render(request, 'chat/index.html') #hiermit wird die Seite neu gerendert