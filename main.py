import pandas as pd
def describeData(filepath):
    df = pd.read_csv(filepath)
    
    return df.describe()
    
