from django.db import models

class Complaint(models.Model):
    id = models.AutoField(primary_key=True)
    issue=models.CharField(max_length=50)
    report=models.TextField()
    prove=models.ImageField()
    location=models.CharField(max_length=200)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)+" "+self.issue
    


