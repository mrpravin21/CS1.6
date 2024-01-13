from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data["full_name"]
            phone = form.cleaned_data["phone_num"]
            national_id = form.cleaned_data["national_id"]
            email = form.cleaned_data["email_id"]
            password = form.cleaned_data["password"]


            Form.objects.create(full_name=full_name, phone=phone,
                                national_id=national_id, email=email, password=password)

            message_body = f"A new user have been submitted. Thank you, \n{full_name}"
            email_message = EmailMessage("User Registration Completed!", message_body, to=[email])
            email_message.send()

            messages.success(request, "User Registered Successfully!")

    return render(request, "register.html")
