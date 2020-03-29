from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, WebPage

# Create your views here.
def index(request):
    my_dict = {'myname': 'Fatih'}
    return render(request, 'first_app/index.html', context=my_dict)

def fatih(request):
    return render(request, 'first_app/fatih.html')


def access(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index_level_two.html', context=date_dict)
