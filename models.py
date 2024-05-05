from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()

    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    question_text = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text