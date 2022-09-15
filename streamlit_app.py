import streamlit
import pandas

# front page
streamlit.title('My Parent New Healthy Diner')
   
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# data handling
my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')#pull the data into a dataframe

#set the df index more readable
my_fruit_list = my_fruit_list.set_index('Fruit')

# a pick list for people to pick fruit
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

streamlit.dataframe(my_fruit_list)#display the df on the front page

