import pickle

from pandas import read_csv

NEW_COLUMN_NAMES = {"Cost (£M)":"Cost", "Points":"Points_x"}

def main():
    # Load the trained model
    def_pickles = ["Linear DEF PerApp 5GWs.pkl", "Incomplete Forest DEF PerApp 5GWs.pkl"]
    mid_pickles = ["Linear MID PerApp 5GWs.pkl", "Incomplete Forest MID PerApp 5GWs.pkl"]
    fwd_pickles = ["Linear FWD PerApp 6GWs.pkl", "Incomplete Forest FWD PerApp 6GWs.pkl"]

    all_predictions(def_pickles, mid_pickles, fwd_pickles)

def all_predictions(def_pickles, mid_pickles, fwd_pickles):
    single_predict(pickling="Linear GK PerApp 6GWs.pkl", file="GK PerApp 6GWs.csv")
    single_random_predict(pickling="Complete GK PerStart 2GWs.pkl", file="GK PerStart 2GWs.csv")
    single_predict(pickling="Incomplete Forest GK PerStart 2GWs.pkl", file="GK PerStart 2GWs.csv")
    group_prediction(pickles=def_pickles, file="DEF PerApp 5GWs.csv")
    single_random_predict(pickling= "Complete DEF PerApp 5GWs.pkl", file= "DEF PerApp 5GWs.csv")
    group_prediction(pickles=mid_pickles, file="MID PerApp 5GWs.csv")
    single_random_predict(pickling= "Complete MID PerApp 5GWs.pkl", file= "MID PerApp 5GWs.csv")
    group_prediction(pickles=fwd_pickles, file="FWD PerApp 6GWs.csv")
    single_random_predict(pickling= "Complete FWD PerApp 6GWs.pkl", file= "FWD PerApp 6GWs.csv")


def single_predict(pickling, file):
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = read_csv(file)
    data = read_csv(file)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x) for x in prediction]

    header = ["Name", "Cost", "Prediction"]
    data_new = data.assign(Prediction = prediction)
    data_new.to_csv(f"{file[:-4]} {pickling[:1]}-Prediction.csv", index=False, columns= header)


def single_random_predict(pickling, file):
    pickle_in = open(pickling, "rb")
    rf = pickle.load(pickle_in)

    data_predict = read_csv(file)
    data = read_csv(file)

    # Rename the Cost column
    data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
    data = data.rename(columns=NEW_COLUMN_NAMES)

    # Drop the columns that are not going to be used in the regression
    data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position"], axis=1, inplace=True)

    # Setting up the values of x and y
    x = data_predict

    # Run the prediction
    prediction = rf.predict(x)
    prediction = [round(x) for x in prediction]

    header = ["Name", "Cost", "Prediction"]
    data_new = data.assign(Prediction = prediction)
    data_new.to_csv(f"{file[:-4]} {pickling[:1]}-Prediction.csv", index=False, columns= header)

def group_prediction(pickles, file):
    for pickling in pickles:
        pickle_in = open(pickling, "rb")
        rf = pickle.load(pickle_in)

        data_predict = read_csv(file)
        data = read_csv(file)

        # Rename the Cost column
        data_predict = data_predict.rename(columns=NEW_COLUMN_NAMES)
        data = data.rename(columns=NEW_COLUMN_NAMES)

        # Drop the columns that are not going to be used in the regression
        data_predict.drop(["Name", "App.", "Fouls Made", "Exp. Clean Sheets", "Names", "Position", "Cost", "Team"], axis=1, inplace=True)

        # Setting up the values of x and y
        x = data_predict

        # Run the prediction
        prediction = rf.predict(x)
        prediction = [round(x) for x in prediction]

        header = ["Name", "Cost", "Prediction"]
        data_new = data.assign(Prediction = prediction)
        data_new.to_csv(f"{file[:-4]} {pickling[:1]}-Prediction.csv", index=False, columns= header)

if __name__ == "__main__":
    main()