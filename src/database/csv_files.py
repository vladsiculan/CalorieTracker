import pandas as pd
from src.settings import DATA_DIR

# Path to the calories data CSV file
calories_data_path = DATA_DIR / "calories.csv"

def get_data():
    """
    Reads the calories data from a CSV file and returns it as a pandas DataFrame.

    The CSV file is expected to have columns representing food items and their calorie content.

    Returns:
        pd.DataFrame: A DataFrame containing the food items and their calorie information.
    """
    file_path = r'D:\Final_Project\CalorieApp\src\data\calories.csv'
    food_calories = pd.read_csv(file_path)
    return food_calories

if __name__ == "__main__":
    # Test the function by printing the data
    print(get_data())


