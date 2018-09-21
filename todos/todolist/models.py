from django.db import models

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=50,blank=False,null=False)
    content =models.TextField(null=False,blank=False,default='This is the default content')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title