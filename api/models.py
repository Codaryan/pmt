from django.db import models
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

class Project(models.Model):   
    project_name         = models.CharField(max_length=100)
    client_project       = models.ForeignKey(Client,on_delete=models.CASCADE,related_name='projects',null=True,blank=True)
    client_name  = models.CharField(max_length=50,null=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    created_by   = models.CharField(max_length=50)

class ProjectUser(models.Model):
    # id        = models.IntegerField(primary_key=True,null=False)
    user_name = models.CharField(max_length=100,null=True)
    project_users = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='users',null=True,blank=True) 

