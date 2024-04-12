from django.shortcuts import render
from .models import Chat, Message
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    if request.method == "POST":
        print("Received data " + request.POST['textmessage']) # mit dem request.POST wird die Nachricht aus dem Input Feld aus dem HTML Teil rausgegeben
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], chat=myChat, author=request.user, receiver=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessages}) #hiermit wird die Seite neu gerendert

def logIn(request):
    user = authenticate(username="john", password="secret")
    if user is not None:
    # A backend authenticated the credentials
        ...
    else:
    # No backend authenticated the credentials
        ...