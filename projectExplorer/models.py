from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## Member model
class Member(models.Model):
    first_name      = models.CharField(max_length = 200)
    last_name       = models.CharField(max_length = 200)
    email           = models.CharField(max_length = 200)
    status          = models.CharField(max_length = 8)          ## ACTIVE, INACTIVE, ALUMNI
    graduating_year = models.IntegerField()

    ## Auth object
    auth_user       = models.OneToOneField(User, on_delete = models.CASCADE)

## Project Manager model
class ProjectManager(models.Model):
    member          = models.OneToOneField('Member', on_delete = models.CASCADE)

## Web Admin model

## Community Partner model

## Project Model
class Project(models.Model):
    status          = models.CharField(max_length = 10)         ## ACTIVE, COMPLETED, INACTIVE, PROPOSAL
    draft_status    = models.BooleanField()

    ## Meta information
    project_title   = models.CharField(max_length = 200)
    project_summary = models.CharField(max_length = 500)
    project_notes   = models.CharField(max_length = 1000, blank = True)
    project_leader  = models.ForeignKey('ProjectManager', on_delete = models.CASCADE)
