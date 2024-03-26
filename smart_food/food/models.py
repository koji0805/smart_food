from django.db import models
from django.urls import reverse_lazy


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
  