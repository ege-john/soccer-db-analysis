# Queries

## Query 1: Team with Highest Free-Kick Accuracy

**Description:**
This query identifies the football team with the highest free-kick accuracy based on player attributes.

**Steps:**
1. Load `PlayerAttributes.csv`, `Match.csv`, and `Team.csv`.
2. Extract the `free_kick_accuracy` values for each player.
3. Map players to their respective teams.
4. Compute the average free-kick accuracy per team.
5. Store the result in `query1.pkl`.

---

## Query 2: Team with Most Left-Footed Players

**Description:**
This query determines which team has the most left-footed players.

**Steps:**
1. Load `PlayerAttributes.csv`, `Player.csv`, `Team.csv`, and `Match.csv`.
2. Identify players with `preferred_foot` as "Left".
3. Map left-footed players to their respective teams.
4. Count the number of left-footed players per team.
5. Store the result in `query2.pkl`.

---

## Query 3: Top Scorer in Slow Build-Up Play Teams

**Description:**
This query finds the highest-scoring player in teams that have a slow build-up play strategy.

**Steps:**
1. Load `TeamAttributes.csv`, `Match.csv`, and `Player.csv`.
2. Identify teams with "slow" build-up play style.
3. Extract goal data from `Match.csv`.
4. Calculate the total goals scored by each player in the selected teams.
5. Identify the top scorer and store the result in `query3.pkl`.

---

