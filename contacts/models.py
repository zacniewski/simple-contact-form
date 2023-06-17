from django.db import models
from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    APP_SUPPORT = 'App support'
    PAYMENT_SUPPORT = 'Payment support'
    HR_JOBS = 'HR/Jobs'
    OTHER = 'other'
    SUBJECT = [
        (APP_SUPPORT, _('App support')),
        (PAYMENT_SUPPORT, _('Payment support')),
        (HR_JOBS, _('HR/Jobs')),
        (OTHER, _('Other'))
    ]

    NEW = 'New'
    IN_PROGRESS = 'In progress'
    RESOLVED = 'Resolved'
    STATUS = [
        (NEW, _('New')),
        (IN_PROGRESS, _('In progress')),
        (RESOLVED, _('Resolved')),
    ]

    name = models.CharField(null=False, max_length=50)
    email = models.EmailField(max_length=255, validators=[EmailValidator])
    subject = models.CharField(max_length=255, choices=SUBJECT)
    message = models.TextField(null=False, max_length=500)
    status = models.CharField(max_length=255, choices=STATUS)

    def __str__(self):
        return f"{self.name}"
