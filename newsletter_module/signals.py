from django.db.models.signals import post_save
from books_module.models import Books
from account_module.models import Subscriber
from django.dispatch import receiver
from utils.email_service import send_email


@receiver(post_save, sender=Books)
def book_added(sender, instance, created, **kwargs):
    if created:
        subscribers = list(Subscriber.objects.all())
        for email in subscribers:
            send_email('رویابوک', email, {'new_book': instance}, 'emails/newsletter.html')
