from main import describeData as f


def test_func():
    df = f("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")

    assert df.iloc[:2,0].values[0]==128 # count
    assert df.iloc[:2,0].values[1]==38.8203125 # mean
