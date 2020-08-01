from django.shortcuts import render
from .models import TitanicData
from django.http import Http404
from .machine_learning import load_ml_model

# Create your views here.
def home_view(request):
    return render(request, 'home/home.html')


def form_value_load(request):
    obj = TitanicData()
    if request.POST.get('age') != "":
        obj.age = request.POST.get('age')
    if request.POST.get('cabin') != "":
        obj.cabin_no = request.POST.get('cabin')
    if request.POST.get('ticket') != "":
        obj.ticket_no = request.POST.get('ticket')
    if request.POST.get('name') != "":
        obj.name = request.POST.get('name')
    if request.POST.get('sex') != "":
        obj.sex = request.POST.get('sex')
    if request.POST.get('siblings') != "":
        obj.siblings = request.POST.get('siblings')
    if request.POST.get('pclass') != "":
        obj.pclass = request.POST.get('pclass')
    if request.POST.get('fare') != "":
        obj.fare = request.POST.get('fare')
    if request.POST.get('embarked') != "":
        obj.embarked = request.POST.get('embarked')
    if request.POST.get('parch') != "":
        obj.parch = request.POST.get('parch')

    return obj



def predict_view(request):
    survived = 0
    if request.method == "POST":
        data = form_value_load(request)
        survived = load_ml_model(data)
        data.survived = survived
        data.save()
        return render(request, 'home/home.html', {"survived" : survived, "visible": "d-block"})
    else:
        raise Http404

def predicted_list_view(request):
    obj = TitanicData.objects.all()
    return render(request, 'home/predicted.html', {"obj": obj})
