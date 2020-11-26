from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy

from django import forms
from .forms import UserRegistrationForm

from .motor import turnMotor
from .constants import Constants

import logging
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def feed(request):
    if (request.user == None or not request.user.is_authenticated):
        logger.info("User not logged in attempted to feed")
        return HttpResponseRedirect(reverse_lazy('login'))

    if request.method == 'POST':
        turnMotor(Constants.DEFAULT_MOTOR_TURN)
        return HttpResponseRedirect(reverse_lazy('fed'))
    else:
        logger.info("User sent get request to feed")
        return HttpResponseRedirect(reverse_lazy('index'))

def fed(request):
    # TODO: feed history page
    return render(request, 'fed.html', {})

def register(request):
    # ensure that logged in users cannot see this page
    if request.user != None and request.user.is_authenticated:
        logger.info("Signed in user hit register")

        # TODO: notify the user that he cannot access that page when logged in
        return HttpResponseRedirect(reverse_lazy('index'))

    if request.method == 'POST':
        # create and save a new username
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']

            logger.info("attempting to create new user with email " + email)

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)

                user = authenticate(username = username, password = password)

                login(request, user)

                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                raise forms.ValidationError('Looks like that username is already in use')
    else:
        # render the page with the form to sign up
        form = UserRegistrationForm()

    # only hit this if either of the else cases are hit
    return render(request, 'register.html', {'form' : form})

def userPage(request, user_id):
    logger.info("getting user for id " + user_id)
    user = get_object_or_404(User, pk=user_id)

    return render(request, 'user.html', {'pageUser': user})
