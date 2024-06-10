from django.db import models

# Create your models here.
class Contact(models.Model):
    subject = models.CharField(max_length=150)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    phone_number = models.CharField(max_length=13)
    text = models.TextField()
    admin_response = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.subject} / {self.full_name} / {self.created.date()}'
    # class Meta:
    #     verbose_name = 'تماس با ما'
    #     verbose_name_plural = 'تماس با ما'