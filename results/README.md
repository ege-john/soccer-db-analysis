# Results

## Overview
This directory contains the output files generated by the queries. The results are stored as serialized Python objects in pickle (`.pkl`) format.

## Files

- **`query1.pkl`**: Stores the name of the team with the highest free-kick accuracy.
- **`query2.pkl`**: Contains a tuple with the team name and the number of left-footed players.
- **`query3.pkl`**: Stores a dictionary with the top scorer's name and their total goals in slow build-up play teams.

## How to Load the Results
To read the results, use the following Python snippet:

```python
import pickle

with open('query1.pkl', 'rb') as file:
    result = pickle.load(file)
print(result)
```

Repeat this for `query2.pkl` and `query3.pkl` by changing the filename.
