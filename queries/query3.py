"""
QUERY #3

Write a Python script that considers only teams with "slow" buildUpPlaySpeed- Class value.
Amongst such teams, the script must calculate the top-scoaring player (i.e., the player who scored the highest number of goals).
The resulting pickle file must contain a list with the name of the player and said number of goals.
"""

import csv
import json
import pickle

def read_csv(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

team_attributes = read_csv('TeamAttributes.csv')
slow_teams = set()
for row in team_attributes:
    if row['buildUpPlaySpeedClass'] == 'Slow':
        slow_teams.add(row['team_api_id'])

print(f"Number of teams with slow build-up play speed: {len(slow_teams)}")

matches = read_csv('Match.csv')
player_goals = {}
for row in matches:
    if row['home_team_api_id'] in slow_teams or row['away_team_api_id'] in slow_teams:
        if row['goal']:
            goals_data = json.loads(row['goal'].replace("'", "\""))
            for goal in goals_data:
                player_api_id = goal.get('player1')
                if player_api_id:
                    player_goals[player_api_id] = player_goals.get(player_api_id, 0) + 1

print(f"Total goals scored by players in slow teams: {sum(player_goals.values())}")

players = read_csv('Player.csv')
for row in players:
    player_api_id = row['player_api_id']
    if player_api_id in player_goals:
        player_name = row['player_name']  
        player_goals[player_name] = player_goals.pop(player_api_id)

top_scorer = max(player_goals, key=player_goals.get, default=None) 
goals = player_goals.get(top_scorer, 0)

print(f"Top Scorer: {top_scorer} with {goals} goals")

result = {'top_scorer': top_scorer, 'goals': goals}
with open('query3.pkl', 'wb') as f:
    pickle.dump(result, f)
