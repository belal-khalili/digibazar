from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=13)
    text = models.TextField()
    admin_response = models.TextField(null=True,blank=True)
    response_sent = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='contact',null=True,blank=True)
    
    def __str__(self) -> str:
        return f'{self.full_name} ({self.subject}) - {self.created.date()}'
    # class Meta:
    #     verbose_name = 'تماس با ما'
    #     verbose_name_plural = 'تماس با ما'

@receiver(pre_save, sender=Contact) 
def save_profile(sender, instance, **kwargs):
        print(instance.email)
        if instance.response_sent == False:
            # send email to user
            print(instance.admin_response)
            instance.response_sent = True
            instance.save()