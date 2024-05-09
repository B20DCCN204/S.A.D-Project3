from djongo import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "mobile_type"

    def __str__(self):
        return self.name


class Mobile(models.Model):
    image = models.ImageField(upload_to="mobile_images/", blank=True, null=True)
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    type = models.ForeignKey(to=Type, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    price = models.BigIntegerField()

    class Meta:
        db_table = "mobile"

    def __str__(self):
        return self.name
