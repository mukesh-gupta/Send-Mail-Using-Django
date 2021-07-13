from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail
from email.mime.image import MIMEImage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import os
from pathlib import Path
from .models import profile
from .forms import ComposeForm
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives

def email_compose(request):
    forms=ComposeForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
       forms.save()
       return redirect('list')
    context = {
        'forms': forms
    }
    return render(request,'profile.html',context=context)

def mail_list(request):
    sub = profile.objects.all()
    for i in sub:
        pass

    info = profile.objects.filter(email=i.email)
    return render(request, 'list.html', {'info':info})


def mail_detail(request,id):
    info=get_object_or_404(profile,id=id)
    body_html = render_to_string('detail.html',{'info':info})
    html_content = strip_tags(body_html)
    to_email = info.email
    msg = EmailMultiAlternatives(
        info.name,
        html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email])

    msg.attach_alternative(body_html, "text/html")
    msg.mixed_subtype = 'related'

    a = '/media/' + str(info.image)
    b = a.split('/')
    with open('D://django-pro//Notification/' + a, 'rb') as p:
        msg_img = MIMEImage(p.read())
        p.close()
        msg_img.add_header('Content-ID', '<{}>'.format(a))
        msg_img.add_header('Content-Disposition', 'inline', filename=b[3])
        msg.attach(msg_img)

    msg.send()
    return HttpResponse('<h3>Single info sent to your mail please check your mail !</h3>')


def mail_bulk(request):
    sub = profile.objects.all()
    for i in sub:
        pass

    info = profile.objects.filter(email=i.email)
    context = {'info': info}

    body_html = render_to_string('all_mail.html',context=context)
    html_content=strip_tags(body_html)
    to_email = i.email
    msg = EmailMultiAlternatives(
        i.name,
        html_content,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_email])

    msg.attach_alternative(body_html, "text/html")

    msg.mixed_subtype = 'related'
    for f in info:
        a='/media/'+str(f.image)
        b=a.split('/')
        with open('D://django-pro//Notification/'+a,'rb') as p:
            print(p)
            msg_img = MIMEImage(p.read())
            p.close()
            msg_img.add_header('Content-ID', '<{}>'.format(a))
            msg_img.add_header('Content-Disposition', 'inline', filename=b[3])
            msg.attach(msg_img)

    msg.send()
    return HttpResponse('<h3>All info sent to your mail please check your mail !</h3>')
