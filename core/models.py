from django.db import models

from userAuth.models import User

from shortuuid.django_fields import ShortUUIDField
from taggit.managers import TaggableManager

from django.utils.html import mark_safe

STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

# Create your models here.

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=100, default="Food")
    image = models.ImageField(upload_to="category", default="category.jpg")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width=50 height=50 />' % (self.image.url))
    
    def __str__(self) -> str:
        return self.title
    
class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix="ven", alphabet="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default="Lobos")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")

    description = models.TextField(null=True, blank=True, default="I'm a vendor")

    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    address = models.CharField(max_length=100, default="123 main street.")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width=50 height=50 />' % (self.image.url))
    
    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefgh12345")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="category")
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="products")

    tags = TaggableManager(blank=True)


    title = models.CharField(max_length=100, default="Fresh produce")
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    #? description = models.TextField(null=True, blank=True, default="This is a product")
    description = models.TextField(null=True, blank=True, default="This is a product")


    price = models.DecimalField(max_digits=999999, decimal_places=2, default="1.99")
    old_price = models.DecimalField(max_digits=999999, decimal_places=2, default="2.99")

    specifications = models.TextField(null=True, blank=True)

    product_status = models.CharField(choices=STATUS ,max_length=20, default="in-review")

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-updated', '-created']

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['-date', '-updated']

    def product_image(self):
        return mark_safe('<img src="%s" width=50 height=50 />' % (self.image.url))
    
    def get_percentage(self):
        new_percentage = (self.price / self.old_price) * 100
        return new_percentage
    
    def __str__(self) -> str:
        return self.title
    
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images", default="product.jpg")
    product = models.ForeignKey(Product, related_name="p_images" ,on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"