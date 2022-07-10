import pandas as pd

# "Linear Regress combined.csv", "Complete Random Forest combined.csv", "Incomplete Random Forest combined.csv"

# Turn the CSV into a pandas table for iterations
dataset = pd.read_csv("Linear Regress combined.csv")


# Sort the dataset for first Points Predicted from highest to lowest and then where even sort for combined Price from lowest to highest
# This will help maximise the budget
dataset.sort_values(["Points", "Prices"], axis=0, ascending=[False, False], inplace=True)

dataset = dataset[(dataset.Prices <= 40) & (dataset.Points >= 23)]

# Teams to be appended here as gotten
team = []

# Players to exclude
exclusion = ["Kenedy ", "Torres ", "Steer ", "Sterling ", "Hudson-Odoi ", "Eriksen ", "Pukki ", "Ronaldo ", "Ward ", "Steffen ", "Steele ", "Foster ", "Kelleher ", "Caballero ", "Olsen ", "Price ", "Woodman ", "Mané ", "Sarr "]

# Total estimated points for the next 3GWs
total_points = 0

# Starting budget
budget = 77

# Positions to be gotten from iteration
positions = {'G': 1, 'D': 3, 'M': 4, 'F': 2}

# Blank positions dictionaries used in iteration
new_position = {'G': 0, 'D': 0, 'M': 0, 'F': 0}

epl_team = {    
    'ARS': 0, 'AVL': 0, 'BRE': 0, 'BHA': 0, 'BUR': 0,
    'CHE': 0, 'CRY': 0, 'EVE': 0, 'LEE': 0, 'LEI': 0,
    'LIV': 0, 'MCI': 0, 'MUN': 0, 'NEW': 0, 'NOR': 0,
    'SOU': 0, 'TOT': 0, 'WAT': 0, 'WHU': 0, 'WOL': 0
}

# Initialise iteration counter to 0
count = 0

# FPL allows 3 players max per EPL team so this dict is used to track that
max_from_teams = {    
    'ARS': 3, 'AVL': 3, 'BRE': 3, 'BHA': 3, 'BUR': 3,
    'CHE': 3, 'CRY': 3, 'EVE': 3, 'LEE': 3, 'LEI': 3,
    'LIV': 3, 'MCI': 3, 'MUN': 3, 'NEW': 3, 'NOR': 3,
    'SOU': 3, 'TOT': 3, 'WAT': 3, 'WHU': 3, 'WOL': 3
    # 'ARS': 2, 'AVL': 2, 'BRE': 3, 'BHA': 3, 'BUR': 3,
    # 'CHE': 2, 'CRY': 3, 'EVE': 3, 'LEE': 2, 'LEI': 2,
    # 'LIV': 0, 'MCI': 3, 'MUN': 3, 'NEW': 3, 'NOR': 2,
    # 'SOU': 3, 'TOT': 1, 'WAT': 3, 'WHU': 3, 'WOL': 2
}



# For every index and row in the pandas table
for index, row in dataset.iterrows():

    # Add 1 to the iteration counter
    count += 1

    # Keep running when budget is above 12 because there is no way way 3 players cost this little
    if budget >= 0 or len(team) < 10:

        # If the budget is more than $15, budget is more than the Prices of the row being iterated but the rows Price is less than 25 etc
        if budget >= row['Prices'] and row["Prices"] <= 40 and  positions[row['Position1']] != 0 and row['Player1'] not in team and row['Player1'] not in exclusion:
            new_position[row['Position1']] += 1
            epl_team[row['Team1']] += 1

            if positions[row['Position2']] != 0 and row['Player2'] not in team and row['Player2'] not in exclusion:
                new_position[row['Position2']] += 1
                epl_team[row['Team2']] += 1

                if positions[row['Position3']] != 0 and row['Player3'] not in team and row['Player3'] not in exclusion:
                    new_position[row['Position3']] += 1
                    epl_team[row['Team3']] += 1

                    if positions[row['Position4']] != 0 and row['Player4'] not in team and row['Player4'] not in exclusion:
                        new_position[row['Position4']] += 1
                        epl_team[row['Team4']] += 1

                        if positions[row['Position5']] != 0 and row['Player5'] not in team and row['Player5'] not in exclusion:
                            new_position[row['Position5']] += 1
                            epl_team[row['Team5']] += 1

                            # If the new position counter is less than or equal to the positions dict then you can add the 5 players to the team list
                            if (new_position[row['Position1']] <=  positions[row['Position1']]) and (new_position[row['Position2']] <=  positions[row['Position2']]) and (new_position[row['Position3']] <=  positions[row['Position3']]) and (new_position[row['Position4']] <=  positions[row['Position4']])  and (new_position[row['Position5']] <=  positions[row['Position5']]) and (epl_team[row['Team1']] <= max_from_teams[row['Team1']]) and (epl_team[row['Team2']] <= max_from_teams[row['Team2']]) and (epl_team[row['Team3']] <= max_from_teams[row['Team3']]) and (epl_team[row['Team4']] <= max_from_teams[row['Team4']]) and (epl_team[row['Team5']] <= max_from_teams[row['Team5']]):
                                team.append(row['Player1'])
                                team.append(row['Player2'])
                                team.append(row['Player3'])
                                team.append(row['Player4'])
                                team.append(row['Player5'])

                                # Reduce the budget
                                budget -= row['Prices']

                                # Reduce the positions as necessary
                                positions[row['Position1']] -= 1
                                positions[row['Position2']] -= 1
                                positions[row['Position3']] -= 1
                                positions[row['Position4']] -= 1
                                positions[row['Position5']] -= 1

                                # Reduce the Team position available
                                max_from_teams[row['Team1']] -= 1
                                max_from_teams[row['Team2']] -= 1
                                max_from_teams[row['Team3']] -= 1
                                max_from_teams[row['Team4']] -= 1
                                max_from_teams[row['Team5']] -= 1
                                
                                # Add up the new total points for the next 3GWs
                                total_points += row['Points']
    else:
        break

    # Rest loop counters and print out the positions left, teams, total points, budget left and the number of iterations run so far
    new_position['G'] = 0
    new_position['D'] = 0
    new_position['M'] = 0
    new_position['F'] = 0
    epl_team[row['Team1']] = 0
    epl_team[row['Team2']] = 0
    epl_team[row['Team3']] = 0
    epl_team[row['Team4']] = 0
    epl_team[row['Team5']] = 0
    print(f"{team}, {positions} Points over 3GW: {total_points}, {budget}, {count}")