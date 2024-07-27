import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open("model.sav","rb"))
def Prediction(input_data):
    if loaded_model[0] == 1:
        return "Couple is compatible"
    else:
        return "Couple is not compatible"
st.set_page_config(
    page_title="FLAMES",
    page_icon="🔥",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
def main():
    st.title("FLAMES")
    # gender, age, income, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met
    gender = st.number_input("Put gender")
    age = st.number_input("Put age")
    income = st.number_input("Put income")
    attraction = st.number_input("Put attraction")
    sincerity = st.number_input("Put sincerity")
    intelligence = st.number_input("Put intelligence")
    funny = st.number_input("Put funny")
    ambition = st.number_input("Put ambition")
    interests = st.number_input("Put interests")
    overall = st.number_input("Put overall")
    reciprocate = st.number_input("Put reciprocate")
    met = st.number_input("Put met")
    rating = None
    if st.button("Enter"):
        rating = Prediction(([[gender, age, income, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met]]))
    st.success(rating)
    
if __name__ == "__main__":
    main()
