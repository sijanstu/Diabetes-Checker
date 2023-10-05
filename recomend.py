import math
from random import random


def get_random_tips():
    food_array = [
        "1. Control Carbohydrate Intake:\n- Focus on complex carbohydrates like whole grains (e.g., brown rice, "
        "quinoa, whole wheat bread), legumes (e.g., lentils, beans), and vegetables.\n- Be mindful of portion sizes "
        "to help manage blood sugar levels.\n- Limit or avoid simple carbohydrates and sugary foods and drinks, "
        "including soda, candy, and sugary snacks.",
        "2. Choose Lean Proteins:\n- Opt for lean sources of protein such as skinless poultry, fish, lean cuts of "
        "meat, tofu, tempeh, and low-fat dairy products.\n- Protein can help stabilize blood sugar levels and keep "
        "you feeling full.",
        "3. Healthy Fats:\n- Include sources of healthy fats in your diet, such as avocados, nuts, seeds, and olive "
        "oil.\n- Limit saturated and trans fats, found in fried foods, processed snacks, and fatty cuts of meat.",
        "4. Fiber-Rich Foods:\n- Fiber can help control blood sugar levels and improve digestive health.\n- "
        "Incorporate fiber-rich foods like fruits, vegetables, whole grains, and legumes into your meals.",
        "5. Balanced Meals:\n- Aim for balanced meals that include a combination of carbohydrates, protein, "
        "and healthy fats.\n- This balance can help prevent spikes and crashes in blood sugar levels.",
        "6. Regular Meal Times:\n- Try to eat meals and snacks at consistent times each day to help regulate blood "
        "sugar levels.\n- Avoid skipping meals, as this can lead to unstable blood sugar.",
        "7. Monitor Your Blood Sugar:\n- Keep track of your blood sugar levels as recommended by your healthcare "
        "provider. This will help you understand how different foods affect your body.",
        "8. Stay Hydrated:\n- Drink plenty of water throughout the day to help with overall health and blood sugar "
        "regulation.",
        "9. Limit Alcohol Intake:\n- If you choose to consume alcohol, do so in moderation and be aware of its "
        "effects on blood sugar levels.\n- Alcohol can lead to low blood sugar in some cases.",
        "10. Individualized Plan:\n- Work with a registered dietitian or healthcare provider to create a personalized "
        "meal plan that takes into account your specific needs, preferences, and lifestyle."]

    life_style_array = [
        "- 1. Regular Physical Activity:\n- Engage in regular exercise as advised by your healthcare provider. Aim for "
        "at least 150 minutes of moderate-intensity aerobic activity per week.\n- Include both aerobic exercises ("
        "like walking, swimming, or cycling) and strength training to improve muscle mass and insulin sensitivity.",
        "- 2. Weight Management:\n- If overweight or obese, losing even a small amount of weight can have a significant"
        "impact on blood sugar control. Work with a healthcare provider or dietitian to set realistic weight loss "
        "goals.",
        "- 3. Balanced Diet:\n- Follow a balanced and individualized meal plan as recommended by your healthcare "
        "team.\n- Monitor carbohydrate intake, control portion sizes, and be mindful of the glycemic index of "
        "foods.\n- Limit processed and sugary foods and beverages.",
        "- 4. Regular Blood Sugar Monitoring:\n- Keep track of your blood sugar levels as prescribed by your healthcare "
        "provider. Regular monitoring helps you make informed decisions about your diet, exercise, and medication.",
        "- 5. Medication Management:\n- Take prescribed medications, including insulin, as directed by your healthcare "
        "provider. Follow the prescribed schedule and dosage.",
        "- 6. Stress Management:\n- High stress levels can affect blood sugar. Practice stress-reduction techniques "
        "such as deep breathing, meditation, yoga, or hobbies you enjoy.\n- Get adequate sleep to support overall "
        "health and stress management.",
        "- 7. Smoking Cessation:\n- If you smoke, consider quitting. Smoking can worsen the complications of diabetes "
        "and increase the risk of heart disease.",
        "- 8. Alcohol in Moderation:\n-If you choose to drink alcohol, do so in moderation. Limit consumption to one "
        "drink per day for women and up to two drinks per day for men.",
        "- 9. Regular Healthcare Check-ups:\n- Attend regular follow-up appointments with your healthcare provider to "
        "monitor your diabetes management and overall health.\n- Ensure you receive recommended screenings for eye, "
        "kidney, and nerve complications associated with diabetes.",
        "- 10. Education and Support:\n- Educate yourself about diabetes and its management. Attend diabetes education "
        "programs and support groups to connect with others facing similar challenges.\n- Reach out to healthcare "
        "professionals and dietitians for guidance and support.",
        "- 11. Foot Care:\n- Check your feet daily for cuts, sores, or blisters. Diabetes can affect blood flow to the "
        "extremities, making proper foot care essential.\n- Wear comfortable shoes and maintain good foot hygiene.",
        "- 12. Hydration:\n- Stay well-hydrated by drinking plenty of water throughout the day."]

    final_array = []
    for i in range(2):
        final_array.append(food_array[math.floor(random() * len(food_array))])
    for i in range(2):
        final_array.append(life_style_array[math.floor(random() * len(life_style_array))])
    return final_array
