from django.shortcuts import render
from .forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register_view(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()


            profile = profile_form.save(commit=False)
            profile.user = user


            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/register.html',
                        {'user_form': user_form,
                            'profile_form': profile_form,
                                'registered': registered})



def user_login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('my_page'))

            else:
                return HttpResponse("Account is not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login")

    else:
        return render(request, 'basic_app/login.html',{})

@login_required
def my_page_view(request):
    return render(request, 'basic_app/my_page.html',{'user':request.user})
