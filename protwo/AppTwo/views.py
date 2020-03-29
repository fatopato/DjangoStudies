from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, 'AppTwo/index.html')

def help(request):
    req_dict = {'app_name': 'AppTwo', 'company_name': 'Fatopato Co.'}
    return render(request, 'AppTwo/help.html', context=req_dict)

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context=user_dict)

def signup(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("INVALID FORM")

    return render(request, 'AppTwo/signup.html', {'form':form})
