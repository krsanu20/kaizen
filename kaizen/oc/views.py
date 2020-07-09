from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader
from oc.forms import CustomerForm,StudentForm
from django.core.mail import send_mail
from kaizen import settings
# Create your views here.
def index(request):
    template = loader.get_template('index.html')  # getting our template
    return HttpResponse(template.render())
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def login(request):
    return render(request,'login.html')
def register(request):
    context={}
    form=StudentForm(request.POST)
    if form.is_valid():
        subject=" has registerd on kaizen.Please check database for full information"
        name=form.cleaned_data['name']
        subject=name+subject
        res=send_mail("Registration",subject,settings.EMAIL_HOST_USER,['kaizenonlineclasses@gmail.com'])
        form.save()
        return HttpResponse("Thanks for registering yourself.We Will get back to you soon")
    context['form']=form
    return render(request,"register.html",context)



def contact(request):
    context = {}
    form = CustomerForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['description']
        phone=form.cleaned_data['phone_no']
        subject=subject+phone
        from_email = form.cleaned_data['email']
        name = form.cleaned_data['name']
        res = send_mail(name, subject, settings.EMAIL_HOST_USER, [from_email])
        form.save()
        return HttpResponse("we will get back to you soon")
    context['form'] = form
    return render(request, "contact.html", context)
