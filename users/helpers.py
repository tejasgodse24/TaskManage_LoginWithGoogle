
from django.contrib.sites.models import Site
from django.conf import settings
from django.core.mail import send_mail

def set_site_id(domain_name):
    try:
        site = Site.objects.get(domain = domain_name)
        settings.SITE_ID = site.id
        print(settings.SITE_ID)
        return True
    except Exception as e:
        settings.SITE_ID = 1
        print(e)
        return False
    
def send_invite_email(to_email):
    subject = 'Invite For Task Management Console registration'
    email_from = settings.EMAIL_HOST_USER   
    message = f'Hi, click on the link to register your account http://127.0.0.1:8000/'
    send_mail(subject , message , email_from , [to_email])
