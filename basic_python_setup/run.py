from pathlib import Path

from src.code_ex import csv_to_df, quick_regression, poly_regression


def run(csv_path):
    """Reads a in a CSV file, generates a regression plot

    Args:
        csv_path (Path): Path to csv file
    """

    df = csv_to_df(csv_path)
    x, y = quick_regression(df)
    # poly_regression(x,y)


if __name__ == "__main__":
    csv_path = Path('data/1.01. Simple linear regression.csv')
    run(csv_path)