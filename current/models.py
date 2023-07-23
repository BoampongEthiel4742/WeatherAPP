from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
  
       
    class Meta:
        verbose_name_plural = 'cities'
        ordering = ['-created']


