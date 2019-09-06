from django.db import models

class fireoffice(models.Model):
    id=models.AutoField(primary_key=True)
    headoffice=models.CharField(max_length=45)
    fireoffice=models.CharField(max_length=45)
    center=models.CharField(max_length=45)
    address=models.CharField(max_length=100)
    number=models.CharField(max_length=20)

    def __str__(self):
        return self.title
    
