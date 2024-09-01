from django.db import models
from product.models import Product
from account.models import User
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(blank=True,null=True)

    def get_total_price(self):
        total_price = 0
        for item in self.cartitem_set.all():
            total_price += item.amount * item.product.price
        return total_price
        
class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    price = models.IntegerField(null=True,blank=True)
