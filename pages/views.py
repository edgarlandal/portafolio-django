from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .form import ContactForm

# Create your views here.


def home(request):
    return render(request, "pages/about.html")


def contact(request):
    print("hola")
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Should send email")

            name = form.cleaned_data["name"]
            message = form.cleaned_data["messege"]
            email_from = form.cleaned_data["email"]

            html = render_to_string("pages/email.html", request.POST)

            send_mail(
                "Message from " + name,
                message,
                email_from,
                ["miguellanda33@gmail.com"],
                html_message=html
            )

            return redirect("home")
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})
