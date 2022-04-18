from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .models import Profile





def index(request):
    profile = Profile.objects.filter(user=request.user)
    context = {'profile':profile}
    return render(request, 'index.html', context)
