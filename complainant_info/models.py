from django.db import models

class Complainant_Info(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=20)
    nid=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+" "+self.name
    

    
