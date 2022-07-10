import pandas as pd
from itertools import combinations
from tqdm import tqdm

number_of_players = 11

# Function for multiplying through a list
def sum_list_items(list):
    answer = 0
    for x in list:
        answer += x 
    return answer

files = ["Linear Regress.csv"]

def main():

    for file in tqdm(files):

        # Read in the Midfielders Excel scrapped file 
        dataset = pd.read_csv(file)

        # Fill in any cells that might be blank or NaN
        dataset.fillna(0, inplace=True)
        dataset['Predict'] = dataset['Predict'].astype(str)
        dataset['Price'] = dataset['Price'].astype(str)

        # Empty lists to accommodate the predicted points total, names of players in those points and their total prices
        cum_product = []
        player_names = []
        player_prices = []
        player_teams = []
        positioning = []

        for predict in tqdm(combinations(dataset['Predict'], number_of_players), total=41507642):    # For each combination gotten
            # print(predict)
            int_list = list(map(float, predict))                # Turn the combination into an iterable list of floats
            cum_product.append(sum_list_items(int_list))        # After multiplying through the list, append the answer to total predicted points list

        for name in tqdm(combinations(dataset['Name'], number_of_players), total=41507642):
            # print(name)
            player_names.append(name)

        for price in tqdm(combinations(dataset['Price'], number_of_players), total=41507642):
            # print(price)
            int_list = list(map(float, price))
            player_prices.append(sum_list_items(int_list))

        for teams in tqdm(combinations(dataset['Team Name'], number_of_players), total=41507642):
            # print(teams)
            player_teams.append(teams)

        for pos in tqdm(combinations(dataset['Position'], number_of_players), total=41507642):
            # print(pos)
            positioning.append(pos)

        dfpredict = pd.DataFrame(cum_product)                   # Create dataframes for each of the lists created
        dfpredict2 = pd.DataFrame(player_names)
        dfpredict3 = pd.DataFrame(player_prices)
        dfpredict4 = pd.DataFrame(player_teams)
        dfpredict5 = pd.DataFrame(positioning)

        # headers = ["Points","Player1","Player2","Prices","Team1","Team2","Position1","Position2"]
        # headers = ["Points","Player1","Player2","Player3","Prices","Team1","Team2","Team3","Position1","Position2","Position3"]
        headers = ["Points","Player1","Player2","Player3","Player4","Player5","Prices","Team1","Team2","Team3","Team4","Team5","Position1","Position2","Position3","Position4","Position5"]
        data = pd.concat([dfpredict, dfpredict2, dfpredict3, dfpredict4, dfpredict5], axis=1)   # Concat the dataframes horizontally so all their values appear on the same line like a neat table
        data.to_csv(f"{file[:-4]} combined.csv", index=False, header=headers)      # Push the final table to an excel file I can work with
if __name__ == "__main__":
    main()