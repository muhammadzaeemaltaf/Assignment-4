import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# st.title("Streamlit Fundamentals")
# st.header("This is header")
# st.subheader("This is subheader")
# st.text("This is simple text")
# st.markdown("**This is bold text using markdown**")


# name = "Zaeem"
# number = 10
# st.write("Hello", name, number)


# ===== Widgets =====

# if st.button("Click Me"):
#     st.write("Button Clicked")

# checked =  st.checkbox("Check Me")
# if checked:
#     st.write("Checkbox Checked")

# age = st.slider("Enter your age", 0, 100, 18)
# st.write("Your age is", age)

# name = st.text_input("Enter your name", value="")
# st.write("Your name is", name)

# name = st.text_input("Enter your name")
# age = st.slider("Enter your age", 0, 100)
# if st.button("Submit"):
#     st.write(f"Hello {name}, you are {age} years old.")


# ===== Excercise =====

# name = st.text_input("Enter your name")
# age = st.slider("Enter your age", 0, 100)
# number = st.number_input("Enter your favourite number", 0, 100)
# if st.button("Submit"):
#     st.write(f"Hello {name}, you are {age} years old.")
#     st.write(f"Your favourite number is {number}.")


# ===== Displaying Data & Styling =====

# data = {
#     "Name":["John", "Annie", "Peter"],
#     "Age": [32, 43, 23],
#     "City": ["Pakistan","Leberio", "DC"],
#     "Score": [90, 80, 70],
# }

# df = pd.DataFrame(data)

# st.dataframe(df) # Scrollable
# st.table(df) # None Scrollable

# city = st.selectbox("Select a city", df["City"].unique())
# filtered_df = df[df["City"] == city]

# st.write("Selected City:", city)
# st.write("Filtered Data", filtered_df)

# style_df = df.style.applymap(lambda x:"background-color: yellow" if isinstance(x, int) and x > 80 else "")
# st.dataframe(style_df)


# ===== Display Visualization on web =====

# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns=["a", "b", "c"],
# )
# st.line_chart(data)
# st.area_chart(data)
# st.bar_chart(data)
# st.line_chart(data, use_container_width=True)

# data = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Grapes"],
#     "Amount": [10, 20, 30, 40],
# })
# fig = px.bar(data, x="Fruit", y="Amount", title="Fruit Amounts")
# st.plotly_chart(fig)


# data = pd.DataFrame(
#     np.random.randn(100, 3),
#     columns=["a", "b", "c"],
# )

# plt.figure(figsize=(10, 6))
# sns.scatterplot(x=data["a"], y=data["b"])

# st.pyplot(plt)


# ===== Layout & Theme Options =====

# col1, col2 = st.columns(2)

# with col1:
#     st.header("Column 1")
#     st.write("This is column 1")
#     st.button("Button 1")

# with col2:
#     st.header("Column 2")
#     st.write("This is column 2")
#     st.button("Button 2")


# with st.expander("See explanation"):
#     st.write("This is an expander")
#     st.write("You can put any content here")
#     st.line_chart([1, 2, 3, 4, 5])


# st.sidebar.header("Navigation")

# option = st.sidebar.selectbox(
#     "Select an option",
#     ("Home", "About", "Contact")
# )

# if option == "Home":
#     st.write("Welcome to the Home page!")
# elif option == "About":
#     st.write("This is the About page.")
# elif option == "Contact":
#     st.write("This is the Contact page.")
