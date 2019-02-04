from django.db import models


class Subscriber(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    city = models.ForeignKey('common.City', verbose_name='City', related_name='subscribers', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MailType(models.Model):
    code = models.CharField(max_length=10, verbose_name='Code', primary_key=True)

    def __str__(self):
        return self.code


class MailTemplate(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    body = models.TextField(verbose_name='Body')
    mail_type = models.OneToOneField(MailType, verbose_name='Mail Type', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
