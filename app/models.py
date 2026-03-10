from django.db import models

class Task_Db(models.Model):
    task = models.CharField(max_length=200)
    desc = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Added for your template

    def __str__(self):
        return self.task

class History_Db(models.Model):
    task = models.CharField(max_length=200)
    desc = models.TextField()
    deleted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task