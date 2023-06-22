from django.db import models

# Create your models here.
class Speakers(models.Model):
    sp_id=models.AutoField(),
    sp_name=models.TextField(max_length=20),
    sp_telephone=models.BigIntegerField(max_length=10),
    
    def __str__(self) -> str:
        return f"name: {self.sp_name}, mobile: {self.sp_telephone}"
    class Meta:
        db_table="speaker"

