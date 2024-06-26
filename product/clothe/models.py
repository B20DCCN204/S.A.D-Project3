from djongo import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "clothe_type"

    def __str__(self):
        return self.name


class Clothe(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="clothe_images/", blank=True, null=True)
    brand = models.CharField(max_length=50)
    type = models.ForeignKey(to=Type, null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.BigIntegerField()

    class Meta:
        db_table = "clothe"

    def __str__(self):
        return self.name
