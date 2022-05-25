from unicodedata import category
from django.db.models.signals import m2m_changed
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import *
from .models import *
from django.template.loader import *

@receiver(m2m_changed, sender=PostCategory)
def post(sender, instance, *args, **kwargs):
    for category in instance.postCategory.all():
        for subscriber in category.subscribers.filter():
            msg = EmailMultiAlternatives(
            subject=instance.title,
            body=instance.text,
            from_email='',
            to=[User.objects.get(pk=subscriber.id).email],
            )
            html_content = render_to_string(
                'subletter.html',
                {
                    'instance': instance,
                    'user': subscriber,
                    'category': category,
                }
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()