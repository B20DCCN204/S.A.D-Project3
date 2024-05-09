from djongo import models


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200, unique=True)
    mail = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

    class Meta:
        db_table = "publishers"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="book_images/", blank=True, null=True)
    price = models.BigIntegerField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.title
