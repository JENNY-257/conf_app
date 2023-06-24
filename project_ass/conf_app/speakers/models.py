from django.db import models

# Create your models here.
class Speakers(models.Model):
    sp_id=models.CharField(max_length=20),
    sp_name=models.TextField(max_length=20),
    sp_email=models.EmailField()
    sp_contact=models.CharField(max_length=10),
    
    def __str__(self) :
        return "%s " %(self.sp_name)
    class Meta:
        db_table="speaker"

