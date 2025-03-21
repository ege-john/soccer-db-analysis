"""
QUERY #1

Write a Python script that calculates the team that has the highest free_kick_accuracy amongst its players. If a given team appears with different squads (i.e., different players), different squads have to be considered separately as there are different players. The resulting pickle file must contain the name of such team. More on
pickle files later.
"""


import csv
import pickle
from datetime import datetime

def read_csv(file_path):
  data = []
  with open(file_path, 'r') as csvfile:
      reader = csv.reader(csvfile)
      headers = None
      for row in reader:
          if headers is None:
              headers = row
          else:
              row_data = dict(zip(headers, row))
              data.append(row_data)
  return data

def calculate_team_fk_accuracy(team_players, player_attributes_data):

    total_accuracy = 0
    valid_player_count = 0

    for player_id in team_players:
        player_data = player_attributes_data.get(str(player_id), {})
        if 'free_kick_accuracy' in player_data:
            try:
                accuracy = int(player_data['free_kick_accuracy'])
                total_accuracy += accuracy
                valid_player_count += 1
            except ValueError:
                pass

    if valid_player_count > 0:
        return total_accuracy / valid_player_count
    else:
        return 0


player_attributes_path = 'PlayerAttributes.csv'
match_path = 'Match.csv'
team_path = 'Team.csv'


player_attributes = read_csv(player_attributes_path)
matches = read_csv(match_path)
teams = read_csv(team_path)


for record in player_attributes:
    record['date'] = datetime.strptime(record['date'], "%d/%m/%Y %H:%M")

def sort_key(record):
    return (record['player_api_id'], record['date'])

player_attributes.sort(key=sort_key, reverse=True)

latest_player_attributes = {}

for record in player_attributes:
    player_api_id = record['player_api_id']
    if player_api_id not in latest_player_attributes:
        latest_player_attributes[player_api_id] = record

filtered_matches = []
for match in matches:
    if match['home_team_api_id'] and match['away_team_api_id']:
        filtered_matches.append(match)


def convert_player_ids_to_int(match_data):
    for match in match_data:
        for i in range(1, 12):
            if match[f'home_player_{i}']:
                match[f'home_player_{i}'] = int(float(match[f'home_player_{i}']))
            if match[f'away_player_{i}']:
                match[f'away_player_{i}'] = int(float(match[f'away_player_{i}']))

convert_player_ids_to_int(filtered_matches)


team_fk_accuracy = {}
for match in filtered_matches:
    home_team = match['home_team_api_id']
    away_team = match['away_team_api_id']
    home_players = [match[f'home_player_{i}'] for i in range(1, 12) if match[f'home_player_{i}']]
    away_players = [match[f'away_player_{i}'] for i in range(1, 12) if match[f'away_player_{i}']]

    home_fk_accuracy = calculate_team_fk_accuracy(home_players, latest_player_attributes)
    away_fk_accuracy = calculate_team_fk_accuracy(away_players, latest_player_attributes)

    if home_team not in team_fk_accuracy:
        team_fk_accuracy[home_team] = []
    team_fk_accuracy[home_team].append(home_fk_accuracy)

    if away_team not in team_fk_accuracy:
        team_fk_accuracy[away_team] = []
    team_fk_accuracy[away_team].append(away_fk_accuracy)


overall_team_fk_accuracy = {}
for team, accuracies in team_fk_accuracy.items():
    if accuracies:
        average_accuracy = sum(accuracies) / len(accuracies)
        overall_team_fk_accuracy[team] = average_accuracy

highest_fk_team = None
highest_accuracy = -1
for team, accuracy in overall_team_fk_accuracy.items():
    if accuracy > highest_accuracy:
        highest_fk_team = team
        highest_accuracy = accuracy

team_name = "Unknown Team"
for team in teams:
    if team['team_api_id'] == highest_fk_team:
        team_name = team['team_long_name']
        break

with open('query1.pkl', 'wb') as file:
    pickle.dump(team_name, file)

print(f"Team with the highest FK accuracy: {team_name}")
