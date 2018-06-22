from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import EmailSignupForm
from .models import *
# Create your views here.
def SmallEngineClassView(request):
    smallengineclass_list = SmallEngineClass.objects.filter(session_1_date__gte = timezone.now())
    # If this is a POST request then process the Form data
    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.class_updates = True
            student.save()
            messages.success(request, 'Form submission successful.  You will now receive email updates on new classes.')
    else:
        form = EmailSignupForm()

    return render(
        request,
        'classes.html',
        context={'smallengineclass_list':smallengineclass_list,'form':form,}
    )

def Unsubscribe(request, email):
    student = Student.objects.get(email=email)
    student.class_updates = False
    student.save()
    return render(
    request,
    'unsubscribe.html',
    {'email':email}
    )

@login_required
def UpdateEmailList(request):
    subscribers = Student.objects.filter(class_updates=True)
    return render(
    request,
    'update_email_list.html',
    {'subscribers':subscribers}
    )
