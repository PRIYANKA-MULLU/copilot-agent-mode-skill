# backend/octofit_tracker/models.py

from djongo import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    date = models.DateField()

class Activity(models.Model):
    name = models.CharField(max_length=100)
    calories_burned_per_min = models.FloatField()

class LeaderboardEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
