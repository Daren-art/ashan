from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = 'Category'
        ordering = ['name']
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_product")
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="ashan_images/")
    raiting = models.FloatField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_product")
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    class Status(models.TextField):
        STATUS_CHOICES = [("pending", "Pending"),("confirmed","Confirmed"),("cancelled","Cancelled")]
    status = models.CharField(max_length=20, choices=Status.STATUS_CHOICES, default='pending')
