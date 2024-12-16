import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def csv_to_df(path):
    """Reads a CSV file, creates a dataframe(df)

    Args:
        path (Path): Path To csv file

    Returns:
        df: Pandas dataframe
    """

    df = pd.read_csv(path)

    return df

def quick_regression(df):
    """Creates a regression line for the dataframe given

    Args:
        df (DF): Pandas Dataframe

    Returns:
        x: X coordinates
        y: Y coordinates
    """

    x = list(df.iloc[:, 0])
    y = list(df.iloc[:,-1])

    coef = np.polyfit(x,y,1)
    poly1d_fn = np.poly1d(coef) 

    plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')

    plt.xlim(min(x), max(x))
    plt.ylim(min(y), max(y))
    plt.show()

    return x, y

def poly_regression(X, y):
    """WIP

    Args:
        X (_type_): X coordinates
        y (_type_): Y coordinates
    """
    pass
    #from sklearn.svm import SVC
    #model = SVC(kernel='poly')
    #model.fit(X,y)


