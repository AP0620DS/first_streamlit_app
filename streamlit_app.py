import streamlit 
import pandas
streamlit.header('\U0001F600 Breakfast Favorites')
streamlit.text('\U0001F423 Omega 3 & Blueberry Oatmeal')
streamlit.text('\U0001F33F Kale , spinach & Rocket Smoothie')
streamlit.text('\U0001F95A Hard-Boiled Free Range Egg')
streamlit.text('\U0001F951 Avacado Toast')
streamlit.header('\U0001F34C \U0001F96D Build Your Own Fruit Smoothie \U0001F95D \U0001F34A')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
 
fruits_selected = streamlit.multiselect("Pick some fruits :", list(my_fruit_list.index),[ 'Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)


#New Section to display fruityvice api response 
import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)



#New Section to display fruityvice api response 

streamlit.header('Fruityvice Fruit Advice !')

import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"Kiwi")
#streamlit.text(fruityvice_response.json()) delete 


#Take the json version of the response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

#output it on the screeen as a table 

streamlit.dataframe(fruityvice_normalized)
