import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header ('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry 03tneal')
streamlit.text('Kalo, Spinach & Rocket Swoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatneal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Bolled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
