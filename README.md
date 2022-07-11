# FPL Points Prediction
 Points Prediction for next 3 GWs (average) for Fantasy Premier League Players

 The data for 2018/19, 2019/20, 2020/21 and 2021/22 were used to as the prediction data.
 
 For each season, the data for a set of GWs was compared against the points scored in the next 3 GWs
i.e. If the seasons are being considered for every 4GWs, then stats for GWs 1 to 4 are compared againsts points scored for GWs 5 to 7 and so on.

After running all the different GW combinations (2, 3, 4, 5 and 6), the GW with the highest accuracy is used for the model to be selected.

For simplicity, 2 different scenarios were considered.

Scenario 1 - Model that exactly predicted the 3 GWs average score. 

Scenario 2 - Model that predicted a player to score more than 4 points (essentially not blanking) and the player then scoring 4 points or more.

# The results showed how many GWs gave the best accuracy
For goalkeepers and forwards, this was every 6GWs
For defenders and midfielders, this was every 5GWs

# Prediction Accuracy
Goalkeepers - 71.00%
Defenders - 76.02%
Midfielders - 81.83%
Forwards - 76.94%

# Optimum Team Selection
A team selection algorithm (pick2.py) was created to select the optimum team at the budget available. Although, this algorithm is still a work in progress with selection efficiency still an issue