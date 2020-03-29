from django.shortcuts import render
from . import forms  # . means current directory

# Create your views here.

def index(request):
    return render(request, 'basicApp/index.html')


def form_page_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print("validation Success")
            print("Name:", form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Text:', form.cleaned_data['text'])
            
    return render(request, 'basicApp/form_page.html', {'form': form})
