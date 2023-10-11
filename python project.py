print("HI, THIS IS LYSA, your medical consultant")
print("We are ready to solve your problems, so please free to ask anything without hesitation")
name=input("Please enter you name:")
age=int(input("Please enter you age:"))
print("Here are some of the problems you can ask for recommendations, please be careful while typing your problem")
print("""
      Fever,
      Stress,
      Anxiety,
      Headache,
      Eye irritation,
      Cold,
      Cough,
      Indigestion,
      Sore throat,
      Menstrual cramp,
      Bad breathe,
      Insomnia,
      Shortness of breath,
      Ulcer,
      Abdominal pain,
      Skin burns,
      Constipation,
      Stomach upset,
      Diarrhoe,
      Dysentry,
      Low BP,
      High BP,
      Vomiting,
      Sneezing,
      Dizziness,
      Hair fall,
      Mouth ulcer,
      Sun burns,
      Leg pain,
      Sneezing,
      Fracture,
      Dry mouth,
      """)
#Fever

illness = input("Enter your illness/health problems:")
if illness == "Fever":
    try:
        temp = float(input("Enter your body temperature in celsius: "))
        if temp > 106:
            climate_change = input("Is there any significant climate change in your region (yes/no): ")
            if climate_change == "yes":
                how_long = int(input("How many days have you been suffering from this condition: "))
                if how_long > 3:
                    print("This is a serious issue.Make sure to get enough rest and stay hydrated. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue. Make sure to get enough rest and stay hydrated. Have more rest. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue.Make sure to get enough rest and stay hydrated. It's advisable to consult a doctor.")
        else:
            print("This might not be a severe issue. Make sure to get enough rest and stay hydrated.")
    except ValueError:
        print("Invalid input for body temperature. Please enter a valid temperature.")



#Stress
    
elif illness == "Stress":
    try:
        trigger = input("Is there any triggering situation that makes you stressed (yes/no): ")
        if trigger == "yes":
            how_long = int(input("How many days have you been experiencing stress (mention the number of days): "))
            if how_long > 2:
                physical_changes = input("Are you experiencing any physical changes in your body (yes/no): ")
                if physical_changes == "yes":
                    print("This is a serious issue.To manage stress, practice relaxation techniques like deep breathing and mindfulness. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue .To manage stress, practice relaxation techniques like deep breathing and mindfulness.Get more physical activity. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue.To manage stress, practice relaxation techniques like deep breathing and mindfulness. Get more physical activity. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. To manage stress, practice relaxation techniques like deep breathing and mindfulness. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")

