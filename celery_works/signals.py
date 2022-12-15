from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from company_app.models import Job


@receiver(post_save, sender=Job)
def save_notification(sender, instance, created, **kwargs):  
    if created:
        print(sender, instance, created)
        print(**kwargs)

        # user  = User.objects.get(username = instance)
        # notification = 'Appointment booked on ' + str(instance.Date) 
        # UserNotification.objects.create(user=user, notification=notification)
