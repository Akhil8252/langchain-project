import streamlit as st
import helper

st.title("Restaurant Name Generator")

# make a dropdown menu
cuisine = st.sidebar.selectbox("pick a cuisine",("Indian","chinese","American","arabic","Mexicon","italic","Russian"))

if cuisine:
    response = helper.generate_restaurant_name_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response['menu_items'].strip().split(",")

    st.write("menu items are:")

    for item in menu_items:
        st.write(".",item)