elif illness == "Dry Mouth":
    try:
        duration = int(input("How long have you been experiencing dry mouth (mention it in the number of days only): "))
        if duration > 2:
            medication = input("Are you taking any medications that may cause dry mouth? (yes/no): ")
            if medication == "yes":
                print("Dry mouth can be a side effect of some medications. Please consult your prescribing doctor about alternatives or solutions.")
            else:
                underlying_condition = input("Do you have any underlying health conditions, such as diabetes or Sjögren's syndrome? (yes/no): ")
                if underlying_condition == "yes":
                    print("Dry mouth can be associated with certain medical conditions.Staying hydrated and chewing sugar-free gum or sucking on sugar-free candies can help alleviate it. It's advisable to consult a healthcare professional to manage the underlying condition.")
                else:
                    print("This might be a moderate issue.Maintain your oral condition good. Consider staying hydrated and using sugar-free lozenges or gum to alleviate dry mouth symptoms. If the problem persists, consult a healthcare professional.")
        else:
            print("This might not be a severe issue. Ensure you're drinking enough water and use sugar-free gum or lozenges to help with dry mouth.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


        
elif illness == "Fracture":
    try:
        location = input("Which part of your body is fractured? (e.g., arm, leg, wrist, etc.): ")
        if location:
            pain_intensity = input("On a scale of 1 to 10, how intense is the pain? (1 = low, 10 = high): ")
            if pain_intensity.isnumeric():
                pain_intensity = int(pain_intensity)
                if pain_intensity >= 7:
                    print("Severe pain in a fractured area is a serious concern. Please keep the injured area immobile and seek immediate medical attention.")
                else:
                    print("While not severe, any fracture should be evaluated by a medical professional. Immobilize the area, and consult a doctor or visit an emergency room.")
            else:
                print("Invalid input for pain intensity. Please enter a number between 1 and 10.")
        else:
            print("Please specify the location of the fracture.")
    except ValueError:
        print("Invalid input. Please enter valid responses.")

        
elif illness == "Leg Pain":
    try:
        pain_intensity = input("Is the pain intensity severe or mild? ")
        if pain_intensity == "severe":
            duration = int(input("How long have you been experiencing severe leg pain (in days)? "))
            if duration > 3:
                cause = input("Have you recently had any injury or trauma to your legs? (yes/no): ")
                if cause == "yes":
                    print("Severe and persistent leg pain after injury requires immediate medical attention.The simplest solution to leg pain is rest and over-the-counter pain relievers,  Consult a doctor or visit an emergency room.")
                else:
                    print("Severe and persistent leg pain should not be ignored.The simplest solution to leg pain is rest and over-the-counter pain relievers. Consult a doctor for a proper evaluation and treatment.")
            else:
                print("Mild leg pain may improve with rest and over-the-counter pain relief medication.place a heating pad in the painful areas.The simplest solution to leg pain is rest and over-the-counter pain relievers,  If it persists, consult a doctor.")
        else:
            print("Mild leg pain can often be managed with rest and over-the-counter pain relief. If it continues or worsens,The simplest solution to leg pain is rest and over-the-counter pain relievers,  consider consulting a doctor.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


#anxiety
    
elif illness == "Anxiety":
    try:
        trigger = input("Is there any triggering situation that makes you anxious (yes/no): ")
        if trigger == "yes":
            how_long = int(input("How many days have you been experiencing anxiety (mention the number of days): "))
            if how_long > 2:
                physical_sensation = input("Are you experiencing any physical sensations or restlessness (yes/no): ")
                if physical_sensation == "yes":
                    print("This is a serious issue. To manage anxiety, practice deep breathing and mindfulness techniques, and consider therapy or medication if needed. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue.To manage anxiety, practice deep breathing and mindfulness techniques, and consider therapy or medication if needed. Drinking of herbal water can reduce. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue. To manage anxiety, practice deep breathing and mindfulness techniques, and consider therapy or medication if needed. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. To manage anxiety, practice deep breathing and mindfulness techniques, and consider therapy or medication if needed. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


#Headaches
    
elif illness == "Headache":
    try:
        severity = input("Is your headache a dull ache or a sharp ache: ")
        if severity == "sharp ache":
            how_long = int(input("How many days have you been experiencing this sharp headache (mention the number of days): "))
            if how_long > 1:
                trigger = input("Is there any specific trigger for your headache (yes/no): ")
                if trigger == "yes":
                    print("This could be a serious issue.For a simple headache, try drinking water, resting, or taking over-the-counter pain relievers. Please consult a doctor immediately.")
                else:
                    print("This is also a serious issue. For a simple headache, try drinking water, resting, or taking over-the-counter pain relievers. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue.Applying a cold compresscan reduce the pain. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue.For a simple headache, try drinking water, resting, or taking over-the-counter pain relievers. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")

    

elif illness == "Eye irritation":
    try:
        symptom = input("Are you experiencing itching or burning in your eyes (yes/no): ")
        if symptom == "yes":
            how_long = int(input("How many days have you been experiencing eye irritation (mention the number of days): "))
            if how_long > 2:
                exposure_to_dust = input("Are your eyes exposed to dust or any foreign substance (yes/no): ")
                if exposure_to_dust == "yes":
                    print("This is a serious issue. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue.Warm compress can reduce the irritation. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input.  Please enter a valid response.")


#Cold    
elif illness == "Cold":
    try:
        how_long = int(input("How many days have you been suffering from cold (mention the number of days): "))
        if how_long > 2:
            symptom = input("Do you have a running nose or stuffy nose? ")
            if symptom == "running nose":
                close_contact = input("Have you had close contact with anyone who has a cold (yes/no): ")
                if close_contact == "yes":
                    print("This is a serious issue.Drinking warm can reduce the cold. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue.Drinking warm can reduce the cold. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue.Drinking warm can reduce the cold. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue.Drinking warm can reduce the cold. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")



#indigestion
    
elif illness == "Indigestion":
    try:
        how_long = int(input("How many days have you been suffering from indigestion (mention the number of days): "))
        if how_long > 2:
            symptom = input("Do you have a burning sensation? ")
            if symptom == "yes":
                uncooked_food = input("Have you consumed any uncooked food (yes/no): ")
                if uncooked_food == "yes":
                    print("This is a serious issue. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue.Intake of chamomile tea is good. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")




#sorethroat

elif illness == "Sore throat":
    try:
        how_long = int(input("How many days have you been suffering from a sore throat (mention the number of days): "))
        if how_long > 2:
            fever = input("Do you have a fever (yes/no)? ")
            if fever == "yes":
                discomfort = input("Do you have discomfort or a painful sensation in your throat (yes/no): ")
                if discomfort == "yes":
                    print("This is a serious issue. Please consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue.Intake of salt water can reduce the painful sensation. You should consider seeking medical advice.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


#Muscle cramp





#Menstrual cramp
    
elif illness == "Menstrual cramp":
    try:
        pain_intensity = input("Is the pain intensity normal (yes/no)? ")
        if pain_intensity == "no":
            menstrual_cycle = input("Is your menstrual cycle pattern normal (yes/no)? ")
            if menstrual_cycle == "no":
                blood_loss = input("Is there a lot of blood loss (yes/no)? ")
                if blood_loss == "yes":
                    print("Please take more rest, and if it continues, consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue.Intake of cinnamon tea is good. You should consider medical advice.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")



#Bad breathe        
elif illness == "Bad breathe":
    try:
        dental_issues = input("Do you have any dental issues (yes/no)? ")
        if dental_issues == "yes":
            how_long = int(input("How long have you been experiencing this (mention it in the number of days only): "))
            if how_long > 5:
                bad_habits = input("Have you been involved in bad habits (yes/no)? ")
                if bad_habits == "yes":
                    print("Please take more rest, and if it continues, consult a doctor immediately.")
                else:
                    print("This is a moderately serious issue. You should consider medical advice.")
            else:
                print("This might be a moderate issue.Keep your mouth clean. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


    

#insomnia        
elif illness == "Insomnia":
    try:
        sleep_pattern = input("Describe your sleep pattern (e.g., difficulty falling asleep, waking up frequently, trouble staying asleep): ")
        if "difficulty" in sleep_pattern:
            how_long = int(input("How long have you been experiencing sleep difficulties (mention it in the number of days only): "))
            if how_long > 7:
                bedtime_habits = input("Do you have any bedtime habits that may affect your sleep (e.g., using screens before bed, consuming caffeine, irregular sleep schedule)? ")
                if "screens" in bedtime_habits or "caffeine" in bedtime_habits:
                    print("Please make changes to your bedtime habits and consider practicing good sleep hygiene.")
                else:
                    print("This is a moderately serious issue. You should consider medical advice.")
            else:
                print("This might be a moderate issue.Takea light therapy. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue.Improve your sleeping habit. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


        
#Shortness of breathe        
elif illness == "Shortness of Breath":
    try:
        triggers = input("Do you have any triggers or specific situations that worsen your shortness of breath (e.g., physical activity, allergies, smoking)?: ")
        if "physical activity" in triggers or "allergies" in triggers:
            how_long = int(input("How long have you been experiencing shortness of breath (mention it in the number of days only): "))
            if how_long > 2:
                bad_habits = input("Do you have any unhealthy habits (e.g., smoking) that could be contributing to your shortness of breath?: ")
                if "smoking" in bad_habits:
                    print("It is a serious issue. Please consult a doctor immediately and consider quitting smoking.")
                else:
                    print("This is a moderately serious issue.Inhaling steam is good. You should consider medical advice.")
            else:
                print("This might be a moderate issue.Deep breath can help in this condition. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")

        
#Ulcer
        
elif illness == "Ulcer":
    try:
        eating_habits = input("Do you eat regularly and timely? (yes/no): ")
        if eating_habits == "no":
            how_long = int(input("How long have you been experiencing this issue (mention it in the number of days only): "))
            if how_long > 5:
                pain_while_eating = input("Can you eat and drink without any pain? (yes/no): ")
                if pain_while_eating == "no":
                    print("This is a moderately serious issue. You should consider medical advice and consult a doctor.")
                else:
                    print("It might be a moderate issue, but consult a doctor for further guidance.")
            else:
                print("This might not be a severe issue.Intake of aloe vera is good. Take proper care of yourself, but consider consulting a doctor.")
        else:
            print("Eating regularly and timely is essential for maintaining good health. Ensure you maintain healthy eating habits.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")


#Abdominal pain        
if illness == "Abdominal Pain":
    try:
        eating_habits = input("Do you eat regularly and timely? (yes/no): ")
        if eating_habits == "no":
            how_long = int(input("How long have you been experiencing this issue (mention it in the number of days only): "))
            if how_long > 5:
                drinking_water = input("Are you drinking water regularly? (yes/no): ")
                if drinking_water == "no":
                    print("This is a moderately serious issue. You should consider medical advice and consult a doctor.")
                else:
                    print("It might be a moderate issue, but consult a doctor for further guidance.")
            else:
                print("This might not be a severe issue. Take proper care of yourself, but consider consulting a doctor.")
        else:
            print("Maintaining regular and timely eating habits is crucial for good health. Ensure you eat properly.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")

        
#Skin burns        
elif illness == "Skin burns":
    try:
        causes =input("Is the burn is severe( that is the size and depth of the burn is severe)?:(yes/no)")
        if causes == "yes":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >5:
                try:
                    abc = input("Do you took any first aid?(yes/no):")
                    if abc == "no":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")


#Small pox
        
elif illness == "Small pox":
    try:
        causes =input("Do you have fever ?:(yes/no)")
        if causes == "yes":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >3:
                try:
                    abc = input("Do you took any rashes in your skin?(yes/no):")
                    if abc == "yes":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")

#Constipation
        
elif illness == "Constipation":
    try:
        causes =input("Have you hydrated?:(yes/no)")
        if causes == "no":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >3:
                try:
                    abc = input("Do you have stomach pain?(yes/no):")
                    if abc == "yes":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")

#Stomach upset        
elif illness == "Stomach upset":
    try:
        causes =input("Did you ate any contaminated foods(such as some street foods or spicy foods)?:(yes/no)")
        if causes == "yes":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >3:
                try:
                    abc = input("Do you have stomach pain?(yes/no):")
                    if abc == "yes":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")

#Diarrhea        
elif illness == "Diarrhea":
    try:
        causes =input("Did you ate any contaminated foods(such as some street foods or spicy foods)?:(yes/no)")
        if causes == "yes":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >3:
                try:
                    abc = input("Do you have stomach pain?(yes/no):")
                    if abc == "yes":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")

#Dysentry        
elif illness == "Dysentry":
    try:
        causes =input("Did you ate any contaminated foods(such as some street foods or spicy foods)?:(yes/no)")
        if causes == "yes":
            how_long = int(input("How long have you been experiencing this?:"))
            if how_long >3:
                try:
                    abc = input("Do you have stomach pain?(yes/no):")
                    if abc == "yes":
                        print("Please take more rest and if it continues, Please consult a doctor immediately.")
                    else:
                        print("This is a moderately serious issue. You should consider medical advice.")
                except ValueError:
                    print("Invalid input for the number of days.")
            else:
                print("This might be a moderate issue. Consider consulting a doctor.")
        else:
            print("This might not be a severe issue. Take proper care of yourself.")
    except ValueError:
        print("Invalid input for body temperature.")

#Low BP        
elif illness == "Low BP":
    try:
        symptoms = input("Are you experiencing symptoms of low blood pressure (e.g., dizziness, fatigue, fainting)?: (yes/no) ")
        if symptoms == "yes":
            try:
                systolic_bp = int(input("What is your current systolic blood pressure reading (the top number)?: "))
                if systolic_bp < 90:
                    print("Your systolic blood pressure is quite low. Please sit down, elevate your legs, and drink fluids. If symptoms persist, seek medical attention immediately.")
                else:
                    print("Your systolic blood pressure is not extremely low, but if you are experiencing symptoms, it's a good idea to rest and drink fluids. If symptoms persist, consider consulting a doctor.")
            except ValueError:
                print("Invalid input for systolic blood pressure.")
        else:
            print("If you're not experiencing symptoms, your low blood pressure may not be a severe issue. However, you should still monitor it and consider consulting a doctor if it persists.")
    except ValueError:
        print("Invalid input for symptoms.")

#High BP
elif illness == "High BP":
    try:
        symptoms = input("Are you experiencing symptoms of high blood pressure (e.g., headache, dizziness, shortness of breath)?: (yes/no) ")
        if symptoms == "yes":
            try:
                systolic_bp = int(input("What is your current systolic blood pressure reading (the top number)?: "))
                diastolic_bp = int(input("What is your current diastolic blood pressure reading (the bottom number)?: "))
                if systolic_bp > 180 or diastolic_bp > 120:
                    print("Your blood pressure is extremely high. You should sit down, relax, and avoid salty foods. Seek medical attention immediately.")
                else:
                    print("Your blood pressure is elevated, and if you're experiencing symptoms, it's advisable to rest and avoid salty foods. Consider consulting a doctor if symptoms persist.")
            except ValueError:
                print("Invalid input for blood pressure readings.")
        else:
            print("If you're not experiencing symptoms, your high blood pressure may not be an immediate emergency, but you should monitor it and consider consulting a doctor for management and advice.")
    except ValueError:
        print("Invalid input for symptoms.")


elif illness == "Vomiting":
    try:
        frequency = input("How often are you vomiting? (e.g., once, multiple times, continuously): ")
        if frequency == "continuously":
            print("Continuous vomiting can be a severe issue. Seek immediate medical attention.")
        elif frequency == "multiple times":
            try:
                last_meal = input("When was your last meal? (e.g., hours ago): ")
                if "hour" in last_meal and int(last_meal.split()[0]) < 24:
                    print("If you've vomited multiple times within the last few hours, it's important to rest your stomach and avoid eating. Sip clear fluids. If vomiting persists or is severe, consult a doctor.")
                else:
                    print("Vomiting multiple times can be a concern. Consider resting your stomach, sipping clear fluids, and consulting a doctor if it continues.")
            except ValueError:
                print("Invalid input for the time since your last meal.")
        elif frequency == "once":
            try:
                contents = input("What did you vomit? (e.g., food, bile, blood): ")
                if "blood" in contents:
                    print("Vomiting blood is a serious concern. Seek immediate medical attention.")
                else:
                    print("If you've vomited once and it doesn't contain blood, it may not be an immediate emergency. Rest your stomach and monitor. Consider consulting a doctor if it continues.")
            except ValueError:
                print("Invalid input for vomit contents.")
    except ValueError:
        print("Invalid input for vomiting frequency.")


elif illness == "Dizziness":
    try:
        duration = input("How long have you been experiencing dizziness? (e.g., minutes, hours, days): ")
        if "minute" in duration:
            print("If your dizziness has lasted only a few minutes, it may not be a severe issue. Rest, sit down, and drink water. If it persists, consider seeking medical advice.")
        elif "hour" in duration:
            print("Dizziness lasting for hours can be concerning. It's advisable to sit down, rest, and drink water. If it continues, consult a doctor.")
        elif "day" in duration:
            print("Experiencing dizziness for a whole day is a concern. You should rest and seek medical attention to determine the cause.")
        else:
            print("It's important to specify the duration of dizziness. Dizziness can have various causes, and a doctor's evaluation is recommended.")
    except ValueError:
        print("Invalid input for the duration of dizziness.")


elif illness == "Hair Fall":
    try:
        hair_loss_period = input("How long have you been experiencing hair fall? (e.g., weeks, months): ")
        if "week" in hair_loss_period:
            try:
                daily_hair_loss = int(input("How many strands of hair are you losing per day on average?: "))
                if daily_hair_loss < 100:
                    print("Losing a small number of hair strands per day is normal. You can improve your hair health with a balanced diet and proper hair care.")
                else:
                    print("If you're losing a significant number of hair strands daily, it might indicate an issue. Consider consulting a dermatologist or hair specialist for advice.")
            except ValueError:
                print("Invalid input for daily hair loss count.")
        elif "month" in hair_loss_period:
            print("Experiencing hair loss over the course of months can be a concern. Consider making lifestyle changes, such as a balanced diet and stress management. Consulting a dermatologist is also advisable.")
        else:
            print("It's important to specify the duration of hair fall. Prolonged or excessive hair loss may require professional evaluation by a dermatologist or hair specialist.")
    except ValueError:
        print("Invalid input for the duration of hair fall.")


elif illness == "Mouth Ulcer":
    try:
        number_of_ulcers = int(input("How many mouth ulcers do you have?: "))
        if number_of_ulcers == 1:
            print("If you have one mouth ulcer, it may not be a severe issue. Maintain good oral hygiene, avoid spicy or acidic foods, and consider using over-the-counter mouth ulcer treatments.")
        elif number_of_ulcers > 1:
            print("Having multiple mouth ulcers can be uncomfortable. Maintain good oral hygiene, avoid spicy or acidic foods, and consider using over-the-counter treatments. If they persist, consult a dentist or healthcare professional.")
        else:
            print("It's essential to specify the number of ulcers. If you have mouth ulcers, it's best to maintain oral hygiene and take appropriate measures. If they persist or worsen, consult a healthcare professional.")
    except ValueError:
        print("Invalid input for the number of mouth ulcers.")
        
elif illness == "Sunburn":
    try:
        exposure = input("Have you been exposed to the sun for an extended period? (yes/no): ")
        if exposure == "yes":
            how_long = int(input("How long have you been experiencing sunburn (mention it in the number of days only): "))
            if how_long > 2:
                blistering = input("Are there any blisters on your skin? (yes/no): ")
                if blistering == "yes":
                    print("It is a serious issue. Please consult a doctor immediately for proper treatment.")
                else:
                    print("This is a moderately serious issue. You should consider medical advice and take measures to relieve the sunburn.")
            else:
                print("This might not be a severe issue. Take proper care of yourself and try home remedies for sunburn relief.")
        else:
            print("Minimize sun exposure, apply sunscreen, and protect your skin to prevent further sunburn.")
    except ValueError:
        print("Invalid input. Please enter a valid response.")
        

else:
    print("Consult a doctor")
 



