from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def index(request):
    return render(request,'app/index.html')


def portfolioDetail(request,id):
    portfolio=Portfolio.objects.all()
    detail=Portfolio.objects.get(id=portfolio)
    return render(request,'app/index.html',{'detail':detail,'portfolio':portfolio})

from .forms import *

# def add_contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('contact')  # Redirect to a success page
#     else:
#         form = ContactForm()
#     return render(request, 'app/index.html', {'form': form})


from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def contactUs(request):
    contactUs = Contact.objects.all()
    
    if request.method == "POST":
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
      
        contactUs_info = Contact(name=name,
                                   subject=subject,
                                   email=email,
                                   message=message)
        contactUs_info.save()
        
        # Send confirmation email to the user
        user_subject = "Thank you for contacting us"
        user_message = f"Thank you for contacting us.\n" \
                       f"• Name: {name}\n" \
                       f"• subject: {subject}\n" \
                       f"• Email: {email}\n" \
                       f"• Message: {message}"
        user_email_from = settings.EMAIL_HOST_USER
        user_recipient_list = [email]
        send_mail(user_subject, user_message, user_email_from, user_recipient_list)
        
        # Send notification email to the admin
        admin_subject = "New Contact Form Submission"
        admin_message = f"A new contact form has been submitted:\n" \
                        f"• Name: {name}\n" \
                        f"• Subject: {subject}\n" \
                        f"• Email: {email}\n" \
                        f"• Message: {message}"
        admin_email_from = settings.EMAIL_HOST_USER
        admin_recipient_list = ["rmshthapa987@gmail.com"]  # Replace with the admin's email address
        send_mail(admin_subject, admin_message, admin_email_from, admin_recipient_list)
        
        messages.success(request, "Thank you for contacting us. We will get back to you via email.")
    
    return render(request, 'app/index.html', {'contactUs': contactUs})


