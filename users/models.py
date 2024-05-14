from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name = models.CharField(verbose_name='Fullname', max_length=100)
    username = models.CharField(verbose_name='Username', max_length=100, null=True)
    user_id = models.BigIntegerField(verbose_name='Telegram_id', unique=True, default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=100, decimal_places=0)
    description = models.TextField()
    photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Example of creating a product without subcategory
# product = Product.objects.create(
#     name='Example Product',
#     price=10.99,
#     description='Example description',
#     photo=['https://www.example.com/image1.jpg', 'https://www.example.com/image2.jpg'],
#     category='GM'
# )
