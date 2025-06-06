import pymongo
from datetime import date

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]

# Users
users = [
    {"username": "alice", "email": "alice@example.com", "password": "testpass"},
    {"username": "bob", "email": "bob@example.com", "password": "testpass"},
    {"username": "carol", "email": "carol@example.com", "password": "testpass"},
]
user_ids = db.users.insert_many(users).inserted_ids

# Teams
teams = [
    {"name": "Team Alpha", "members": [user_ids[0], user_ids[1]]},
    {"name": "Team Beta", "members": [user_ids[2]]},
]
team_ids = db.teams.insert_many(teams).inserted_ids

# Activities
activities = [
    {"user": user_ids[0], "activity_type": "run", "duration": 30, "date": str(date(2025, 6, 1))},
    {"user": user_ids[1], "activity_type": "walk", "duration": 45, "date": str(date(2025, 6, 2))},
    {"user": user_ids[2], "activity_type": "cycle", "duration": 60, "date": str(date(2025, 6, 3))},
]
db.activity.insert_many(activities)

# Leaderboard
leaderboard = [
    {"team": team_ids[0], "score": 150},
    {"team": team_ids[1], "score": 100},
]
db.leaderboard.insert_many(leaderboard)

# Workouts
workouts = [
    {"name": "Pushups", "description": "Do 20 pushups", "suggested_for": [user_ids[0], user_ids[2]]},
    {"name": "Situps", "description": "Do 30 situps", "suggested_for": [user_ids[1]]},
]
db.workouts.insert_many(workouts)

print("Database populated with test data.")
