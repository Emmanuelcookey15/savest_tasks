from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps


# Create your views here.

User = apps.get_model('users', 'User')


def send_email(request):
    if request.method == 'POST':
        email_body = request.POST.get("email")

        if email_body is not None:
            email_list_dict = list(User.objects.values('email').filter(is_active=True))

            email_list = []

            for i in email_list_dict:
                email = i.get('email')
                email_list.append(email)


            send_mail('Subject goes here', email_body, 'no-reply@authapplciation.com', email_list, fail_silently=False)
            return HttpResponse("Mail Sent to the following active accounts: " + ", ".join(email_list))


    return render(request, 'admin/users/send_email.html')
