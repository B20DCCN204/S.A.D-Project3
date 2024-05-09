from django.db import models

class Cart(models.Model):
    user_id = models.BigIntegerField()
    quantity = models.IntegerField()
    product_type = models.CharField(max_length=255)
    product_id = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


