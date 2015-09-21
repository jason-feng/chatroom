from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Message
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def chatroom(request):
    messages = Message.objects.order_by('date')
    context = {'messages': messages}
    return render(request, 'client/index.html', context)
