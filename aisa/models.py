from django.db import models

class Study(models.Model):
      study_tittle = models.Charfield(max_length=150)
      study_content = models.TextField()
      study_published = models.DateTimeField('date published')
      
      
      def __str__(self):
        return self.study_tittle
  
