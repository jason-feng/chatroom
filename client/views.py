from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from .models import Message, MessageForm
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.

@login_required
def chatroom(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            new_message = form.save(commit=False)
            new_message.date = datetime.datetime.now()
            new_message.username = request.user.username
            new_message.save()
            return HttpResponseRedirect('/chat/')

    # if a GET (or any other method) we'll create a blank form
    form = MessageForm()
    messages = Message.objects.all().order_by('date')
    context = {'messages': messages}
    return render(request, 'client/index.html', {'form': form, 'context': context})
