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
        'Report a bug': "https://github.com/Defalt-here/FLAMES-couple-predictor/issues",
        'About': "Go ahead check if you're compatible with your crush!"
    }
)
def main():
    st.title("FLAMES")
    # gender, age, income, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met
    gender = st.number_input("Put gender")
    age = st.number_input("Put age")
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
        rating = Prediction(([[gender, age, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met]]))
    st.success(rating)
    
if __name__ == "__main__":
    main()
