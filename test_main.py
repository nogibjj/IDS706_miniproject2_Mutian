from main import describeData as f


def test_func():
    df = f("https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv")
    
    
    print(df)