from django.db import models



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
