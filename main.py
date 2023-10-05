import math
from random import random

import streamlit as st

from diabetes_prediction import predict_disease
from recomend import get_random_tips


# Creating main function
def diabetes_prediction():
    title = "Diabetes Prediction"
    # if not st.session_state.login:
    #     st.warning("You need to login first")
    #     return
    # Setting title of the page
    st.title(title)
    # Writing Markdown heading 5
    st.markdown("##### Check if you have diabetes or not! \n\n")
    # default values: (5, 166, 72, 19, 175, 25.8, 0.587, 51)
    # Creating input field to enter number of pregnancies
    pregnancies = st.number_input('Number of Pregnancies?', 0, 10, step=1, key='Pregnancies', value=5)
    # Input field to enter age
    age = st.number_input('What is your age?', 0, 100, step=1, key='Age', value=51)

    # Input field to enter glucose level
    glucose = st.number_input('What is your glucose level?', 70, 300, step=1, key='Glucose', value=166)

    # Input field to enter skin thickness
    skin_thickness = st.number_input('What is your skin-thickness?', 12, 40, step=1, key='SkinThickness', value=19)

    # Input field to enter insulin
    insulin = st.number_input('What is your insulin?', 0.00, 500.00, step=1.00, key='insulin')
    bmi = st.number_input('What is your BMI?', 18.4, 300.00, step=1.00, key='BMI', value=25.8)
    blood_pressure = st.number_input('What is your blood pressure?', 70.80, 190.00, step=1.00, key='BP')
    pedigree_function = st.number_input('What is your pedigree function?', 0.00, 140.00, step=1.00, key='PD',
                                        value=0.587)

    # Creating a button
    if st.button("Predict Diabetes", key='predict'):
        try:
            if age == 0:
                output = predict_disease(5, 166, 72, 19, 175, 25.8, 0.587, 51)
            else:
                output = predict_disease(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                                         pedigree_function, age)
            if output == 1:
                st.error("""Sorry to say that you have diabtes""".format(output))
                st.write(
                    "I know it's super sad to know that you have diabetes but don't worry i am here to help you you "
                    "can try following medicines.")
                st.markdown("""**Some tips to control diabetes**""")
            
                st.markdown("""
                **Try these medicines it might work and try to reach out to doctors as soon as possible** :):
                
                Food Recommendations:
                    {0}
                    {1}
                Lifestyle Recommendations:
                    {2}
                    {3}
                
                """.format(random_value[0], random_value[1], random_value[2], random_value[3]))
            else:
                st.success("Hurray! You do not have diabetes".format(output))
        except:
            st.warning("Something didn't go well\nTry again!")


# /login
def main():
    st.title("Login Page")
    username = st.text_input("User Name")
    password = st.text_input("Password", type='password')
    st.session_state.menu = False
    if st.button("Login"):
        if password == '12345':
            st.success("Logged In as {}".format(username))
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.menu = False
            st.session_state.login = True
            diabetes_prediction()
        else:
            st.warning("Incorrect Username/Password")


# /signup
def signup():
    st.title("Signup Page")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    if st.button("Signup"):
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")


routing = st.sidebar.selectbox("Menu", ["Login", "Signup", "Diabetes Prediction"])

if __name__ == '__main__':
    if routing == "Login":
        main()
    elif routing == "Signup":
        signup()
    elif routing == "Diabetes Prediction":
        diabetes_prediction()
