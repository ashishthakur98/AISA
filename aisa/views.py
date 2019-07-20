from django.shortcuts import render

class Study(models.Model):
    study_title = models.CharField(max_length=200)
    study_content = models.TextField()
    study_published = models.DateTimeField('date published')

    def __str__(self):
        return self.tutorial_title

