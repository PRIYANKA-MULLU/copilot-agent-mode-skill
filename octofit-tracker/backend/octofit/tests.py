from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser3', email='test3@example.com', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2025-06-06')
        self.assertEqual(activity.activity_type, 'run')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser4', email='test4@example.com', password='testpass')
        team = Team.objects.create(name='Test Team 2')
        team.members.add(user)
        leaderboard = Leaderboard.objects.create(team=team, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        User = get_user_model()
        user = User.objects.create_user(username='testuser5', email='test5@example.com', password='testpass')
        workout = Workout.objects.create(name='Pushups', description='Do 20 pushups')
        workout.suggested_for.add(user)
        self.assertIn(user, workout.suggested_for.all())
