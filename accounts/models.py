from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )

RATING_CHOICES = ((1, 1),
                  (2, 2),
                  (3, 3),
                  (4, 4),
                  (5, 5))


class Review(models.Model):
    author = User
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    street = models.CharField(max_length=100, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    description = models.TextField(null=True, blank=True)
    importance = models.BooleanField(default=False)
    longitude = models.FloatField()
    latitude = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('-created_date',)

    def str(self):
        return '{} by {}'.format(self.title, self.author)
