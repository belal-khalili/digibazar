from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=13)
    text = models.TextField()
    admin_response = models.TextField()
    created = models.DateTimeField(auto_created=True)

    # class Meta:
    #     verbose_name = 'تماس با ما'
    #     verbose_name_plural = 'تماس با ما'