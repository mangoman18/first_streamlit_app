import streamlit
import pandas
streamlit.title("My Parents Healthy Diner")
streamlit.header('New breakfast Menu')
streamlit.text('Uh oh Nothin to show here')
streamlit.text('On intermittent fasting!')
streamlit.text('Ok Will try again')
#streamlit.text('🍞 Basic Bread')
streamlit.header("🥣 🥗 Build your own Smoothiee 🥑")
breakfastmenu = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
breakfastmenu = breakfastmenu.set_index('Fruit')

fruits_selected = streamlit.multiselect('Choose your Fruit',list(breakfastmenu.index),['Avocado','Strawberries'])
#streamlit.dataframe(breakfastmenu)
fruits_to_show = breakfastmenu.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
