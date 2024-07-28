import numpy as np
import pickle
import streamlit as st
import sklearn
loaded_model = pickle.load(open("newModel.sav","rb"))
def Prediction(input_data):
    npArray = np.array(input_data)
    array2D = npArray.reshape(1,11)
    Prediction = loaded_model.predict(array2D)
    if Prediction[0] == 1:
        return "Couple is compatible"
    else:
        return "Couple is not compatible"
st.set_page_config(
    page_title="FLAMES",
    page_icon="🔥",
    menu_items={
        'Report a bug': "https://github.com/Defalt-here/FLAMES-couple-predictor/issues",
        'About': "Go ahead check if you're compatible with your crush!\
        Training dataset found at: https://www.kaggle.com/datasets/mexwell/speed-dating/data\
        Check me out on github at: https://github.com/Defalt-here\
        "
    }
)
def main():
    st.title("FLAMES")
    st.subheader("Check out your compatibility with your crush, or your partner maybe you'll fall in love maybe you'll breakup who knows?")
    st.text("Put all the required inputs in integers(no decimals) between 0 to 10 both inclusive")
    # gender, age, income, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met
    option = st.selectbox(
    "Select your gender?",
    ("Male", "Female"))
    if option == "Male":
        gender = 1
    else:
        gender = 0
    age = st.number_input("Enter your age")
    attraction = st.number_input("How attracted you are to the person")
    sincerity = st.number_input("How sincere is the person in question?")
    intelligence = st.number_input("How intelligent is the person in question")
    funny = st.number_input("How funny is the person in question")
    ambition = st.number_input("How ambitious is the person in question")
    interests = st.number_input("How many shared interests do you have with the person?")
    overall = st.number_input("Put an overall score for the person")
    reciprocate = st.number_input("Do you think the person will reciprocate your emotions?")
    met_option = st.selectbox(
    "Have you met before?",
    ("Met before", "Not met"))
    if met_option == "Met before":
        met = 1
    else:
        met = 2
    rating = "Are you compatible? 🥁"
    if st.button("Enter"):
        rating = Prediction([gender, age, attraction, sincerity, intelligence, funny, ambition, interests, overall, reciprocate, met])
    st.success(rating)
    
if __name__ == "__main__":
    main()
