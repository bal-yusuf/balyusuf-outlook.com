from django.db import models


# Create your models here.

class Settings(models.Model):
    STATUS = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(blank=True, max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    company = models.CharField(blank=True, max_length=255)
    address = models.CharField(blank=True, max_length=255)
    fax = models.CharField(blank=True, max_length=255)
    email = models.CharField(blank=True, max_length=255)
    smtpserver = models.CharField(blank=True, max_length=255)
    smtpemail = models.CharField(blank=True, max_length=255)
    smtppassword = models.CharField(blank=True, max_length=255)
    smtpport = models.CharField(blank=True, max_length=255)
    facebook = models.CharField(blank=True, max_length=255)
    instagram = models.CharField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    about_us = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
