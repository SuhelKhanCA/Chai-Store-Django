from django.db import models
from django.utils import timezone

# Create your models here.

class ChaiVariety(models.Model):
  __tablename__ = "Chai Varieties"
  CHAI_TYPE_CHOICES = [
    ('ML', 'MASALA'),
    ('GR', 'GINGER'),
    ('KL', 'KIWI'),
    ('PL', 'PLAIN'),
    ('EL', 'ELAICHI'),
  ]

  name = models.CharField(max_length=100)
  image = models.ImageField(upload_to='chais/')
  date_added = models.DateTimeField(default=timezone.now)
  type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='ML')
  description = models.TextField(default='')
  price = models.IntegerField(default=20)
  
  def __str__(self):
    return self.name
  
class Review(models.Model):
  review_text = models.TextField()
  rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
  author = models.CharField(max_length=100)

  def __str__(self):
    return self.author + str(self.rating)