from celery import shared_task
from django.core.mail import message, send_mail
from job_portal_project import settings


@shared_task(bind = True)
def send_registration_mail(self, to_mail):
    mail_subject = 'HI WELCOME ...'
    message = 'Hi welcome to JOBRIAL'
    #to_mail = '12vishnuks@gmail.com'

    send_mail(subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_mail,],
        fail_silently=False,
        ) 
        
    return 'Mail sent successfully...'


@shared_task(bind = True)
def beat_test(self):       
    return 'Mail sent successfully...'