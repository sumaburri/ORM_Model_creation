from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField(default='suma@gmail.com')
    def __str__(self):
        return self.topic_name
    

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    team=models.CharField(max_length=100,default='team_india')

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    match=models.CharField(max_length=100,default='ipl')

    def __str__(self):
        return self.author