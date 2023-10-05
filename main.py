import streamlit as st

from diabetes_prediction import predict_disease


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

    # Creating input field to enter number of pregnancies
    pregnancies = st.number_input('Number of Pregnancies?', 0, 10, step=1, key='Pregnancies')

    # Input field to enter age
    age = st.number_input('What is your age?', 0, 100, step=1, key='Age')

    # Input field to enter glucose level
    glucose = st.number_input('What is your glucose level?', 70, 300, step=1, key='Glucose')

    # Input field to enter skin thickness
    skin_thickness = st.number_input('What is your skin-thickness?', 12, 40, step=1, key='SkinThickness')

    # Input field to enter insulin
    insulin = st.number_input('What is your insulin?', 0.00, 500.00, step=1.00, key='insulin')
    bmi = st.number_input('What is your BMI?', 18.4, 300.00, step=1.00, key='BMI')
    blood_pressure = st.number_input('What is your blood pressure?', 70.80, 190.00, step=1.00, key='BP')
    pedigree_function = st.number_input('What is your pedigree function?', 0.00, 140.00, step=1.00, key='PD')

    # Creating a button
    if st.button("Predict Diabetes", key='predict'):
        try:
            output = predict_disease(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi,
                                     pedigree_function, age)
            if output == 1:
                st.error("""Sorry to say that you have diabtes""".format(output))
                st.write(
                    "I know it's super sad to know that you have diabetes but don't worry i am here to help you you "
                    "can try following medicines.")
                st.markdown("""
                **Try these medicines it might work and try to reach out to doctors as soon as possible** :):

                - Humulin R U-100 
                - Novolin R FlexPen 
                - Novolin R ReliOn 
                - Novolin R FlexPen ReliOn 
                - Inhaled insulin (Afrezza) 
                - insulin aspart (Fiasp, Fiasp FlexTouch, 
                Fiasp PenFill, NovoLog, NovoLog FlexPen, NovoLog FlexTouch, 
                NovoLog PenFill, ReliOn NovoLog, ReliOn NovoLog FlexPen) 

                - metformin-alogliptin (Kazano) 
                - metformin-glipizide 

                - Consult with a Healthcare Professional: It's crucial to work closely with your healthcare provider, such as an endocrinologist or primary care physician, who can create a personalized diabetes management plan for you. They will help you understand your specific type of diabetes (Type 1, Type 2, or another type) and the best treatment options.
                
                - Educate Yourself: Knowledge is a powerful tool in managing diabetes. Take the time to learn about the condition, its causes, symptoms, and how it affects your body. Understand how food, exercise, and medication can impact your blood sugar levels.
                
                - Adopt a Healthy Diet: Focus on a balanced diet that includes plenty of vegetables, fruits, whole grains, lean proteins, and healthy fats. Limit your intake of sugary and processed foods, and be mindful of carbohydrate portions to help regulate blood sugar levels.
                
                - Regular Exercise: Incorporate regular physical activity into your daily routine. Aim for at least 150 minutes of moderate-intensity exercise per week, as recommended by your healthcare provider. Exercise helps improve insulin sensitivity and can assist in maintaining healthy blood sugar levels.
                
                - Monitor Blood Sugar Levels: Keep track of your blood sugar levels as directed by your healthcare provider. This will help you understand how your body responds to different foods, activities, and medications. It's an essential part of managing diabetes.
                
                - Medication and Insulin: If prescribed medication or insulin, take it as directed by your healthcare provider. Never adjust your medication regimen without consulting them first.
                
                - Stay Hydrated: Drink plenty of water throughout the day to help maintain good blood sugar control and overall health.
                
                - Stress Management: Stress can impact blood sugar levels. Find effective ways to manage stress, such as deep breathing exercises, meditation, yoga, or hobbies you enjoy.
                
                - Regular Check-ups: Attend regular follow-up appointments with your healthcare provider to monitor your progress and make any necessary adjustments to your treatment plan.
            
                
                """)
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
