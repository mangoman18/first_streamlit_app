import streamlit
import pandas
streamlit.title("My Parents Healthy Diner")
streamlit.header('New breakfast Menu')
streamlit.text('Uh oh Nothin to show here')
streamlit.text('On intermittent fasting!')
streamlit.text('Ok Will try again going to try again')
#streamlit.text('🍞 Basic Bread')
breakfastmenu = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(breakfastmenu)
