from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
import os

class BaseModel(models.Model):
  create_at = models.DateTimeField()
  update_at = models.DateTimeField()
  
  class Meta:
    abstract = True
    
    
class Foods(BaseModel):
  name = models.CharField(max_length=255)
  expirydate = models.DateField()
  quantity = models.IntegerField()
  
  class Meta:
    db_table = 'foods'
    
  def get_absolute_url(self):
    return reverse_lazy("food:detail_food", kwargs={"pk": self.pk})
  
  
class PicturesManager(models.Manager):
  def filter_by_food(self, food):
    return self.filter(food=food).all()
  
  
class Pictures(BaseModel):
  
  picture = models.FileField(upload_to="picture/")
  food = models.ForeignKey(
    "foods", on_delete=models.CASCADE
  )
  objects = PicturesManager()
  
  
@receiver(models.signals.post_delete, sender=Pictures)
def delete_picture(sender, instance, **kwargs):
  if instance.picture:
    if os.path.isfile(instance.picture.path):
      os.remove(instance.picture.path)
