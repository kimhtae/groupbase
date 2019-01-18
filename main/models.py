from django.db import models

# Create your models here.
class Fund(models.Model):
    펀드코드 = models.CharField(max_length=5, db_index=True)
    펀드명 = models.CharField(max_length=150, db_index = True)
    펀드설정일 = models.DateTimeField(auto_now=True)
    펀드순자산총액 = models.DecimalField(max_digits=16, decimal_places=2)