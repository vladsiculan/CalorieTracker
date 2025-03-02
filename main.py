import streamlit as st
import src.database.csv_files
from src.database.calorie_tracker import CalorieTracker
from src.database.models import User, session
from src.database.email_function import validate



# Set page configuration for the Streamlit app
st.set_page_config(layout="wide")

# Define base theme and font for the app
base = "dark"
font = "serif"

# Sidebar section
with st.sidebar:
    # Display the app title with emojis
    st.markdown(
        """
        <div style="text-align: center;">
            <p style="font-weight:bold; font-size: 30px;">💪Calorie Tracker🍎</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Display an image in the sidebar
    st.image("src/sidebar_image/sidebar.jpg", use_container_width=True)

# Create two columns for layout
col1, col2 = st.columns([1, 2])

# First column with tabs for general information, calories, and health
with col1:
    tab1, tab2, tab3 = st.tabs(["General", "Calories", "Health"])

    # General information tab
    with tab1:
        st.header("General information")

        # Display general information about the app
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;">This</span> application is a calorie tracker built using Streamlit, 
                a popular framework for creating interactive web applications in Python.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;">The</span> app allows users to monitor their 
                daily calorie intake, calculate their Body Mass Index (BMI) and Basal Metabolic Rate (BMR), 
                and track their food consumption by meal categories (breakfast, lunch, dinner).
            </div>
            """,
            unsafe_allow_html=True
        )

    # Calories tab
    with tab2:
        st.header("What is a calorie?")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> A</span> calorie is a unit of energy. It measures the energy content
                 in food and beverages.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Daily Calorie Needs")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> On</span> average, men need about 2,500 calories per day, while
                 women need about 2,000 calories per day. 
                 Your exact needs depend on your age, weight, height, and activity level.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Weight Management")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> To</span> lose weight, eat fewer calories than you burn. 
                To gain weight, eat more calories than you burn.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Calories and Exercise")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> Walking</span> for 30 minutes burns about 100-150 calories,
                 running burns 300-400 calories, and cycling burns 200-300 calories.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

    # Health tab
    with tab3:
        st.header("Benefits of Exercise")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> Regular</span> exercise improves heart health, 
                boosts energy, and helps maintain a healthy weight.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Types of Exercise")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> Cardio</span> exercises like running, cycling, and swimming improve 
                endurance and burn calories, strength training like lifting weights builds muscle and boosts 
                metabolism, and flexibility exercises like yoga and stretching improve mobility and reduce injury 
                risk.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Exercise Recommendations")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> Aim</span> for at least 150 minutes of moderate exercise 
                (such as brisk walking) or 75 minutes of intense exercise (such as running) each week.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.header("Health Tips")
        st.markdown(
            """
            <div style="margin-left: -20px;">
                <span style="margin-left: 30px;"> Stay</span> hydrated by drinking water before, during, and after 
                exercise, combine exercise with a balanced diet for the best results, and get enough sleep to help your
                body recover and stay healthy.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

    # Dictionary for activity level multipliers
    activity_level_dict = {
        "sedentary": 1.2,
        "lightly active": 1.375,
        "moderately active": 1.55,
        "very active": 1.9,
    }

    # Initialize user in session state if not already present
    if "user" not in st.session_state:
        st.session_state.user = None

# Second column for user data input and calorie tracking
with col2:
    st.title("Users data")
    st.subheader("Please write your data below:")

    # Input fields for user data
    firstname = st.text_input("Firstname", placeholder="Please write your firstname")
    if firstname:
        lastname = firstname.split(' ')[0].split('-')[0]
        if firstname[0].isupper():
            st.success("Firstname is valid.")
        else:
            st.error("The first name must start with a capital letter, and be separated by a space or '-'.")

    lastname = st.text_input("Lastname", placeholder="Please write your lastname")
    if lastname:
        if lastname[0].isupper():
            st.success("Lastname is valid.")
        else:
            st.error("The first letter of the lastname must be capitalized.")

    email = st.text_input("Email", placeholder="Please write your email")
    if email:
        if validate(email):
            st.success("Email is valid.")
        else:
            st.error("Email is not valid")

    age = st.number_input("Age", value=None, min_value=1, step=1, placeholder="Please enter your age")
    if age is not None:
        if age > 0:
            st.success("Age is valid.")
        else:
            st.error("Age is not valid")

    height = st.number_input("Height (cm)", value=None, min_value=1, step=1, placeholder="Please enter your height in cm")
    if height is not None:
        if height > 0:
            st.success("Height is valid.")
        else:
            st.error("Height is not valid")

    weight = st.number_input("Weight (kg)", value=None, min_value=1, step=1, placeholder="Please enter your weight in kg")
    if weight is not None:
        if weight > 0:
            st.success("Weight is valid.")
        else:
            st.error("Weight is not valid")

    gender = st.selectbox(
        "Please choose your gender",
        ("Male", "Female"),
        index=None,
        placeholder="Select your gender...",
    )
    st.write("You selected:", gender)

    activity_level = st.selectbox(
        "Please choose your activity level",
        ("sedentary", "lightly active", "moderately active", "very active"),
        index=None,
        placeholder="Select your activity level...",
    )
    st.write("You selected:", activity_level)


    # Calculate BMI and BMR when the button is clicked
    if st.button("Calculate BMI and BMR"):
        if activity_level in activity_level_dict:
            activity_level_value = activity_level_dict[activity_level]
        else:
            st.error("Please select a valid activity level.")
            st.stop()


        # Create a CalorieTracker instance and store it in session state
        st.session_state.user = CalorieTracker(weight, height, age, gender, activity_level_value)

    # Display BMI and BMR results if user data is available
    if st.session_state.get("user"):
        user = st.session_state.user
        st.write(f"**Your BMI is:** {user.bmi:.2f}")
        st.write(f"**Daily calorie intake (BMR x activity level):** {user.daily_calories:.0f} kcal")

        # Save user data to the database if not already saved
        if "user_saved" not in st.session_state:
            try:
                new_user_data = User(
                    firstname=firstname,
                    lastname=lastname,
                    age=age,
                    gender=gender,
                    bmr=user.daily_calories,
                    consumed_calories=user.get_total_consumed_calories(),
                    remaining_calories=user.get_remaining_calories(),
                )
                session.add(new_user_data)
                session.commit()
                st.session_state.user_saved = True
                st.success("User data saved successfully!")
            except Exception as e:
                session.rollback()
                st.error(f"Error saving user data: {e}")

        # Track food intake
        st.subheader("Track your food intake")

        try:
            # Load food data from CSV
            food_data = src.database.csv_files.get_data()
            selected_food = st.selectbox("Select a food item:", food_data["Food_item"])
            food_calories = food_data.loc[food_data["Food_item"] == selected_food, "Cals_per100grams"].values[0]
            grams = st.number_input("Quantity (g)", min_value=0, max_value=1000, value=100)
            meal_type = st.selectbox("Meal type", ["breakfast", "lunch", "dinner"])

            # Add food to the tracker
            if st.button("Add food"):
                consumed_calories = (food_calories / 100) * grams
                user.add_food(meal_type, consumed_calories)

                # Update user data in the database
                try:
                    user_data = session.query(User).filter_by(firstname=firstname, lastname=lastname).first()
                    if user_data:
                        user_data.consumed_calories = user.get_total_consumed_calories()
                        user_data.remaining_calories = user.get_remaining_calories()
                        session.commit()
                        st.success("Food data updated successfully!")
                except Exception as e:
                    session.rollback()
                    st.error(f"Error updating food data: {e}")

                # Display consumed and remaining calories
                st.write(f"You consumed: {consumed_calories:.0f} kcal at {meal_type}.")
                st.write(f"**Total consumed calories:** {user.get_total_consumed_calories():.0f} kcal")
                st.write(f"**Remaining calories:** {user.get_remaining_calories():.0f} kcal")

                # Display calories per meal
                st.subheader("Consumed calories per meal")
                meal_calories = user.get_meal_calories()
                for meal, calories in meal_calories.items():
                    st.write(f"{meal.capitalize()}: {calories:.0f} kcal")

        except Exception as e:
            st.error(f"CSV file error: {e}")
