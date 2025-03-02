class CalorieTracker:
    """
    A class to track calorie intake, calculate BMI, BMR, and daily calorie needs.

    Attributes:
        weight (float): The user's weight in kilograms.
        height (float): The user's height in centimeters.
        age (int): The user's age in years.
        gender (str): The user's gender ("Male" or "Female").
        activity_level (float): The user's activity level multiplier.
        bmi (float): The user's Body Mass Index (BMI).
        bmr (float): The user's Basal Metabolic Rate (BMR).
        daily_calories (float): The user's daily calorie needs based on BMR and activity level.
        meals (dict): A dictionary to track calories consumed per meal type.
        calories_consumed (float): Total calories consumed by the user.
    """

    def __init__(self, weight, height, age, gender, activity_level):
        """
        Initializes a CalorieTracker instance.

        Args:
            weight (float): The user's weight in kilograms.
            height (float): The user's height in centimeters.
            age (int): The user's age in years.
            gender (str): The user's gender ("Male" or "Female").
            activity_level (float): The user's activity level multiplier.
        """
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        self.activity_level = activity_level
        self.bmi = self.bmi_calculator()
        self.bmr = self.bmr_calculator()
        self.daily_calories = self.bmr * self.activity_level
        self.meals = {"breakfast": 0, "lunch": 0, "dinner": 0}
        self.calories_consumed = 0

    def bmi_calculator(self):
        """
        Calculates the user's Body Mass Index (BMI).

        Returns:
            float: The user's BMI.
        """
        height_in_meters = self.height / 100
        return self.weight / (height_in_meters ** 2)

    def bmr_calculator(self):
        """
        Calculates the user's Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation.

        Returns:
            float: The user's BMR.
        """
        if self.gender == "Male":
            return 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            return 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

    def add_food(self, meal_type, calories):
        """
        Adds calories consumed for a specific meal type.

        Args:
            meal_type (str): The type of meal ("breakfast", "lunch", or "dinner").
            calories (float): The number of calories consumed.
        """
        self.meals[meal_type] += calories
        self.calories_consumed += calories

    def get_remaining_calories(self):
        """
        Calculates the remaining calories the user can consume for the day.

        Returns:
            float: The remaining calories.
        """
        return self.daily_calories - self.calories_consumed

    def get_meal_calories(self):
        """
        Returns the calories consumed per meal type.

        Returns:
            dict: A dictionary with meal types as keys and calories consumed as values.
        """
        return self.meals

    def get_total_consumed_calories(self):
        """
        Calculates the total calories consumed by the user.

        Returns:
            float: The total calories consumed.
        """
        return sum(self.get_meal_calories().values())