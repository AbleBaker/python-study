import pandas as pd


def test_run():
    """Function called by Test Run."""
    df = pd.read_csv("data/AAPL.csv")
    # TODO: Print last 5 rows of the data frame
    print(df.tail(5)) # use head() and tail() methods
    


if __name__ == "__main__":
    test_run()
