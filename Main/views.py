from django.shortcuts import render
from django.shortcuts import redirect
from .forms import PostForm
import http
from django.contrib import messages
from django.utils import timezone
from django.core.validators import EmailValidator
from django.shortcuts import render
from .models import message

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Date = timezone.now()
            post.save()
            messages.success(request, 'Message Sent Successfully')
            return redirect('/')
    else:
        form = PostForm()
    msg = message.objects.all().order_by('Date').reverse()
    if len(msg)>=5:
       msg=msg[:5]
    return render(request, 'home.html', {'form': form,"msg":msg })




