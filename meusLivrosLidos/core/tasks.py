from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from celery import shared_task

#https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/

@shared_task
def send_mail_template(subject, template_name, context, recipient_list,
                       from_email=settings.DEFAULT_FROM_EMAIL,
                       fail_silently=False, attachments=None):

    message_html = render_to_string(template_name, context)

    message_txt = striptags(message_html)

    email = EmailMultiAlternatives(
        subject=subject, body=message_txt, from_email=from_email, 
        to=recipient_list
    )    
    email.attach_alternative(message_html, "text/html")
    if attachments is not None:
        email.attach_file(attachments[1])
    email.send(fail_silently=fail_silently)