from django.db import models
from django.core.validators import MinValueValidator
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='%(class)s_created_by')
    updated_by = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='%(class)s_updated_by')
    class Meta:
        abstract = True

class Product(BaseModel):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    image_url = models.URLField()

    def __str__(self):
        return self.name

class ImageType(BaseModel):
    TYPE_CHOICES = (
        ('square', 'Square'),
        ('wide', 'Wide'),
        ('portrait', 'Portrait'),
    )
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='square')
    width = models.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2) 
    height = models.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2)
    aspect_ratio = models.CharField(max_length=10)    

class ImageVarient(BaseModel):
    type = models.ForeignKey(ImageType, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    LICENSE_CHOICES = (
        ('personal', 'Personal'),
        ('commercial', 'Commercial'),
    )
    license = models.CharField(max_length=10, choices=LICENSE_CHOICES, default='personal')
    
class Order(BaseModel):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_varient = models.ForeignKey(ImageVarient, on_delete=models.CASCADE)
    razorpay_order_id = models.TextField()
    razorpay_payment_id = models.TextField()
    amount =  models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    STATUS_CHOICES =(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')            
    download_url = models.URLField()
    preview_url = models.URLField()
