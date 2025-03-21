"""
QUERY #2

Write a Python script that calculates the team which has (across the entire
dataset, by considering also different squads) the highest number of left-footed
players. The resulting pickle file must contain a tuple with the name of the
team and the number of said players.
"""

import csv
import pickle


def read_csv(file_path):
  with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    return list(csv_reader)


player_attributes = read_csv('PlayerAttributes.csv')
players = read_csv('Player.csv')
teams = read_csv('Team.csv')
matches = read_csv('Match.csv')

left_footed_players = []
for player in player_attributes:
  if player.get('preferred_foot') == 'left':
    left_footed_players.append(player)
 print(f"Number of left-footed players: {len(left_footed_players)}")

player_team_map = {}
for match in matches:
  for i in range(1, 12):
    home_player = match.get(f'home_player_{i}')
    away_player = match.get(f'away_player_{i}')
    if home_player:
      player_team_map[home_player] = match.get('home_team_api_id')
    if away_player:
      player_team_map[away_player] = match.get('away_team_api_id')

team_left_footed_count = {}
for player in left_footed_players:
  player_id = player.get('player_api_id')
  team_id = player_team_map.get(str(float(player_id)))
  if team_id:
    team_left_footed_count[team_id] = team_left_footed_count.get(team_id,0) + 1

 print(f"Teams with left-footed players: {len(team_left_footed_count)}")

if team_left_footed_count:
  most_left_footed_team = max(team_left_footed_count, key=team_left_footed_count.get)
  most_left_footed_count = team_left_footed_count[most_left_footed_team]
  most_left_footed_team_name = None
  for team in teams:
    if team['team_api_id'] == most_left_footed_team:
      most_left_footed_team_name = team['team_long_name']
      break
  if most_left_footed_team_name:
    # print(f"The team with the most left-footed players is {most_left_footed_team_name} with {most_left_footed_count} players.")
    with open('query2.pkl', 'wb') as file:
      pickle.dump((most_left_footed_team_name, most_left_footed_count), file)
  else:
  print("Team Not Found")
else:
print("No teams with left-footed players found.")
