from django.shortcuts import render
from django.http import HttpResponse
from App_1.models import Topic, Webpage, AccessRecord
from . import forms

# Create your views here.
# def index(request):
    # my_dict = {'insert_me':"Hello I am from views.py"}
    # return render(request, 'App_1/index.html', context=my_dict)

def help(keanu):
    k_dict = {'image':'image incoming '}
    return render(keanu, 'App_1/page2.html', context=k_dict)

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpage_list}
    return render(request, 'App_1/index.html', context=date_dict)
    
def knowledge_view(request):
    form_1 = forms.Form_1()

    if request.method == 'POST':
        form_1 = forms.Form_1(request.POST) 

        if form_1.is_valid():
            print("VALIDATION SUCCESS ")
            print("NAME = " + form_1.cleaned_data['name'])
            print("EMAIL = "+ form_1.cleaned_data['email'])
            print("Text = " + form_1.cleaned_data['text'])
            



    for_form = {'form':form_1}
    return render (request, 'App_1/form_page.html', context=for_form)
    # return render (request, 'App_1/form_page.html', {'form':form})


